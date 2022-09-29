import math
import random

def numInteiro():
    insInt = int(input("\nInsira um número inteiro: "))

    return insInt

def numRand():
    genNumRand = random.randint(1,numInteiro())

    return genNumRand

def numMes():
    vetMes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    vetNumMes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    insNumMes = int(input("\nInsira um número inteiro: "))

    if(insNumMes>12 or insNumMes<1):
        while(insNumMes>12 or insNumMes<1):
            print("\nApenas entre 1 e 12!")
            insNumMes = int(input("\nInsira um número inteiro: "))
    for i in range(0,len(vetMes)):
        if(insNumMes==i+1):
            #print(f"O número {insNumMes} é o mês de {vetMes[i]}")
            retMes = vetMes[i]

            return retMes
    
    # ou 
    
    # elif(insNumMes==1):
        # retMes = vetMes[i]
        # return retMes
    # elif(insNumMes==2):
        # retMes = vetMes[i]
        # return retMes
    # elif(insNumMes==3):
        # retMes = vetMes[i]
        # return retMes
    # elif(insNumMes==4):
        # retMes = vetMes[i]
        # return retMes
    # elif(insNumMes==5):
        # retMes = vetMes[i]
        # return retMes
    # elif(insNumMes==6):
        # retMes = vetMes[i]
        # return retMes
    # elif(insNumMes==7):
        # retMes = vetMes[i]
        # return retMes
    # elif(insNumMes==8):
        # retMes = vetMes[i]
        # return retMes
    # elif(insNumMes==9):
        # retMes = vetMes[i]
        # return retMes
    # elif(insNumMes==10):
        # retMes = vetMes[i]
        # return retMes
    # elif(insNumMes==11):
        # retMes = vetMes[i]
        # return retMes
    # else:
        # retMes = vetMes[i]
        # return retMes

def menuPrinc():
    x = False
    while(x==False):
        print("\n====== Menu Principal ======")
        print("\n1. Área do Quadrado")
        print("\n2. Área do Retângulo")
        print("\n3. Área do Triângulo")
        print("\n4. Área do Trapézio")
        print("\n5. Volume do Cubo")
        print("\n6. Cálculo de Fatorial")
        print("\n7. Sair")

        try:
            opc = int(input("\nInsira a opção escolhida: "))

        except:
            print("\nHouve um problema!")

            continue

        
        if(opc > 7 or opc < 1):
            print("\nApenas entre 1 e 7!")
        elif(opc == 1):
            l = int(input("\nInsira o valor de um lado do quadrado: "))
            opc1 = areaQuad(l)
            return opc1

        elif(opc == 2):
            b = int(input("\nInsira o valor da base do retângulo: "))
            h = int(input("\nInsira o valor da altura do retângulo: "))
            opc2 = areaRetan(b,h)
            return opc2

        elif(opc == 3):
            b = int(input("\nInsira o valor da base do triângulo: "))
            h = int(input("\nInsira o valor da altura do triângulo: "))
            opc3 = areaTrian(b,h)
            return opc3

        elif(opc == 4):
            bm = int(input("\nInsira o valor da base menor do trapézio: "))
            bM = int(input("\nInsira o valor da base maior do trapézio: "))
            h = int(input("\nInsira o valor da altura do retângulo: ")) 
            opc4 = areaTrapezio(bm,bM,h)
            return opc4
            
        elif(opc == 5):
            b = int(input("\nInsira o valor da base do cubo: "))
            h = int(input("\nInsira o valor da altura do cubo: "))
            p = int(input("\nInsira o valor da profundidade do cubo: "))
            opc5 = volCubo(b,h,p)
            return opc5

        elif(opc == 6):
            x = int(input("\nInsira o valor para cálculo de fatorial: "))
            opc6 = calcFatorial(x)
            return opc6

        else:
            y = "\nFinalizando ..."
            return y
            
def areaQuad(l):
    resAreaQuad = l * 2
    result = (f"\nDada as medidas, a àrea do quadrado é: {resAreaQuad}m²")

    return result

def areaRetan(b,h):

    resAreaRetan = b * h
    result = (f"\nDada as medidas, a àrea do retângulo é: {resAreaRetan}m²")

    return result

def areaTrian(b,h):

    resAreaTrian = (b * h)/2
    result = (f"\nDada as medidas, a àrea do triângulo é: {resAreaTrian}m²")

    return result

def areaTrapezio(bm,bM,h):

    resAreaTra = ((bm+bM)*h)/2
    result = (f"\nDada as medidas, a àrea do trapézio é: {resAreaTra}m²")

    return result

def volCubo(b,h,p):
    
    resVolCubo = b * h * p
    result = (f"\nDada as medidas, o volume do cubo é: {resVolCubo}m³")

    return result

def calcFatorial(x):
    
    fat = math.factorial(x)

    result = (f"\nO resultado fatorial de {x} é {fat}")

    return result

    #ou
    
    # fat = 1
    # i = 2
    # f = False
    
    # while(f==False):
    #     if(x<0):
    #         print("\nApenas número inteiro positivo!")
    #         while(x<0):
    #             x = int(input("\nInsira o valor para cálculo de fatorial: "))
    #     else:
    #         while(i<=x):
                
    #             fat = fat * i
    #             i = i + 1
            
    #     result = (f"\nO resultado fatorial de {x} é {fat}")

    #     return result