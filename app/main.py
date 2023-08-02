import json
import logging.config
from pathlib import Path
from pprint import pprint

from app.controller.controller import ControllerIMPL
from app.gateway.http_gateway import HttpGatewayIMPL
from app.gateway.soup_gateway import SoupGatewayIMPL
from app.model.service import ServiceIMPL
from app.util import get_file_path

logger = logging.getLogger(__name__)
LOGGING_SETTINGS = "logging.json"


def configure_logging(config: Path) -> None:
    if config.exists():
        with config.open() as f:
            loaded_config = json.load(f)
            logging.config.dictConfig(loaded_config)
    else:
        raise FileNotFoundError(f"Couldn't configure the logger using {config!r}")


def parse_books():
    logger.info("Setting up")
    service = ServiceIMPL.compose()
    http_gateway = HttpGatewayIMPL()
    soup_gateway = SoupGatewayIMPL()

    controller = ControllerIMPL(
        service=service, http_gateway=http_gateway, soup_gateway=soup_gateway
    )

    result = controller.get_data()

    logger.info("Printing result")
    pprint(result)


if __name__ == "__main__":
    configure_logging(get_file_path(LOGGING_SETTINGS))
    parse_books()
