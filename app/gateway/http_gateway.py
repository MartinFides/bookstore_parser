from abc import ABC
from abc import abstractmethod
from typing import Protocol

import requests

from app.gateway.exceptions import ForbiddenError
from app.gateway.exceptions import ResponseError


class HttpResponse(Protocol):
    @property
    @abstractmethod
    def text(self) -> str:
        pass


class HttpGateway(ABC):
    @abstractmethod
    def get(self, url) -> HttpResponse:
        pass


class HttpGatewayIMPL(HttpGateway):
    def get(self, url) -> HttpResponse:
        response = requests.get(url)

        if response.status_code == 403:
            raise ForbiddenError(f"Forbidden access to {url=}")
        elif not response.status_code == 200:
            raise ResponseError("Status code of response was not 200")

        return requests.get(url)
