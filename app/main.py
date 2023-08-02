import logging
import logging.config
from pprint import pprint

from app.controller.controller import ControllerIMPL
from app.gateway.exceptions import GatewayError
from app.gateway.http_gateway import HttpGatewayIMPL
from app.gateway.soup_gateway import SoupGatewayIMPL
from app.logging_config import LOGGING_CONFIG
from app.model.service import ServiceIMPL

logger = logging.getLogger(__name__)


def configure_logging() -> None:
    logging.config.dictConfig(LOGGING_CONFIG)


def parse_books():
    logger.info("Setting up")
    service = ServiceIMPL.compose()
    http_gateway = HttpGatewayIMPL()
    soup_gateway = SoupGatewayIMPL()

    controller = ControllerIMPL(
        service=service, http_gateway=http_gateway, soup_gateway=soup_gateway
    )

    try:
        result = controller.get_data()

        logger.info("Printing result")
        pprint(result)

    except GatewayError as e:
        logger.error(f"Could not get response because of: {e}")


if __name__ == "__main__":
    configure_logging()
    parse_books()
