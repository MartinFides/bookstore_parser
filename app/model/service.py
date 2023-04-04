import abc
from typing import Self

from app.model.base import Model
from app.model.enums import Country
from app.model.model import Company
from app.model.model import PantaRheiSk


class Service(Model):
    companies: list[Company]

    @classmethod
    @abc.abstractmethod
    def compose(cls) -> Self:
        ...


class ServiceIMPL(Service):
    companies: list[Company]

    @classmethod
    def compose(cls) -> Self:
        return cls(
            companies=[Company(name="Panta Rhei", shops=[PantaRheiSk(country=Country.SLOVAKIA)])]
        )
