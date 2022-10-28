import csv
import json

from ..reports.complete_report import CompleteReport
from ..reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if type == "simples":
            data = cls.read_data(path)
            return SimpleReport.generate(data)
        if type == "completo":
            data = cls.read_data(path)
            return CompleteReport.generate(data)

    def read_data(list):
        if list.endswith(".csv"):
            with open(list, encoding="utf-8") as data:
                return [*csv.DictReader(data)]
        if list.endswith(".json"):
            with open(list) as data:
                return json.load(data)
