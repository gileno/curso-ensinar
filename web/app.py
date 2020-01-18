import dataset

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def inicio():
    banco = dataset.connect('sqlite:///db.sqlite3')
    contatos = banco['contatos'].find()
    titulo = 'Curso Python'
    return render_template('inicio.html', titulo=titulo, contatos=contatos)


app.run(debug=True)
