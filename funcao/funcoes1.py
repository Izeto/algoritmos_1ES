import random

def criarVetor(num1):
    vet =  [0] * num1
    for i in range(0,len(vet)):
        vet[i] = random.randint(1,200)
    return vet

def exibirVetor(v):
    for y in range(0,len(v)):
        print(v[y])

def somarImpares(v):
    impar = 0
    for y in range(0, len(v)):
        if(v[y]%2!=0):
            impar += v[y]
    return impar

def buscaVetor(num2,v):
    #ordenação seleção
    for i in range(0, len(v) - 1):
        i_menor = i
        for j in range(i+1, len(v)):
            if(v[j] < v[i_menor]):
                i_menor = j
        menor = v[i_menor]
        v[i_menor] = v[i]
        v[i] = menor

    #busca linear
    valor = num2
    i_valor = -1

    for i in range(0, len(v)):
        if(v[i] == valor):
            i_valor = i
            break

    if(i_valor >= 0):
        print("\nEncontramos o valor", valor, "no índice", i_valor)
    else:
        print("\nValor", valor, "não encontrado no vetor")

def ordenar(v, ordenacao):
    if(ordenacao==1):
        for i in range(0, len(v)-1):
            for j in range(0, len(v)-1):
                if(v[j] > v[j+1]):
                    temp = v[j]
                    v[j] = v[j+1]
                    v[j+1] = temp
        
    elif(ordenacao==2):
        for i in range(0, len(v)):
            chave = v[i]
            j = i-1
            while((j >= 0) and (v[j] > chave)):
                v[j+1] = v[j]
                j = j - 1
            v[j+1] = chave
        
    else:
        for i in range(0, len(v) - 1):
            i_menor = i
            for j in range(i+1, len(v)):
                if(v[j] < v[i_menor]):
                    i_menor = j
            menor = v[i_menor]
            v[i_menor] = v[i]
            v[i] = menor
    return v
