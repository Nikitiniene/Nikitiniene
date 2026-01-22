vendas = []

while True:
    valor = input("Digite o valor da venda ou 'fim' para encerrar: ")

    if valor.lower() == "fim":
        break

    vendas.append(float(valor))

print("\nTOTAL DE VENDAS:", len(vendas))
print("SOMA DAS VENDAS:",sum(vendas))
