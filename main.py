import mysql.connector

 

connection = mysql.connector.connect(user = 'root', database = 'example', password = 'Zariolicious534')

 

cursor = connection.cursor()

 

addData = ("INSERT INTO ex_table (id, name, amount) VALUES (3,'Zener',5)")
 

cursor.execute(addData)

 

connection.commit()

cursor.close()

connection.close()
