import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agri_iot",
    use_pure = True
)

id = int(input("Enter id whose record is to be deleted : "))

query = f"delete from soil_moisture where id = {id};"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()
connection.close()
