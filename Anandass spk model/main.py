import sys
from colorama import Fore, Style
from model import Base, Laptop
from engine import engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import (
    DEV_SCALE_brand,
    DEV_SCALE_ram,
    DEV_SCALE_prosesor,
    DEV_SCALE_storage,
    DEV_SCALE_baterai,
    DEV_SCALE_harga,
    DEV_SCALE_webcam,
)

session = Session(engine)


def create_table():
    Base.metadata.create_all(engine)
    print(f"{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has created!")


class BaseMethod:
    def __init__(self):
        # 1-5
        self.raw_weight = {
            "brand": 5,
            "ram": 4,
            "prosesor": 4,
            "storage": 4,
            "baterai": 5,
            "harga": 1,
            "webcam": 2,
        }

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v / total_weight, 2) for k, v in self.raw_weight.items()}

    @property
    def data(self):
        query = select(Laptop)
        return [
            {
                "id": laptop.id,
                "brand": DEV_SCALE_brand.get(laptop.brand, 0),
                "ram": DEV_SCALE_ram.get(laptop.ram, 0),
                "prosesor": DEV_SCALE_prosesor.get(laptop.prosesor, 0),
                "storage": DEV_SCALE_storage.get(laptop.storage, 0),
                "baterai": DEV_SCALE_baterai.get(laptop.baterai, 0),
                "harga": DEV_SCALE_harga.get(laptop.harga, 0),
                "webcam": DEV_SCALE_webcam.get(laptop.webcam, 0),
            }
            for laptop in session.query(Laptop).all()
        ]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        brands = []  # max
        ram = []  # max
        prosesor = []  # max
        storage = []  # max
        baterai = []  # max
        harga = []  # min
        webcam = []  # max
        for data in self.data:
            brands.append(data["brand"])
            ram.append(data["ram"])
            prosesor.append(data["prosesor"])
            storage.append(data["storage"])
            baterai.append(data["baterai"])
            harga.append(data["harga"])
            webcam.append(data["webcam"])
        max_brand = max(brands)
        max_ram = max(ram)
        max_prosesor = max(prosesor)
        max_storage = max(storage)
        max_baterai = max(baterai)
        min_harga = min(harga)
        max_webcam = max(webcam)
        return [
            {
                "id": data["id"],
                "brand": data["brand"] / max_brand,  # benefit
                "ram": data["ram"] / max_ram,  # benefit
                "prosesor": data["prosesor"] / max_prosesor,  # benefit
                "storage": data["storage"] / max_storage,  # benefit
                "baterai": data["baterai"] / max_baterai,  # benefit
                "harga": min_harga / data["harga"],  # cost
                "webcam": data["webcam"] / max_webcam,  # benefit
            }
            for data in self.data
        ]


class WeightedProduct(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result = {
            row["id"]: round(
                row["brand"] ** weight["brand"]
                * row["ram"] ** weight["ram"]
                * row["prosesor"] ** weight["prosesor"]
                * row["storage"] ** weight["storage"]
                * row["baterai"] ** weight["baterai"]
                * row["harga"] ** weight["harga"]
                * row["webcam"] ** weight["webcam"],
                2,
            )
            for row in self.normalized_data
        }
        # sorting
        return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))


class SimpleAdditiveWeighting(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight
        result = {
            row["id"]: round(
                row["brand"] * weight["brand"]
                + row["ram"] * weight["ram"]
                + row["prosesor"] * weight["prosesor"]
                + row["storage"] * weight["storage"]
                + row["baterai"] * weight["baterai"]
                + row["harga"] * weight["harga"]
                + row["webcam"] * weight["webcam"],
                2,
            )
            for row in self.normalized_data
        }
        # sorting
        return dict(
            sorted(result.items(), key=lambda x: x[1], reverse=True)
        )  # Sorting descending


def run_saw():
    saw = SimpleAdditiveWeighting()
    print("result:", saw.calculate)


def run_wp():
    wp = WeightedProduct()
    print("result:", wp.calculate)


if len(sys.argv) > 1:
    arg = sys.argv[1]

    if arg == "create_table":
        create_table()
    elif arg == "saw":
        run_saw()
    elif arg == "wp":
        run_wp()
    else:
        print("command not found")
