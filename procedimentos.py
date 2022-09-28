#Exercício 1

import math


def soma2num(num1, num2):
    somaResul = num1+num2
    print(f"\nO resultado da soma dos 2 números é: {somaResul}")


def mult2num(num1, num2):
    multResul = num1*num2
    print(f"\nO resultado da multiplicação dos 2 números é: {multResul}")


def raizNum(raiz):
    raizCalc = round(math.sqrt(raiz), 2)
    print(f"\nA raiz quadrada de {raiz} é {raizCalc}")


def pow2num(num1, num2):
    powResul = num1**num2
    print(f"\nO resultado da potência é: {powResul}")


def tabu(num1):
    for x in range(0, 11):
        tabuada = num1 * x
        print(f"{num1} x {x} = {tabuada}")


def menuPrincipal():
    x = False

    while(x == False):

        print("\n====== Menu Principal ======")
        print("\n1. Somar dois números")
        print("\n2. Multiplicar dois números")
        print("\n3. Raiz Quadrada")
        print("\n4. Potência")
        print("\n5. Tabuada")
        print("\n6. Sair")

        try:

            opc = int(float(input("\nInsira sua opção: ")))

        except:

            print("Houve um problema!")

            continue

        if(opc > 6 or opc < 1):
            print("\nApenas entre 1 e 6!")
        elif(opc == 1):
            y = int(input("\nInsira 1 número: "))
            z = int(input("\nInsira 2 número: "))
            soma2num(y, z)
        elif(opc == 2):
            y = int(input("\nInsira 1 número: "))
            z = int(input("\nInsira 2 número: "))
            mult2num(y, z)
        elif(opc == 3):
            z = int(input("\nInsira o número: "))
            raizNum(z)
        elif(opc == 4):
            y = int(input("\nInsira 1 número: "))
            z = int(input("\nInsira 2 número: "))
            pow2num(y, z)
        elif(opc == 5):
            z = int(input("\nInsira o número: "))
            tabu(z)
        else:
            print("\nFinalizando ...")
            break


menuPrincipal()



import math
import random


def soma2num(num1, num2):
    somaResul = num1+num2
    print(f"\nO resultado da soma dos 2 números é: {somaResul}")


def mult2num(num1, num2):
    multResul = num1*num2
    print(f"\nO resultado da multiplicação dos 2 números é: {multResul}")


def raizNum(raiz):
    raizCalc = round(math.sqrt(raiz), 2)
    print(f"\nA raiz quadrada de {raiz} é {raizCalc}")


def pow2num(num1, num2):
    powResul = num1**num2
    print(f"\nO resultado da potência é: {powResul}")


def tabu(num1):
    for x in range(0, 11):
        tabuada = num1 * x
        print(f"{num1} x {x} = {tabuada}")

# ========== Junção exercícios 1 e 2 ==========

def printVetor(vet):
    for i in range(0,len(vet)):
        print(F"\nValor contido no índice {i} está {vet[i]}")

def numMaior(vet):
    maior = vet[0]
    for y in range(0,len(vet)):
        if(vet[y]>maior):
            maior=vet[y]
    
    print(f"\nO maior número é {maior}")

def numMenor(vet):
    menor = vet[0]
    for q in range(0,len(vet)):
        if(vet[q]<menor):
            menor=vet[q]
    
    print(f"\nO menor número é {menor}")



def menuPrincipal():
    x = False

    while(x == False):

        print("\n====== Menu Principal ======")
        print("\n1. Somar dois números")
        print("\n2. Multiplicar dois números")
        print("\n3. Raiz Quadrada")
        print("\n4. Potência")
        print("\n5. Tabuada")
        print("\n6. Imprimir Vetor")
        print("\n7. Maior Número do Vetor")
        print("\n8. Menor Número do Vetor")
        print("\n9. Sair")

        try:

            opc = int(float(input("\nInsira sua opção: ")))

        except:

            print("\nHouve um problema!")

            continue

        if(opc > 9 or opc < 1):
            print("\nApenas entre 1 e 9!")
        elif(opc == 1):
            y = int(input("\nInsira o 1 número: "))
            z = int(input("\nInsira o 2 número: "))
            soma2num(y, z)
        elif(opc == 2):
            y = int(input("\nInsira o 1 número: "))
            z = int(input("\nInsira o 2 número: "))
            mult2num(y, z)
        elif(opc == 3):
            z = int(input("\nInsira o número para cálculo de raiz: "))
            raizNum(z)
        elif(opc == 4):
            y = int(input("\nInsira o 1 número para base: "))
            z = int(input("\nInsira o 2 número para expoente: "))
            pow2num(y, z)
        elif(opc == 5):
            z = int(input("\nInsira o número para cálculo de tabuada: "))
            tabu(z)
        elif(opc == 6):

            global vetor
            vetor = int(input("\nInsira o tamanho do vetor: ")) * [0]

            for z in range(0,len(vetor)):
                vetor[z] = random.randint(0,100)
            
            printVetor(vetor)

        elif(opc == 7):
            numMaior(vetor)

        elif(opc == 8):
            numMenor(vetor)

        else:
            print("\nFinalizando ...")
            break


menuPrincipal()
