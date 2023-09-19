import pytest
from pathlib import Path

from src.InstantiateCSVError import InstantiateCSVError


def test_file_not_found(item):
    # �������� �� ���������� �����
    # �������� ������ � �������� �����
    path = Path(__file__).parent.parent.joinpath("src").joinpath("ite1ms.csv")
    with pytest.raises(FileNotFoundError) as excinfo:
        item.instantiate_from_csv(path)


def test_file_not_found_InstantiateCSVError(item):
    # �������� �� ����������� �����
    path = Path(__file__).parent.parent.joinpath("src").joinpath("items.csv")
    with pytest.raises(InstantiateCSVError) as excinfo:
        item.instantiate_from_csv(path)
