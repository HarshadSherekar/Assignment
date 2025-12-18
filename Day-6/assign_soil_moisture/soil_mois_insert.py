import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agri_iot",
    use_pure = True
)

id = int(input("Enter ID : "))
mois = float(input("Enter moisture level : "))
date = input("Enter date&time : ")

query = f"insert into soil_moisture values({id},{mois},'{date}')"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()
connection.close()
