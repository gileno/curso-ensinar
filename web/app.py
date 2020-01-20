import dataset
import joblib
import pandas as pd
import os
from geopy.geocoders import Nominatim

from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        dados = request.form.to_dict()
        modelo = joblib.load('mlp.joblib')
        # latitude,longitude,valor,iptu,condominio,area,quartos,banheiros,suites,vaga
        geocoder = Nominatim()
        localizacao = geocoder.geocode(dados['endereco'])
        dados = pd.DataFrame(
            [[localizacao.latitude, localizacao.longitude, dados['iptu'], dados['condominio'],
            dados['area'], dados['quartos'], dados['banheiros'], dados['suites'], dados['vagas']]]
        )
        previsao = round(modelo.predict(dados)[0], 2)
    else:
        previsao = None
    return render_template('inicio.html', previsao=previsao)


@app.route('/novo-contato/', methods=['GET', 'POST'])
def novo_contato():
    banco = dataset.connect('sqlite:///db.sqlite3')
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        banco['contatos'].insert({
            'nome': nome,
            'email': email,
            'telefone': telefone
        })
        # banco['contatos'].insert(request.form.to_dict())
        return redirect('/')
    return render_template('novo_contato.html')


@app.route('/editar-contato/<id>/', methods=['GET', 'POST'])
def editar_contato(id):
    banco = dataset.connect('sqlite:///db.sqlite3')
    contato = banco['contatos'].find_one(id=id)
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        banco['contatos'].update({
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'id': id,
        }, ['id'])
        return redirect('/')
    return render_template('editar_contato.html', contato=contato)


app.run(debug=True, host='0.0.0.0')
