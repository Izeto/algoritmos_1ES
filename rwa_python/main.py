import comple

def main():
    while(True):
        print("\n1. Mostrar Relatório")
        print("\n2. Inserir Número")
        print("\n3. Inserir número de usuário")
        print("\n4. Sair")
        
        opc = int(input("\nInsira a opção escolhida: "))
        
        if(opc>4 or opc<1):
            print("\nApenas entre 1 e 4!")
        elif(opc==1):
            comple.opc1()
            
        elif(opc == 2):
            comple.opc2()
            
        elif(opc == 3):
            comple.opc3()
            
        else:
            comple.opc4()
            break
main()