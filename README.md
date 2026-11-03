# Controle de Gastos

Programa de terminal em Python para registrar gastos, ver resumos e exportar os dados para CSV e Excel.

Projeto de estudo com menu, subalgoritmos, dicionários, arquivos JSON/CSV/Excel e tratamento de erros.

## Funcionalidades

- **Registrar gasto:** pede descrição, categoria e valor, e acrescenta ao `gastos.json` sem apagar os anteriores.
- **Listar gastos:** mostra todos os gastos registrados.
- **Total por categoria:** soma os valores de cada categoria.
- **Maior gasto:** mostra o gasto de maior valor.
- **Exportar:** gera `gastos.csv` e `gastos.xlsx` a partir do JSON.

## Estrutura do projeto

```
.
├── main.py             # menu e fluxo do programa
├── subalgoritmos.py    # funções de cada funcionalidade
└── README.md
```

Os arquivos `gastos.json`, `gastos.csv` e `gastos.xlsx` são criados na pasta do projeto durante o uso.

## Como rodar

1. Instale o Python 3.11 ou mais recente.
2. Instale a biblioteca do Excel:

```
py -m pip install openpyxl
```

3. Rode o programa na pasta do projeto:

```
py main.py
```

## Como usar

```
MENU PRINCIPAL
0 - SAIR
1 - Registrar gasto
2 - Listar gastos
3 - Total por categoria
4 - Maior gasto
5 - Exportar para CSV e Excel
```

Na opção 1, deixe a descrição vazia e aperte Enter para encerrar o cadastro.

### Exemplo

Gastos registrados:

| Descrição | Categoria   | Valor  |
|-----------|-------------|--------|
| Mercado   | Alimentacao | 150.50 |
| Onibus    | Transporte  | 80.00  |
| Pizza     | Alimentacao | 80.00  |
| Cinema    | Lazer       | 45.00  |

Total por categoria:

```
Alimentacao: R$ 230.50
Transporte: R$ 80.00
Lazer: R$ 45.00
```

Maior gasto:

```
Maior gasto: Mercado | Alimentacao | R$ 150.50
```

## Formato dos dados

Cada gasto é um dicionário, e o `gastos.json` guarda uma lista deles:

```json
[
    {
        "descricao": "Mercado",
        "categoria": "Alimentacao",
        "valor": 150.5
    }
]
```

## Conceitos praticados

- Menu com `while True` e subalgoritmos com tipagem
- Lista de dicionários e dicionário como acumulador
- Leitura e escrita de JSON, CSV e Excel (`json`, `csv`, `openpyxl`)
- `try/except` para arquivo inexistente

## Melhorias futuras

- Tratar valor inválido (`ValueError`) ao registrar um gasto
- Opção para remover um gasto, usando um `id` para cada registro
- Campo de data em cada gasto

## Autor

Guilherme Amorim