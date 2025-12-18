import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "student",
    use_pure = True
)

name = input("Enter name whose mail is to be updated : ")
email = input("Enter new email : ")

query = f"update students set email = '{email}' where name = '{name}' "

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()
connection.close()
