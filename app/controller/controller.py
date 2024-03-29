import abc
import logging

from app.gateway.http_gateway import HttpGateway
from app.gateway.soup_gateway import SoupGateway
from app.model.service import Service

logger = logging.getLogger(__name__)


class Controller:
    def __init__(self, service: Service, http_gateway: HttpGateway, soup_gateway: SoupGateway):
        self.service = service
        self.http_gateway = http_gateway
        self.soup_gateway = soup_gateway

    @abc.abstractmethod
    def get_data(self) -> Service:
        ...


class ControllerIMPL(Controller):
    def get_data(self) -> dict[str, str]:
        for company in self.service.companies:
            for shop in company.shops:
                logger.info(f"Getting response from {shop=}")
                response = shop.get_response(self.http_gateway)
                data = self.soup_gateway.find_all(response, shop.attributes)

                logger.info("Parsing response")
                shop.parse_response(data)

        return self.service.dict()
