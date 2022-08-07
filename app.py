from flask import Flask, render_template
from distutils.log import debug
from flask_sqlalchemy import SQLAlchemy
import sys

from sqlalchemy import Integer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://moshe:Billgates2.0@localhost:5432/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    
    def __repr__(self):
        return f'<Todo: {self.id} {self.description}>'
    
db.create_all()


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())


# always include this at the bottom of your code
if __name__ == '__main__':
    app.debug = True
    app.run(host="127.0.0.1", port=3000)
