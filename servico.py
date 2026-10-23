
def registrar_servico(animais):
    nome_pesquisa = input("Digite o nome do animal: ")

    encontrado = False

    for animal in animais:
        if animal[0].lower() == nome_pesquisa.lower():
            servico = input("Digite o serviço (Banho ou Tosa): ")
            valor = float(input("Digite o valor do serviço: "))

            print("Serviço registrado com sucesso!")
            print("Animal:", animal[0])
            print("Serviço:", servico)
            print("Valor: R$", valor)

            encontrado = True

    if encontrado == False:
        print("Animal não encontrado.")
