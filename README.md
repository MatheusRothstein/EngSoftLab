# EngSoftLab

## Criando o ambiente virtual 
>> python -m venv nome_do_ambiente_virtual

## Como acessar o ambiente virtual
>> nome_do_ambiente_virtual\Scripts\Activate

## Para desativar o ambiente virtual
>> deactivate

## Para utilizar os comandos do Flask
>> set FLASK_APP=main.py

## Para acessar o banco de dados com o shell da aplicação 
>> python -m flask shell

## Dentro do shell para criar o banco de dados
>> from app.model.database import db 
>> db.create_all()

## Para iniciar a aplicação
>> python -m flask run

