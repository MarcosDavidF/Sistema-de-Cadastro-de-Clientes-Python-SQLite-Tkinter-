# backend.py
import sqlite3
from typing import List, Tuple, Optional

DATABASE = 'clientes.db'

def _connect():
    """Abre conexão e retorna (conn, cur)."""
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    return conn, cur

def initDB():
    conn, cur = _connect()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            sobrenome TEXT,
            email TEXT,
            cpf TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert(nome: str, sobrenome: str, email: str, cpf: str) -> None:
    conn, cur = _connect()
    cur.execute('INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES (?,?,?,?)',
                (nome, sobrenome, email, cpf))
    conn.commit()
    conn.close()

def view() -> List[Tuple]:
    conn, cur = _connect()
    cur.execute('SELECT * FROM clientes')
    rows = cur.fetchall()
    conn.close()
    return rows

def search(nome: str = '', sobrenome: str = '', email: str = '', cpf: str = '') -> List[Tuple]:
    conn, cur = _connect()
    cur.execute(
        'SELECT * FROM clientes WHERE nome=? OR sobrenome=? OR email=? OR cpf=?',
        (nome, sobrenome, email, cpf)
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id_: int) -> None:
    conn, cur = _connect()
    cur.execute('DELETE FROM clientes WHERE id = ?', (id_,))
    conn.commit()
    conn.close()

def update(id_: int, nome: str, sobrenome: str, email: str, cpf: str) -> None:
    conn, cur = _connect()
    cur.execute(
        'UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?',
        (nome, sobrenome, email, cpf, id_)
    )
    conn.commit()
    conn.close()

# inicializa DB ao importar o módulo (seguro)
initDB()
