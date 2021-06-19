from flask import Flask
# from flask.templating import render_template_string
# from flask.templating import render_template, render_template_string
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# app.debug = True
# app.config['SECRET_KEY'] = 'a really really really really long secret key 12345 '
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:test1234@localhost/flask_app_db'

db = SQLAlchemy()
# db = SQLAlchemy()
# db.init_app(app)

# db.create_all()
# db.session.commit()
 
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r %r %r>' %  (self.id , self.username, self.email)
    def __str__(self):
        return '<User %r %r %r>' %  (self.id , self.username, self.email)

