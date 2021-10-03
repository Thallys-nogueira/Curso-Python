import numpy as np

def jogar(nome):
    print("##################################")
    print(f"Olá {nome}!")
    print("Bem vindo ao jogo de Adivinhação!")
    print("##################################")
    pontuacao = 1000
    tentativas = 0
    nivel = int(input("Digite qual nível do jogo você deseja: (1) - Fácil, (2) - Médio e (3) - Difícil: "))

    while(nivel != 1 and nivel != 2 and nivel != 3):
        nivel = int(input("Digite novamente qual nível do jogo você deseja: (1) - Fácil, (2) - Médio e (3) - Difícil: "))

    if(nivel == 1):
        numero_secreto = np.random.randint(0, 10)
        chute_usuario = int(input("Digite um número de 0 a 10: "))
    elif(nivel == 2):
        numero_secreto = np.random.randint(0, 100)
        chute_usuario = int(input("Digite um número de 0 a 100: "))
    elif(nivel == 3):
        numero_secreto = np.random.randint(0, 1000)
        chute_usuario = int(input("Digite um número de 0 a 1000: "))


    while(chute_usuario != numero_secreto):
        if(chute_usuario != numero_secreto):
            print("Você errou o número secreto!")
            print(f"O número secreto era: {numero_secreto}")
            numero_secreto = np.random.randint(0, 10)
            chute_usuario = int(input("Digite um novo número de 0 a 10: "))
        tentativas += 1
    pontuacao -= tentativas
    print("Você acertou o número secreto com {} tentativas, sua pontuação é {}!".format(tentativas, pontuacao))
    print("Fim de Jogo!")
