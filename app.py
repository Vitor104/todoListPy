from flask import Flask, render_template, request

import mysql.connector

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'  
app.config['MYSQL_PASSWORD'] = '12345'  
app.config['MYSQL_DATABASE'] = 'todolist'  
app.config['MYSQL_HOST'] = 'localhost'


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/adicionar")
def adicionar():
    return render_template("adicionar.html")


if __name__ == "__main__":
    app.run(debug=True)