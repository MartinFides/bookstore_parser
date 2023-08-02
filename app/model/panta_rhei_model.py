import logging
import re

from bs4 import ResultSet
from pydantic import Field
from pydantic import HttpUrl
from pydantic import validator

from app.model.model import Book
from app.model.model import Shop
from app.model.type_alias import DictAny

logger = logging.getLogger(__name__)

RE_PRICE = r"^(?:\d+[.,]?\d*\s?)+\s?\W*$"
RE_FLOAT = r"^(?:[\"\']?\d+[.,]?\d*\s?[\"\']?)+$"
RE_PERCENTAGE = r"^-?\d+(\.\d+)?%$"

NOT_ALLOWED_TOPIC = ["e-kniha", "iba u nás", "Novinka"]
NOT_ALLOWED_CONTENT = ["CD", "DVD", "LP", "BRD", "náplň", "Podložka", "Diár", "diár"]


class PantaRheiBook(Book):
    price: str = Field(regex=RE_PRICE)

    @validator("topic", pre=True)
    def validate_topic(cls, value) -> str:
        if re.match(RE_FLOAT, value):
            raise ValueError("Value can be converted to float")

        if re.match(RE_PERCENTAGE, value):
            raise ValueError("Value is percentage number")

        if value in NOT_ALLOWED_TOPIC:
            raise ValueError("Not allowed topic")

        for x in NOT_ALLOWED_CONTENT:
            if x in value:
                raise ValueError(f"Not allowed value {x} found in topic")

        return value

    @validator("price", pre=True)
    def validate_price(cls, value) -> str:
        if not value:
            raise ValueError("Empty string")

        return value


class PantaRheiShopSk(Shop):
    attributes: DictAny = Field({"itemprop": "mainEntity"}, exclude=True)
    url: HttpUrl = "https://www.pantarhei.sk/"
    headers: DictAny = Field(
        {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Host": "www.google.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        },
        exclude=True,
    )

    def parse_response(self, response: ResultSet) -> None:
        for name in response:
            x = name.get_text()
            input_string = x.lstrip()
            split_list = re.split(r"\s{2,}", input_string)

            try:
                self.books.append(
                    Book(author=split_list[-3], topic=split_list[-4], price=split_list[-1])
                )

            except (ValueError, IndexError):
                logger.error(f"Couldn't parse response for {name=}.")
                pass
