from . import app,db

from flask_sqlalchemy import SQLAlchemy

class equipement(db.Model):
    id_equipement = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=True)
    descriptione = db.Column(db.String(100), nullable=False)
    tarife = db.Column(db.Float(10), nullable=False)
    image = db.Column(db.String(100), nullable=False, default='default.jpg')
    stock = db.Column(db.Integer, nullable=False)
    id_categorie = db.Column(db.Integer, db.ForeignKey('categorie.id_categorie'), nullable=False)

    def __repr__(self):
        return f"equipement('{self.id_equipement}', '{self.nome}', '{self.descriptione}', '{self.tarife}', '{self.image}', '{self.stock}', '{self.id_categorie}')"

class categorie(db.Model):
    id_categ = db.Column(db.Integer, primary_key=True)
    nom_categ = db.Column(db.String(100), nullable=False)
    equipements = db.relationship('equipement', backref='categorie', lazy=True)