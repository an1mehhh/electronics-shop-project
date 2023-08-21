from src.phone import Phone
import pytest


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_for_number_of_sim(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone.number_of_sim == 2

    assert phone + phone == 10
