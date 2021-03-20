from app import db

ingredientes = db.Table('receita_ingrediente',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('ingrediente_id', db.Integer, db.ForeignKey('ingrediente.id')),
    db.Column('quantidade', db.String(80)),
    db.Column('receita_id', db.Integer, db.ForeignKey('receita.id'))
)


etapas = db.Table('receita_etapa',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('etapa_id', db.Integer, db.ForeignKey('etapa.id')),
    db.Column('receita_id', db.Integer, db.ForeignKey('receita.id'))
)



class Ingrediente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Ingrediente %r>' % self.nome

    @classmethod
    def list(cls):
        return cls.query.all()
    
    def create(self):
        db.session.add(self)
        db.session.commit()


class Etapa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(500), unique=True, nullable=False)
    numero = db.Column(db.Integer)

    def __repr__(self):
        return '<Receita %r>' % self.nome


class Receita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    ingredientes = db.relationship('Ingrediente', secondary=ingredientes, lazy='subquery',
        backref=db.backref('receitas', lazy=True))
    etapas = db.relationship('Etapa', secondary=etapas, lazy='subquery',
        backref=db.backref('receitas', lazy=True))

    def __repr__(self):
        return '<Receita %r>' % self.nome

    @classmethod
    def list_receitas(cls):
        return cls.query.all()