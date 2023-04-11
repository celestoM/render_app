#pip install flask     /para instala flask
#entrar en la pagina https://flask.palletsprojects.com/en/2.2.x/quickstart/ y copiar el codigo

from flask import Flask, render_template # se agrega render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")  # para que ubique el archivo html, hay q moverlo a la carpeta llamada / templates

# en la consola escribrir flask run

# para correr en rende.com
# en terminal: pip install gunicorn
