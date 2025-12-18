import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agri_iot",
    use_pure = True
)

query = "select * from soil_moisture";

cursor = connection.cursor()

cursor.execute(query)

record = cursor.fetchall()

for i in record:
    print(i)
    
cursor.close()
connection.close()