import abc
import re

from bs4 import ResultSet
from pydantic import Field
from pydantic import validator
from pydantic.networks import HttpUrl

from app.gateway.http_gateway import HttpGateway
from app.gateway.http_gateway import HttpResponse
from app.model.base import Model
from app.model.enums import Country

RE_PRICE = r"^(?:\d+[.,]?\d*\s?)+\s?\W*$"
RE_FLOAT = r"^(?:[\"\']?\d+[.,]?\d*\s?[\"\']?)+$"
RE_PERCENTAGE = r"^-?\d+(\.\d+)?%$"

NOT_ALLOWED_TOPIC = ["e-kniha", "iba u nás", "Novinka"]
NOT_ALLOWED_CONTENT = ["CD", "DVD", "LP", "BRD", "náplň", "Podložka", "Diár", "diár"]


class Book(Model):
    author: str
    topic: str = Field(min_length=1)
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


class Shop(Model):
    country: Country
    url: HttpUrl
    attributes: dict[str, str] = Field(exclude=True)
    books: list[Book] = Field(default_factory=list)

    def get_response(self, http_client: HttpGateway) -> HttpResponse:
        return http_client.get(self.url)

    @abc.abstractmethod
    def parse_response(self, response: ResultSet) -> None:
        ...


class PantaRheiSk(Shop):
    attributes: dict[str, str] = Field({"itemprop": "mainEntity"}, exclude=True)
    url: HttpUrl = "https://www.pantarhei.sk/"

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
                # todo: Implement logging
                pass


class Company(Model):
    name: str
    shops: list[Shop]
