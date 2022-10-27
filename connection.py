import sqlite3

def connection():
    connection = sqlite3.connect('codewithcanon.db')
    
    create_table = '''CREATE TABLE IF NOT EXISTS users(firstname TEXT, contact INT, username TEXT)'''
    connection.execute(create_table)
    
    firstname = 'John Doe'
    contact = 76543322
    username = 'john'
    
    insert_data = '''INSERT INTO users(firstname, contact, username) VALUES(?,?,?)'''
    data_tuple = (firstname, contact, username)
    cursor = connection.cursor()
    process = cursor.execute(insert_data, data_tuple)
    connection.commit()
    
    if(process) :
        print('Data Inserted Successfully')
    else :
        print('Data processing Failed')
    
    
    connection.close()
    
connection()