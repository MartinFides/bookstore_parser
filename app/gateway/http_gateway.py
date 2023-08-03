from abc import ABC
from abc import abstractmethod
from http import HTTPStatus
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
    def get(self, url, headers) -> HttpResponse:
        pass


class HttpGatewayIMPL(HttpGateway):
    def get(self, url, headers) -> HttpResponse:
        response = requests.get(url, headers=headers)

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise ForbiddenError(f"Forbidden access to {url=}")
        elif not response.status_code == HTTPStatus.OK:
            raise ResponseError("Status code of response was not 200")

        return requests.get(url)
