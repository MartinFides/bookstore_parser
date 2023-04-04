from pprint import pprint

from app.controller.controller import ControllerIMPL
from app.gateway.http_gateway import HttpGatewayIMPL
from app.gateway.soup_gateway import SoupGatewayIMPL
from app.model.service import ServiceIMPL


def parse_books():
    service = ServiceIMPL.compose()
    http_client = HttpGatewayIMPL()
    soup = SoupGatewayIMPL()

    controller = ControllerIMPL(service=service, http_gateway=http_client, soup=soup)

    pprint(controller.get_data())


if __name__ == "__main__":
    parse_books()