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