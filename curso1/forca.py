import random
def escreve_arquivo():
    arquivo = open("palavras.txt", "w")
    palavras_secretas = ["Banana", "Pera", "laranja", "Uva"]
    for i in palavras_secretas:
        arquivo.write(i+"\n")
    arquivo.close()

def leitura_arquivo():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())

    palavra_sorteada = palavras[random.randrange(len(palavras))]
    return palavra_sorteada.upper()

def apresentacao(nome):
    print("##################################")
    print(f"Olá {nome}!")
    print("Bem vindo ao jogo da Forca!")
    print("##################################")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def perdedor():
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def jogar(nome):
    apresentacao(nome)
    palavra_secreta = leitura_arquivo()
    enforcou = False
    acertou = False
    letras_adivinhadas = ["_" for letra in palavra_secreta]
    letras_erradas = []
    chances = 0

    print("A palavra a ser adivinha contém {} letras".format(len(letras_adivinhadas)))
    print(letras_adivinhadas)

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()
        indice = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(letra == chute):
                    print("Encontrou a letra {} na posicao {}".format(chute, indice))
                    letras_adivinhadas[indice] = chute
                indice += 1
        else:
            print("Você errou!")

            if(chute not in letras_erradas):
                letras_erradas.append(chute)
            chances += 1
            desenha_forca(chances)

        enforcou = chances == 7
        acertou = "_" not in letras_adivinhadas

        print(letras_adivinhadas)
        print(letras_erradas)

    if(acertou):
        vencedor()
    else:
        print("Você perdeu! A palavra secreta era {} !".format(palavra_secreta))
        perdedor()

    print("Fim de Jogo!")