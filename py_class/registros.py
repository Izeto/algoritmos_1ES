# class Data:
#     def __init__(self):
#         self.dia = 0
#         self.mes = 0
#         self.ano = 0

# class Professor:
#     def __init__(self):
#         self.nome = ""
#         self.idade = 0
#         self.salario = 0.0
#         self.dataNascimento = Data()
        
# p1 = Professor()
# p1.nome = "Ayslan T. Possebom"
# p1.idade = 41
# p1.salario = 1100.90
# p1.salario += p1.salario*1.25
# p1.dataNascimento.dia = 19
# p1.dataNascimento.mes = "Dezembro"
# p1.dataNascimento.ano = 1980

# def exibirProfessor(professor):
#     print(f"Nome do Professor: {professor.nome}")
#     print(f"Idade do Professor: {professor.idade}")
#     print(f"Salário do Professor: {professor.salario}")
    
# p2 = Professor()
# p2.nome = "Rafael Zotesso"
# p2.idade = 34
# p2.salario = 20000.00
# p2.dataNascimento.dia = 20
# p2.dataNascimento.mes = "Fevereiro"
# p2.dataNascimento.ano = 1988

# exibirProfessor(p1)

# --------------------------------------------------------

# class Aluno:
#     def __init__(self):
#         self.nome = ""
#         self.idade = 0
#         self.email = [""]*10
#         self.sexo = False  # False: feminino / True: masculino
#         self.dataNascimento = Data()

# a1 = Aluno()
# a1.nome = "José Antônio"
# a1.idade = 18
# a1.email[0] = "joseantonio@gmail.com"
# a1.sexo = True
# a1.dataNascimento.dia = 22
# a1.dataNascimento.mes = 5
# a1.dataNascimento.ano = 2004

# a2 = Aluno()
# a2.nome = "Maria das Dores"
# a2.idade = 17
# a2.email = "mariadasdores@gmail.com"
# a2.sexo = False
# a2.dataNascimento.dia = 16
# a2.dataNascimento.mes = 9
# a2.dataNascimento.ano = 2005

# print("Nome do 1 aluno: ", a1.nome)
# print("Nome do 2 aluno: ", a2.nome)

# data1 = Data()
# data1.dia = int(input("Insira o dia: "))
# data1.mes = int(input("Insira o mês: "))
# data1.ano = int(input("Insira o ano: "))
