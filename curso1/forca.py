def jogar(nome):
    print("##################################")
    print(f"Olá {nome}!")
    print("Bem vindo ao jogo da Forca!")
    print("##################################")

    palavra_secreta = "laranja"
    enforcou = False
    acertou = False
    letras_adivinhadas = [""]*len(palavra_secreta)
    parte_corpo_cortada = ["Seu corpo foi cortado", "Sua cabeça foi cortada",
                           "Seu braço direito foi cortado","Seu braço esquerdo foi cortado",
                           "Sua perna direita foi cortada", "Sua perna esquerda foi cortada"]
    chances = len(parte_corpo_cortada)
    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        indice = 0
        for letra in palavra_secreta:
            if(letra == chute):
                print("Encontrou a letra {} na posicao {}".format(chute, indice))
                letras_adivinhadas[indice] = chute
            indice += 1

        print(letras_adivinhadas)