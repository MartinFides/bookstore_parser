from abc import ABC
from abc import abstractmethod
from typing import Protocol

import requests


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
        return requests.get(url)
