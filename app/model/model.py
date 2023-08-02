import abc

from bs4 import ResultSet
from pydantic import Field
from pydantic.networks import HttpUrl

from app.gateway.http_gateway import HttpGateway
from app.gateway.http_gateway import HttpResponse
from app.model.base import Model
from app.model.enums import Country
from app.model.type_alias import DictAny


class Book(Model):
    author: str
    topic: str = Field(min_length=1)
    price: str


class Shop(Model):
    country: Country
    url: HttpUrl
    attributes: DictAny = Field(exclude=True)
    headers: DictAny = Field(exclude=True)
    books: list[Book] = Field(default_factory=list)

    def get_response(self, http_client: HttpGateway) -> HttpResponse:
        return http_client.get(self.url, self.headers)

    @abc.abstractmethod
    def parse_response(self, response: ResultSet) -> None:
        ...


class Company(Model):
    name: str
    shops: list[Shop]
