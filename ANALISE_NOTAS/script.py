import pandas as pd

# Lendo o arquivo
data_frame = pd.read_csv("dados.csv")

# Média por aluno
data_frame["media"] = (data_frame["prova1"] + data_frame["prova2"] + data_frame["prova3"]) / 3

# Média geral
media_geral = data_frame["media"].mean()

# Maior média
maior = data_frame[data_frame["media"] == data_frame["media"].max()]

# Recuperação
recuperacao = data_frame[data_frame["media"] < 6]

print("Médias dos alunos:")
print(data_frame[["aluno", "media"]])

print("\nMédia geral da turma:")
print(media_geral)

print("\nAluno com maior média:")
print(maior[["aluno", "media"]])

print("\nAlunos em recuperação (média < 6):")
print(recuperacao[["aluno", "media"]])
