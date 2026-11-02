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
       