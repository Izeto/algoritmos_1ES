import mysql.connector
#conectar no banco de dados

class Disciplina:
    def __init__(self):
        self.nm = ""
        self.ch = 0
        self.nm_prof = ""
        self.chr = 0.0

def salvar(materia):
    banco = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="algoritmos"
    )
    sql = "INSERT INTO disciplina VALUES(%s,%s,%s,%s,%s)"

    valores1 = (None, materia.nm, materia.ch, materia.nm_prof, materia.chr)

    cursor = banco.cursor()
    cursor.execute(sql, valores1)
    banco.commit()
    cursor.close()
    banco.close()

def lerDados():
    banco = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="algoritmos"
    )
    sql = "SELECT * FROM disciplinas ORDER BY id"
    
    cursor = banco.cursor()
    
    cursor.execute(sql)
    
    dados = cursor.fetchall()

    d = [Disciplina()] * cursor.rowcount
    
    i = 0
    
    for linha in dados:


    banco.commit()
    cursor.close()
    banco.close()

materia = Disciplina()
materia.nm = input("Insira o nome da Disciplina: ")
materia.ch = int(input("Insira a Carga Horária: "))
materia.nm_prof = input("Insira o nome do Professor: ")
materia.chr = round(((materia.ch*50)/60),2)

salvar(materia)

disciplinas = lerDados()

print("----------- Disciplinas Cadastradas -----------")

for i in range(0, len(x)):
    disc = x=[i]
    print("Código:", disc.codigo)
    print("Nome:", disc.nm)
    print("CH:", disc.ch)
    print("Professor:", disc.nm_prof)
    print("CHR:", disc.chr)





# for linha in resultados:
#     print("Código: ", linha[0])
#     print("Nome: ", linha[1])
#     print("Carga Horária: ", linha[2])
#     print("Professor: ", linha[3])
#     print("--------------------------")




# valores2 = (None, "Banco de Dados", 80, "Hélio")
# valores3 = (None, "Matemática", 80, "Azuaite")

# nm_mat = input("Insira o nome da Matéria: ")
# ch = int(input("Insira a Carga Horário: "))
# nm_prof = input("Insira o nome do Professor: ")
# chr = (ch*60)/50

# valores4 = (None, nm_mat, ch, nm_prof)


# ch = int(input("Insira a Carga Horário: "))
# chr = (ch*50)/60

# print(round(chr,2),"aulas")




























# cursor = banco.cursor()
# sql = "INSERT INTO disciplinas VALUES(%s,%s,%s,%s)"
# valores1 = (None, "Algoritmos", 160, "Ayslan")
# valores2 = (None, "Banco de Dados", 80, "Hélio")
# valores3 = (None, "Matemática", 80, "Azuaite")

# # nm_mat = input("Insira o nome da Matéria: ")
# # ch = int(input("Insira a Carga Horário: "))
# # nm_prof = input("Insira o nome do Professor: ")
# # valores4 = (None, nm_mat, ch, nm_prof)


# # cursor.execute(sql, valores1)
# # cursor.execute(sql, valores2)
# # cursor.execute(sql, valores3)
# # cursor.execute(sql, valores4)

# sql = "SELECT * FROM disciplinas ORDER BY id"

# cursor.execute(sql)

# resultados = cursor.fetchall()

# for linha in resultados:
#     print("Código: ", linha[0])
#     print("Nome: ", linha[1])
#     print("Carga Horária: ", linha[2])
#     print("Professor: ", linha[3])
#     print("--------------------------")

# banco.commit()
# cursor.close()
# banco.close()
