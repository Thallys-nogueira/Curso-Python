import adivinhacao
import forca

def escolhe_jogo():
    print("#################################")
    print("Escolha qual jogo você deseja:")
    print("1- Adivinhação")
    print("2- Forca")

    opcao = int(input("Digite a opção desejada:"))
    nome = input(f"Digite seu nome: ")
    if(opcao == 1):
        adivinhacao.jogar(nome)
    elif(opcao == 2):
        #forca.escreve_arquivo()
        forca.jogar(nome)
    else:
        while(opcao !=1 or opcao!=2):
            opcao = int(input("Digite a opção desejada:"))

if(__name__ == "__main__"):
    escolhe_jogo()