from flask import Flask, render_template
from distutils.log import debug
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://moshe:Billgates2.0@localhost:5432/test'
db = SQLAlchemy(app)






#always include this at the bottom of your code
if __name__ == '__main__':
    app.debug = True
    app.run(host="127.0.0.1", port=3000)