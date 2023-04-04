import abc

from app.gateway.http_gateway import HttpGateway
from app.gateway.soup_gateway import SoupGateway
from app.model.service import Service


class Controller:
    def __init__(self, service: Service, http_gateway: HttpGateway, soup: SoupGateway):
        self.service = service
        self.http_gateway = http_gateway
        self.soup = soup

    @abc.abstractmethod
    def get_data(self) -> Service:
        ...


class ControllerIMPL:
    def __init__(self, service: Service, http_gateway: HttpGateway, soup: SoupGateway):
        self.service = service
        self.http_gateway = http_gateway
        self.soup = soup

    def get_data(self) -> dict[str, str]:
        for company in self.service.companies:
            for shop in company.shops:
                response = shop.get_response(self.http_gateway)
                data = self.soup.find_all(response, shop.attributes)
                shop.parse_response(data)

        return self.service.dict()
