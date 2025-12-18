import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "student",
    use_pure = True
)

roll = int(input("Enter Roll No. : "))
name = input("Enter Name : ")
email = input("Enter email : ")
course = input("Enter course name : ")

query = f"insert into students values({roll},'{name}','{email}','{course}')"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()
connection.close()
