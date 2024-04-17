import mysql.connector


connection = mysql.connector.connect(
    user = 'root', 
    database = 'example', 
    password = 'Zariolicious534'
    )


cursor = connection.cursor()

testQuery = ('SELECT * FROM ex_table') 

cursor.execute(testQuery)

for item in cursor:
    print(item)
 

cursor.close()

connection.close()
