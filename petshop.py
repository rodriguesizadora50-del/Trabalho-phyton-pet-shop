
from cadastro import cadastrar_animal
from listagem import listar_animais
from pesquisa import pesquisar_animal
from servico import registrar_servico

animais = []

def menu():
    while True:
        print("\n===== PET SHOP Clube do Bicho =====")
        print("1 - Cadastrar animal")
        print("2 - Listar animais")
        print("3 - Pesquisar animal")
        print("4 - Registrar serviço")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_animal(animais)
        elif opcao == "2":
            listar_animais(animais)
        elif opcao == "3":
            pesquisar_animal(animais)
        elif opcao == "4":
            registrar_servico(animais)
        elif opcao == "5":
            print("Sistema encerrado!")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()

