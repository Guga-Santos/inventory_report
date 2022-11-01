from collections.abc import Iterable

from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    @classmethod
    def __init__(cls, importer):
        cls.data = []
        cls.importer = importer

    def import_data(cls, path, type):
        list = cls.importer.import_data(path)
        cls.data.extend(list)
        return cls.type_selected(cls.data, type)

    def type_selected(cls, list, type):
        if type == "simples":
            return SimpleReport.generate(list)
        if type == "completo":
            return CompleteReport.generate(list)

    def __iter__(cls):
        return InventoryIterator(cls.data)
