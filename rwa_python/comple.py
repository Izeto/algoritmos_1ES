import random


def opc1():
    link = "dados.txt"
    modo = "r"
    arq = open(link, modo)

    conteudo = arq.readlines()

    maior = -11111111
    soma = 0
    par = 0

    for i in range(0, len(conteudo)):
        nome = int(conteudo[i])
        print(nome)
        if(nome > maior):
            maior = nome

        if(nome % 2 == 0):
            par = par + 1

        soma += nome

        media = soma/len(conteudo)

    print("\nO maior número é: ", maior)
    print("\nA média é: ", round(media, 2))
    print("\nQuantidade de números pares: ", par)
        
    arq.close()
    
def opc2():
    link = "dados.txt"
    modo = "a"

    n = random.randint(1, 100)

    arq = open(link, modo)

    arq.write(str(n)+"\n")

    arq.close()

def opc3():
    link = "dados.txt"
    modo = "a"

    n = input("\nInsira o número: ")

    arq = open(link, modo)

    arq.write(str(n) + "\n")

    arq.close()

def opc4():
    print("\nFinalizando ...")
    