pessoas = []

while True:
    print("\n--- Sistema de Cadastro ---")
    print("1 - Cadastrar pessoa")
    print("2 - Exibir pessoas cadastradas")
    print("3 - Sair")

    opcao = input("Digite um número dentre as opções acima: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))

        pessoa = {
            "nome": nome,
            "idade": idade
        }
        pessoas.append(pessoa)

    elif opcao == "2":
        for pessoa in pessoas:
            print(pessoa)
    
    elif opcao == "3":
        print("Encerrando o Sistema ...")
        break    