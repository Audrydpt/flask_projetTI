from app import app, models
from flask import render_template, url_for

@app.route("/")
def accueil():
    return render_template('accueil.html')

@app.route("/tous_produits")
def produits():
    equipements = models.equipement.query.all()
    return render_template('tous_produits.html', equip=equipements)

@app.route("/categories")
def categories():
    toutes_categories = models.categorie.query.all()
    return render_template('categories.html', categories=toutes_categories)

@app.route("/categorie/<int:id_categ>")
def produits_par_categorie(id_categ):
    produits = models.equipement.query.filter_by(id_categorie=id_categ).all()
    nom_categ = models.categorie.query.get(id_categ).nom_categ
    return render_template('produits_categorie.html', produits=produits, nom_categ=nom_categ)
