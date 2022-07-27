from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is my First flask app<h1>'
    
@app.route('/home')
def home():
    return redirect(url_for(index))

@app.route('/User/<name>/age/<age>')
def user(name,age):
    return f"Hello I am {name}, I am {age} years old"

if __name__=='__main__':
    app.run()