# linhas = int(input("Insira a quantidade de linhas: "))
# colunas = int(input("Insira a quantidade de colunas: "))

# matriz = [0] * linhas

# for i in range(0, linhas):
#     matriz[i] = matriz[i] * colunas

#def significa definir

#Exercicio

# def calcFatorial(x):
#     fat = 1
#     i = 2

#     if(x<0):
#         print("\nApenas número inteiro positivo!")
#     else:
#         while(i<=x):

#             fat = fat * i
#             i = i + 1

#         print(f"\nO resultado fatorial de {x} é {fat}")


# def principal():
#     x = int(input("\nInsira o número para resultado fatorial: "))
#     calcFatorial(x)

# principal()

# variável global e local

# def mostrarX():
#     #variável local
#     #só existe no procedimento
#     x=20
#     print(x)

# x=10
# print(x)
# mostrarX()
# print(x)

# def mostrarX():
#     #variável local declarada global
#     global x 
#     x = 20
#     print(x)


# x = 10
# print(x)
# mostrarX()
# print(x)

#return-----

# def calcFatorial(x):
#     fat = 1
#     i = 2

#     if(x<0):
#         print("\nApenas número inteiro positivo!")
#     else:
#         while(i<=x):

#             fat = fat * i
#             i = i + 1

#         return fat

# def principal():
#     ins = int(input("Insira o fatorial: "))
#     x = calcFatorial(5)
#     print(f"Resposta: {x}")

# principal()

# import random

# v = [0] * 10

# for i in range(0,10):
#     v[i]=random.randint(0,100)

# def numMenor(vet):
#     menor = vet[0]
#     for y in range(0,10):
#         if(vet[y]<menor):
#             menor=vet[y]
    
#     return menor

# x=numMenor(v)
# print(v)
# print(f"\nO menor número do vetor é: {x}")
