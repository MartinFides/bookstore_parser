from copy import deepcopy

import pytest

from app.model.model import Book

VALID_DATA = {"author": "Adam Grant", "topic": "Ešte si to premysli", "price": "17,06 €"}

VALID_TOPICS = ["Max. Holandský majster Formuly 1", "Púštna hviezda", "Gemer: Deň prvý"]

INVALID_TOPICS = [
    "Separ - Flowdemort CD",
    "Ježek Sonic 2 DVD",
    "Elán - Nebezpečný náklad LP",
    "Zaz - Sur La Route BRD",
    "Inšpiratívny diár Navzájom lepší 2023",
    "10%",
    "e-kniha",
    "iba u nás",
    "Novinka",
    "1",
    "1.1",
    "1,1",
]


class TestBook:
    @pytest.mark.parametrize("topic", VALID_TOPICS)
    def test_can_create_with_valid_topic(self, topic: str) -> None:
        data = deepcopy(VALID_DATA)
        data["topic"] = topic

        actual = Book.parse_obj(data)

        assert isinstance(actual, Book)

    @pytest.mark.parametrize("invalid_topic", INVALID_TOPICS)
    def test_can_raise_error_with_invalid_topic(self, invalid_topic: str) -> None:
        data = deepcopy(VALID_DATA)
        data["topic"] = invalid_topic

        with pytest.raises(ValueError):
            Book.parse_obj(data)
