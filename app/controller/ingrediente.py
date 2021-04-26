from app import app
from app.model.database import Ingrediente, Receita, ingredientes
from flask import render_template, request, redirect, url_for


@app.route('/')
@app.route('/home')
def home():
    return render_template('home/home.html', home='home')

@app.route('/ingredientes/', methods=['GET'])
def ingrediente_list():
    ingredientes = Ingrediente.list()
    return render_template('ingrediente/list.html', ingredientes=ingredientes)

@app.route('/ingredientes/create/', methods=['GET', 'POST'])
def ingrediente_create():
    if request.method == 'POST':
        ingrediente = Ingrediente(nome=request.form['nome'])
        ingrediente.create()
        return redirect(url_for('ingrediente_list'))
    ingredientes = Ingrediente.list()
    return render_template('ingrediente/create.html', ingredientes=ingredientes)

@app.route('/receitas', methods=['GET'])
def receitas_list():
    receitas = Receita.list_receitas()
    return render_template('receita/receita.html', receitas=receitas)

@app.route('/receitas/<receitaID>', methods=['GET'])
def receita_etapas(receitaID):
    receita = Receita.query.filter_by(id=receitaID).first()
    ingredientes = receita.ingredientes
    etapas = receita.etapas
    return render_template('receita/etapas.html', receita=receita)

@app.route('/receitas/create', methods=['GET', 'POST'])
def receita_create():
    ingredientes = Ingrediente.list()
    return render_template('receita/criarReceita.html', ingredientes=ingredientes)

