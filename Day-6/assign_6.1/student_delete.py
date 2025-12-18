import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "student",
    use_pure = True
)

name = input("Enter name whose record is to be deleted : ")

query = f"delete from students where name = '{name}';"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()
connection.close()
