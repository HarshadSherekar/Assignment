import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data",
    use_pure = True
)

id = int(input("Enter ID : "))
temp = float(input("Enter temperature : "))
humid = float(input("Enter humidity : "))
timestamp = input("Enter date/time(timestamp) : ")

query = f"insert into sensor values({id},{temp},{humid},'{timestamp}')"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()
connection.close()
