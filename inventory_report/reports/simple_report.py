import csv
from datetime import date
from statistics import mode


def read(path):
    with open(path, encoding="utf-8") as data:
        return [*csv.DictReader(data)]


class SimpleReport:
    @classmethod
    def generate(cls, data):
        now = date.today().isoformat()

        min_fabr_date = min(product["data_de_fabricacao"] for product in data)

        company = mode(product["nome_da_empresa"] for product in data)

        min_val_date = min([product["data_de_validade"] for product in data
                            if product["data_de_validade"] > now])

        return (
              f"Data de fabricação mais antiga: {min_fabr_date}\n"
              f"Data de validade mais próxima: {min_val_date}\n"
              f"Empresa com mais produtos: {company}"
          )
