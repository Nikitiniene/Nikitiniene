# Os números representam a distância em Km do Sol #

Planetas = {
    "Mercúrio": 57.9,     
    "Vênus": 108.2,
    "Terra": 149.6,
    "Marte": 227.9,
    "Júpiter": 778.6,
    "Saturno": 1433.5,
    "Urano": 2872.5,
    "Netuno": 4495.1
}

Planeta = input("Digite o nome de um Planeta do Sistema Solar: ")

if Planeta in Planetas:
    print(f"{Planeta} está a {Planetas[Planeta]} milhões de Km do Sol.")
else:
    print("Planeta não encontrado.")