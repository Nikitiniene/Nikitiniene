import pandas as pd

# Lendo os dados do Arquivo CSV:

data_frame = pd.read_csv("dados.csv")
print(data_frame)

# Organizando os dados:

data_frame_org = data_frame.dropna()

# Calculando Estatística:

print("\nEstatísticas")
print("Idade média:", data_frame_org["Idade"].mean())
print("Salário médio:", data_frame_org["Salario"].mean())

# Listando os 3 Maiores Salários:

print("\nTOP 3 Maiores Salários:")
print(data_frame_org.sort_values("Salario",ascending=False).head(3))

# Listando os 3 Menores Salários: 

print("\nTOP 3 Menores Salários:")
print(data_frame_org.sort_values("Salario",ascending=True).head(3))