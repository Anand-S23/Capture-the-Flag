import sqlite3
import bcrypt

db = sqlite3.connect('auth.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE users (username TEXT PRIMARY KEY, password TEXT)')
db.commit()

def create_user(username, password, password_conf):
  cursor.execute("""SELECT username FROM users WHERE username=?""", (username))
  exisiting_user = cursor.fetchone()

  if exisiting_user: 
    print('User already exisits, login or choose another username.')

  else:
    if password == password_conf: 
      encoded = password.encode('utf-8')
      final_password = bcrypt.hashpw(password, bcrypt.gensalt())

      cursor.execute("INSERT INTO users VALUES (?, ?)", (username, hpass))
      db.commit()

    else: 
      print('Passwords did not match. ')

def authenticate_user(username, password):
  cursor.execute("""SELECT username, password FROM users WHERE username=?""", (username))
  user = cursor.fetchone()

  if user: 
    encoded_pass = user[1].encode('utf-8')
    if bcrypt.checkpw(encoded_pass, password):
      print('You have logged on.')
    else:
      print('Passwords don\'t match.')
  else:
    print('User not found.')


  



