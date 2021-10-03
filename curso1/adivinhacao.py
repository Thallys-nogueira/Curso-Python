import numpy as np

def jogo_adivinhacao(nome):
    print("##################################")
    print(f"Olá {nome}!")
    print("Bem vindo ao jogo de Adivinhação!")
    print("##################################")

    numero_secreto = np.random.randint(0, 10)
    chute_usuario = int(input("Digite um número de 0 a 10: "))

    while(chute_usuario != numero_secreto):
        if(chute_usuario != numero_secreto):
            print("Você errou o número secreto!")
            print(f"O número secreto era: {numero_secreto}")
            numero_secreto = np.random.randint(0, 10)
            chute_usuario = int(input("Digite um novo número de 0 a 10: "))
    print("Você acertou o número secreto!")