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
