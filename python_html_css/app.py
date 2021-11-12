import sqlite3
from flask import Flask, g

DATABASE = "blog.db"
SECRET_KEY = "enois"

app = Flask(__name__)
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(DATABASE)

@app.before_request
def pre_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def pos_requisicao(exception):
    g.bd.close_bd()

@app.route('/')
def exibir_entrada():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto in cur.techall():
        entradas.append({'titulo': titulo, 'texto': texto})
    return str(entradas)
