
def cadastrar_animal(animais):
    nome = input("Digite o nome do animal: ")
    especie = input("Digite a espécie do animal: ")

    animal = [nome, especie]
    animais.append(animal)

    print("Animal cadastrado com sucesso!")
