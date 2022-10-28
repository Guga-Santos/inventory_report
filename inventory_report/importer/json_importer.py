from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    @staticmethod
    def import_data(data):
        if data.endswith(".json"):
            return Inventory.read_data(data)
        else:
            raise ValueError("Arquivo inválido")
