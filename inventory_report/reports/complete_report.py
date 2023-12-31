import csv
from collections import Counter

from .simple_report import SimpleReport


def read(path):
    with open(path, encoding="utf-8") as data:
        return [*csv.DictReader(data)]


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        simple_report = super().generate(data)

        quantity_per_company = Counter(
            product["nome_da_empresa"] for product in data)

        report = "Produtos estocados por empresa:\n"

        for company in quantity_per_company:
            report += f"- {company}: {quantity_per_company[company]}\n"

        return (
            f"{simple_report}\n"
            f"{report}"
        )
