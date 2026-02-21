from flask import Flask, render_template
import json

import sqlite3
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "super_secret_key"
app = Flask(__name__)

ARQUIVO = "musicas.json"

def carregar_musicas():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

@app.route("/")
def home():
    musicas = carregar_musicas()
    return render_template("home.html", musicas=musicas)

@app.route("/entrar")
def entrar():
    return render_template("entrar.html")

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar.html")

@app.route("/musicas")
def musicas():
    return render_template("musicas.html")

@app.route("/listas")
def listas():
    return render_template("listas.html")

@app.route("/artistas")
def artistas():
    return render_template("artistas.html")

@app.route("/diario")
def diario():
    return render_template("diario.html")

def criar_banco():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

criar_banco()
if __name__ == "__main__":
    app.run(debug=True)
@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        senha = generate_password_hash(request.form["senha"])

        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO usuarios (username, email, senha) VALUES (?, ?, ?)",
                           (username, email, senha))
            conn.commit()
        except:
            return "Usuário ou email já existe"

        conn.close()
        return redirect("/entrar")

    return render_template("cadastrar.html")

@app.route("/entrar", methods=["GET", "POST"])
def entrar():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        usuario = cursor.fetchone()

        conn.close()

        if usuario and check_password_hash(usuario[3], senha):
            session["usuario_id"] = usuario[0]
            session["username"] = usuario[1]
            return redirect("/")

        return "Login inválido"

    return render_template("entrar.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")