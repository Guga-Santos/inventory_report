from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

product = [
    {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1"
    }
]

BLUE = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


def test_decorar_relatorio():
    report = ColoredReport(SimpleReport).generate(product)
    assert report == (
        f"{GREEN}Data de fabricação mais antiga:{RESET}"
        + f" {BLUE}2021-02-18{RESET}\n"
        f"{GREEN}Data de validade mais próxima:{RESET}"
        + f" {BLUE}2023-09-17{RESET}\n"
        f"{GREEN}Empresa com mais produtos:{RESET} {RED}Target{RESET}"
    )
