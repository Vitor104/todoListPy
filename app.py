from flask import Flask, render_template, request, url_for, redirect

import mysql.connector

app = Flask(__name__)
from operacoesbd import *

db_config = {
    "user": "root",
    "password": "12345",
    "host": "localhost",
    "database": "Users"
}


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=['GET', 'POST']) 
def login():
    if request.method == "POST":
        name = request.form['name']
        senha = request.form['senha']

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

            # Search for the user
        query = "SELECT * FROM Users WHERE name = %s AND senha = %s"
        cursor.execute(query, (name, senha))
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:
            return redirect(url_for("adicionar", name = name))
        else:
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/adicionar")
def adicionar():
    name = request.args.get("name")
    return render_template("adicionar.html")




if __name__ == "__main__":
    app.run(debug=True)




#app.config['MYSQL_USER'] = 'root'  
#app.config['MYSQL_PASSWORD'] = '12345'  
#app.config['MYSQL_DATABASE'] = 'todolist'  
#app.config['MYSQL_HOST'] = 'localhost'