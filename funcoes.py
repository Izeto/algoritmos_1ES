#1 Importações

#2 Criar sub-algoritmos

#3 Criar o algoritmo main(principal)

# import random
# import math

# def soma3num():
#     num1 = int(input("\nInsira o 1 número: "))
#     num2 = int(input("\nInsira o 2 número: "))
#     num3 = int(input("\nInsira o 3 número: "))
#     somaResul = num1+num2+num3
#     print(f"\nO resultado da soma dos 3 números é: {somaResul}")

# def raizNum():
#     raizInp = int(input("\nInsira um número para cálculo de raiz: "))
#     raizCalc = round(math.sqrt(raizInp),2)
#     print(f"\nA raiz quadrada de {raizInp} é {raizCalc}")

# def sortNum():
#     sortNums = random.randint(1,100)
#     print(f"\nO número sorteado é {sortNums}")

# def mostraMenu():
#     print("\n========== MENU DE OPÇÕES ==========")
#     print("\n1. Somar 3 números")
#     print("2. Mostrar raiz de um número")
#     print("3. Sortear um número de 1 a 100")
#     print("4. Sair")


# teste = False

# while(teste!=True):
#     mostraMenu()
#     opcao = int(input("\nInsira uma opção: "))
#     if(opcao==1):
#         soma3num()
#     elif(opcao==2):
#         raizNum()
#     elif(opcao==3):
#         sortNum()
#     else:
#         print("\nFinalizando ...")
#         teste = True

# ------ Exercícios Apostila -------

# 1. O que é um procedimento?
# 2. Qual é a sintaxe para se criar um procedimento?
# 3. Seja acao() um procedimento. Durante o algoritmo, como chamar este procedimento para que seu código seja executado?
# 4. O que são parâmetros? Para que eles servem?
# 5. Seja acao(a, b, c) um procedimento que recebe três números inteiros como parâmetro.
#   - Como chamar este procedimento para que seu código seja executado?

# 1. R: São sub-algoritmos, bibliotecas pessoais, rotina, módulo que pode ser chamado de um arquivo para o outro,
# seja de forma abrangente ou específica. Se for o caso de chamar funções em outras pastas dentro de uma única, realizar import de diretório.

# 2. R: a sintaxe utilizada é:

#   def subAlg():

# 3. R: para chamar a função, basta: 
   
#   ubAlg()

# 4. R: são valores em específico inseridos por obrigatoriedade entre os parênteses de algum procedimento.
# por exemplo:

#   x = math.pow(2,3)
#   print(x)

#       ou

#   def somar(n1,n2):
#       s = n1+n2
#       print(s)
#   somar(10,10)

# *irá aparecer na tela a soma/pow dos valores inseridos na chamada da função, cuja não possui valores definidos,
#  portanto são dinâmicas, pois a soma/pow vai ser definida a partir do que colocarmos entre parênteses, tendo 2 valores obrigatórios.

 
# 5. R:  acao(10,5,8)

# Exercício

# def coisa(n1, n2, n3):
#     if(n1>=n2 and n1>=n3):
#         maior=n1
#         print(f"O maior é {maior}")
#     elif(n2>=n1 and n2>=n3):
#         maior=n2
#         print(f"O maior é {maior}")
#     else:
#         maior=n3
#         print(f"O maior é {maior}")


# n1 = int(input("Insira o 1 número: "))
# n2 = int(input("Insira o 2 número: "))
# n3 = int(input("Insira o 3 número: "))

# coisa(n1, n2, n3)