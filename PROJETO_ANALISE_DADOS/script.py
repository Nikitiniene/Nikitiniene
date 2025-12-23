import pandas as pd

dados = {
    "Produtos": ["Relógio","Mouse","Teclado","Notebook","Monitor","Celular"],
    "Categoria": ["Acessório","Acessório","Acessório","Eletrônico","Eletrônico","Eletrônico"],
    "Vendas": [8,6,7,3,2,4],
    "Valor_Unidade": [90,60,50,2000,1000,1300]
}

df = pd.DataFrame(dados)

df["Faturamento"] = df["Vendas"] * df["Valor_Unidade"]

print(df)