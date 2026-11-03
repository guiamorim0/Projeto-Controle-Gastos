import json
import csv
from openpyxl import Workbook, load_workbook

def registrar_gastos(descricao: str, categoria: str, valor: float) -> str | None:
    try:
        with open("gastos.json", "r", encoding="utf-8") as arquivo:
            gastos = json.load(arquivo)
    except FileNotFoundError:
        pass
        gastos = []

    novo_gasto = {
                "descricao": descricao,
                "categoria": categoria,
                "valor": valor 
            }
            
    gastos.append(novo_gasto)      
    with open("gastos.json", "w", encoding="utf-8") as arquivo:
        json.dump(gastos, arquivo, indent=4)

def listar_gastos() -> None:
    try:
        with open("gastos.json", "r", encoding="utf-8") as arquivo:
            gastos = json.load(arquivo)
            for linha in gastos:
                print(f"{linha['descricao']} | {linha['categoria']} | R$ {linha['valor']:.2f}")
    except FileNotFoundError:
        print("ERRO! O arquivo gastos.json nao existe!")

def total_por_categoria() -> None:
    try:
        with open("gastos.json", "r", encoding="utf-8") as arquivo:
            gastos = json.load(arquivo)
            totais = {}
            for linha in gastos:
                categoria = linha["categoria"]
                valor = linha["valor"]

                if categoria in totais:
                    totais[categoria] += valor
                else:
                    totais[categoria] = valor

            for categoria, total in totais.items():
                print(f"{categoria}: R$ {total:.2f}")
    except FileNotFoundError:
        print("ERRO! O arquivo gastos.json nao existe!")

def maior_gasto() -> None:
    try:
        with open("gastos.json", "r", encoding="utf-8") as arquivo:
            gastos = json.load(arquivo)
            maior = gastos[0]
            for linha in gastos:
                if linha["valor"] > maior["valor"]:
                    maior = linha
            print(f"Maior gasto: {maior['descricao']} | {maior['categoria']} | R$ {maior['valor']:.2f}")
    except FileNotFoundError:
        print("ERRO! O arquivo gastos.json nao existe!")

def exportar_csv() -> None:
    try:
        with open("gastos.json", "r", encoding="utf-8") as arquivo:
            gastos = json.load(arquivo)
    except FileNotFoundError:
        print("ERRO! O arquivo gastos.json nao existe!")
        return

    with open("gastos.csv", "w", newline="", encoding="utf-8") as arquivo:
        gravador = csv.writer(arquivo, delimiter=",")
        gravador.writerow(['DESCRICAO', 'CATEGORIA', 'VALOR'])
        for linha in gastos:
            gravador.writerow([linha['descricao'], linha['categoria'], linha['valor']])

def exportar_excel() -> None:
    planilha = Workbook()
    aba = planilha.active
    aba.title = "Gastos"
    
    aba["A1"] = "Descricao"
    aba["B1"] = "Categoria"
    aba["C1"] = "Valor"
    
    try:
        with open("gastos.json", "r", encoding="utf-8") as arquivo:
            gastos = json.load(arquivo)
    except FileNotFoundError:
        print("ERRO! O arquivo gastos.json nao existe!")
        return

    for numero_linha, linha in enumerate(gastos, 2):
        aba[f"A{numero_linha}"] = linha['descricao']
        aba[f"B{numero_linha}"] = linha['categoria']
        aba[f"C{numero_linha}"] = float(linha['valor'])

    planilha.save("gastos.xlsx")
    