contatos = []


print("Bem vindo a sua agenda")
print("--------------------------------")
print("1 - Salvar contato")
print("2 - Editar contato")
print("3 - Listar contatos")
print("4 - Excluir contato")
print("5 - Marcar como favorito")
print("6 - Desmarcar como favorito")
print("7 - Listar favoritos")
print("8 - Sair")
print("--------------------------------")

opcao = int(input("Digite a opção desejada: "))

while opcao != 8:
    if opcao == 1:
        print("Digite o nome do contato: ")
        nome = input()
        print("--------------------------------")

        print("Digite o telefone do contato: ")
        telefone = input()
        print("--------------------------------")

        print("Digite o email do contato: ")
        email = input()
        print("--------------------------------")

        contatos.append({"id": len(contatos) + 1 ,"nome": nome, "telefone": telefone, "email": email, "favorito": False})
    elif opcao == 2:
        print("Digite o id do contato: ")
        id = int(input())
        print("--------------------------------")

        print("Digite o novo nome do contato: ")
        nome = input()
        print("--------------------------------")

        print("Digite o novo telefone do contato: ")
        telefone = input()

        print("Digite o novo email do contato: ")
        email = input()
        print("--------------------------------")

        contatos[id - 1]["nome"] = nome
        contatos[id - 1]["telefone"] = telefone
        contatos[id - 1]["email"] = email

        print("Contato editado com sucesso")
    elif opcao == 3:
        contatos.sort(key=lambda x: x["id"])
        for contato in contatos:
            print(f"ID: {contato['id']} - Nome: {contato['nome']} - Telefone: {contato['telefone']} - Email: {contato['email']} - Favorito: {contato['favorito']}")
    elif opcao == 4:
        print("Digite o id do contato: ")
        id = int(input())
        print("--------------------------------")

        contatos.pop(id - 1)
        print("Contato excluído com sucesso")
    elif opcao == 5:
        print("Digite o id do contato: ")
        id = int(input())
        print("--------------------------------")

        contatos[id - 1]["favorito"] = True
        print("Contato marcado como favorito com sucesso")
    elif opcao == 6:
        print("Digite o id do contato: ")
        id = int(input())
        print("--------------------------------")

        contatos[id - 1]["favorito"] = False
        print("Contato desmarcado como favorito com sucesso")
    elif opcao == 7:
        contatos.sort(key=lambda x: x["id"])
        for contato in contatos:
            if contato["favorito"]:
                print(f"ID: {contato['id']} - Nome: {contato['nome']} - Telefone: {contato['telefone']} - Email: {contato['email']} - Favorito: {contato['favorito']}")
        print("--------------------------------")
    else:
        print("Opção inválida")

    print("--------------------------------")
    opcao = int(input("Digite a opção desejada: "))

print("Obrigado por usar a agenda")