from src.InstantiateCSVError import InstantiateCSVError
from src.item import Item
from pathlib import Path

if __name__ == '__main__':

    path = Path(__file__).parent.parent.joinpath("src").joinpath("items.csv")
    # Файл items.csv отсутствует.
    try:
        Item.instantiate_from_csv("path")
    except FileNotFoundError as e:
        print(e)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    try:
        Item.instantiate_from_csv(path)
    except InstantiateCSVError as e:
        print(e)
    # InstantiateCSVError: Файл item.csv поврежден
