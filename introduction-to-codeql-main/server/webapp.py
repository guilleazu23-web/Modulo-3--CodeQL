import os
import sqlite3

from flask import Flask


ROOT = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
TEMPLATES = os.path.join(ROOT, 'templates')

flaskapp = Flask("BookStore", template_folder=TEMPLATES)
flaskapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database_uri = os.environ.get('SQLITE_URI', ':memory:')

database = sqlite3.connect(database_uri, check_same_thread=False)
cursor = database.cursor()
# CÓDIGO INSEGURO PARA PROBAR CODEQL
import sqlite3

def buscar_usuario(username):
    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    # Esta línea es peligrosa porque concatena la entrada del usuario directamente
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()
buscar_usuario("admin")