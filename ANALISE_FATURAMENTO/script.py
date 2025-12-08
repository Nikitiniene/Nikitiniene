Receita = float(input("Digite a receita: R$ "))
Custo = float(input("Digite o custo: R$ "))

Lucro = Receita - Custo

print(f"\nLucro: R$ {Lucro:.2f}")

if Lucro > 0:
    print("Situação: LUCRATIVO")
elif Lucro == 0:
    print("Situação: PONTO DE EQUILÍBRIO")
else:
    print("Situação: PREJUÍZO")
