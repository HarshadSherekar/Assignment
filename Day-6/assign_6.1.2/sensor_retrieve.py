import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data",
    use_pure = True
)

query = "select * from sensor";

cursor = connection.cursor()

cursor.execute(query)

sens = cursor.fetchall()

for i in sens:
    print(i)
    
cursor.close()
connection.close()