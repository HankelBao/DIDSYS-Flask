from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
