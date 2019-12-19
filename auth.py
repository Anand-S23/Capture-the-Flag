import bcrypt 
from getpass import getpass
import sqlite3
from sqlite3 import Error
 
def sql_connection():
    try:
        con = sqlite3.connect(':memory:')
        print('Database created')
 
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE users(username text, password text)")
    con.commit()


con = sql_connection()
sql_table(con)
 

def create_user():
    username = input('Username: ')
    pass1 = getpass()
    pass2 = getpass()

    cur = g.db.cursor()
    cur.execute("""SELECT username FROM users WHERE username=?""", (username))

    result = cur.fetchone()

    if result:
        print('User already exits. ')
    

    else:
        if pass1 == pass2:
            password = pass1.encode('utf-8')
            hpass = bcrypt.hashpw(password, bcrypt.gensalt())

            cur.execute("INSERT INTO users VALUES (?, ?)", (username, hpass))
            g.db.commit()

        else: 
            print('Passwords did not match. ')
    

def authenticate():
    username = input('Username: ')
    password = getpass()

    found = False

    # Get passowrd here
        
    if found: 
        npass = password.encode('utf-8')
        if bcrypt.checkpw(npass, all_users[location]['password']):
            print('You have logged on.')
        else:
            print('Passwords don\'t match.')
    else:
        print('User not found.')