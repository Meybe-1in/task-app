from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.sqlite'

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)
    
#ROUTES
@app.route('/')
def home():
     return render_template('index.html')
 
@app.route('/create-task', methods=['POST'])
def create():
    new_task = Task(content=request.form['content'], done= False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('home'))

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.debug = True
    app.run()