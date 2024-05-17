from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '37978bd904a2c01f1a68a9d6e8237259'

app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://anonyme:admin@localhost/projetTI'

db = SQLAlchemy(app)

