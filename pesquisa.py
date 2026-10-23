
def pesquisar_animal(animais):
    nome_pesquisa = input("Digite o nome do animal que deseja encontrar: ")

    encontrado = False

    for animal in animais:
        if animal[0].lower() == nome_pesquisa.lower():
            print("Animal encontrado!")
            print("Nome:", animal[0])
            print("Espécie:", animal[1])
            encontrado = True

    if encontrado == False:
        print("Animal não encontrado.")
