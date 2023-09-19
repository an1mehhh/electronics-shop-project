from src.item import Item
import pytest


@pytest.fixture
def item():
    return Item("Smartphone", 10000, 20)
