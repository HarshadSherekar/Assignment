import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "student",
    use_pure = True
)

query = "select * from students";

cursor = connection.cursor()

cursor.execute(query)

students = cursor.fetchall()

for student in students:
    print(student)
    
cursor.close()
connection.close()