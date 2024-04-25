import mysql.connector


connection = mysql.connector.connect(
    user = 'root', 
    database = 'example', 
    password = 'Zariolicious534'
    )


cursor = connection.cursor()

'''
Use for printing table information now function print_all_accounts
testQuery = ('SELECT * FROM ex_table') 

cursor.execute(testQuery)
'''


def fetch_user(id):
    cursor.execute('SELECT * FROM ex_table WHERE id=%s''',(id,))
    return cursor.fetchall()

def update_amount(amount, id):
    cursor.execute('UPDATE ex_table SET amount=%s WHERE id=%s' % (amount, id))
    connection.commit()

def insert_new_account(name, amount, id, pinnumber):
    query = "INSERT INTO ex_table (name, amount, id, pinnumber) VALUES (%s, %s,%s,%s)"
    values = (name, amount, id, pinnumber)
    cursor.execute(query, values) 
    connection.commit()

def cleanup():
    cursor.close()
    connection.close()

def print_all_accounts():
    query = ('SELECT * FROM ex_table')

    cursor.execute(query)
    for item in cursor:
        print(item)

#def login(name, pinnumber):
   # cursor.execute('SELECT * FROM ex_table WHERE name=%s AND pinnumber=%s', (name, pinnumber))
   # return cursor.fetchall()

def cleanup():
    cursor.close()
    connection.close()

print(fetch_user(1)) #Checks user 1's details before update 
update_amount(500, 1)
print(fetch_user(1)) #Verify user 1's amount was updated

insert_new_account(4, 'someone else', 700, '7484') 

'''
Turned into function for use inside bank.py for simplicity
cursor.close()

connection.close()
'''