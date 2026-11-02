import json

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