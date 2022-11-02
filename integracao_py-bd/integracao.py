import mysql.connector

#conectar no banco de dados

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="algoritmos"
)
if(banco):
    print("Conectado com sucesso")
else:
    print("Erro na conexão")
    
cursor = banco.cursor()
sql = "INSERT INTO disciplinas VALUES(%s,%s,%s,%s)"
valores1 = (None, "Algoritmos", 160, "Ayslan")
valores2 = (None, "Banco de Dados", 80, "Hélio")
valores3 = (None, "Matemática", 80, "Azuaite")

# nm_mat = input("Insira o nome da Matéria: ")
# ch = int(input("Insira a Carga Horário: "))
# nm_prof = input("Insira o nome do Professor: ")
# valores4 = (None, nm_mat, ch, nm_prof)


# cursor.execute(sql, valores1)
# cursor.execute(sql, valores2)
# cursor.execute(sql, valores3)
# cursor.execute(sql, valores4)

sql = "SELECT * FROM disciplinas ORDER BY id"

cursor.execute(sql)

resultados = cursor.fetchall()

for linha in resultados:
    print("Código: ", linha[0])
    print("Nome: ", linha[1])
    print("Carga Horária: ", linha[2])
    print("Professor: ", linha[3])
    print("--------------------------")

banco.commit()
cursor.close()
banco.close()