
def listar_animais(animais):
    if len(animais) == 0:
        print("Nenhum animal cadastrado.")
    else:
        for animal in animais:
            print("Nome:", animal[0])
            print("Espécie:", animal[1])
            print("--------------------")
