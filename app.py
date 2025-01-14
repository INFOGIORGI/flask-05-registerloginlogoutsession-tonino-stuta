from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = '138.41.20.102'
app.config['MYSQL_PORT'] = 53306
app.config['MYSQL_USER'] = 'ospite'
app.config['MYSQL_PASSWORD'] = 'ospite'
app.config['MYSQL_DB'] = 'w3schools'


mysql=MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/registrati/", methods = ["GET", "POST"])
def signin():
    if request.method == 'GET':
        return render_template("signin.html")
    else:
        cursor = mysql.connection.cursor()
        query = """SELECT username FROM users WHERE username = %s"""
        nome = request.form.get("nome")
        cognome = request.form.get("cognome")
        username = request.form.get("username")
        password = request.form.get("password")
        confpassword = request.form.get("confpassword")

        if password == confpassword:
            cursor.execute(query, (username,))
            user = cursor.fetchall()
            if len(user)==0:
                insert = """INSERT INTO users VALUES(%s, %s, %s, %s)"""
                cursor.execute(insert, (username, password,nome,cognome))
                cursor.fetchall()
                mysql.connection.commit()
                return redirect ("/")
@app.route("/login")
def login():
    return render_template("login.html")



app.run(debug=True)
