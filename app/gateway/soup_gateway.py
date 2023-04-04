import abc

from bs4 import BeautifulSoup
from bs4 import ResultSet

from app.gateway.http_gateway import HttpResponse


class SoupGateway:
    @staticmethod
    @abc.abstractmethod
    def find_all(response: HttpResponse, attributes: dict[str, str]) -> ResultSet:
        ...


class SoupGatewayIMPL(SoupGateway):
    @staticmethod
    def find_all(response: HttpResponse, attributes: dict[str, str]) -> ResultSet:
        soup = BeautifulSoup(response.text, "html.parser")

        return soup.find_all(**attributes)
