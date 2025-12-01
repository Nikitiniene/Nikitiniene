import pandas as pd

# Lendo os dados do Arquivo CSV:

data_frame = pd.read_csv("dados.csv")
print(data_frame)

# Organizando os dados:

data_frame_org = data_frame.dropna()

# Calculando Estatística:

print("\nEstatísticas")
print("Preço Médio dos Produtos:", data_frame_org["Preco"].mean())

print("\nProduto Mais Caro:")

print(data_frame_org.sort_values("Preco",ascending=False).head(1))

print("\nProduto Mais Barato:")
print(data_frame_org.sort_values("Preco",ascending=True).head(1))