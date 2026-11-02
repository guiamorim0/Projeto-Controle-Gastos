from subalgoritmos import (registrar_gastos, listar_gastos)

print("""
MENU PRINCIPAL
0 - SAIR
1 - Registrar gasto
2 - Listar gastos
3 - Total por categoria
4 - Maior gasto
5 - Exportar para CSV e Excel
""")

while True:

    escolha = input("Escolha: ")

    if escolha == "1":
        while True:
            descricao = input("Descricao: ")
            if descricao == "":
                break

            categoria = input("Categoria: ")
            valor = float(input("Valor: "))

            registrar_gastos(descricao, categoria, valor)

        print("Gastos registrados com sucesso!")
        print("-" * 30)

    elif escolha == "2":
        listar_gastos()