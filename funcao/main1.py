import funcoes1

def main():
    
    ins = int(input("\nInsira o tamanho do vetor: "))
    
    vet1 = funcoes1.criarVetor(ins)
    
    funcoes1.exibirVetor(vet1)
    
    imp = funcoes1.somarImpares(vet1)
    
    print(f"\nA soma de todos os números ímpares do vetor é: {imp}")
    
    informe = int(input("\nInsira um número para buscar no vetor: "))
    
    funcoes1.buscaVetor(informe, vet1)
    
    print("\n====== MENU PRINCIPAL ======")
    print("\n1. Ordenação Bolha")
    print("2. Ordenação Inserção")
    print("3. Ordenação Seleção")

    opc = input("\nInsira o tipo de ordenação que busca no seu vetor: ")

    ord = funcoes1.ordenar(vet1, opc)

    print(f"\nA opção selecionada foi {opc}")
    
    print(ord)

main()