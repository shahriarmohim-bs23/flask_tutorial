from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is my First flask app<h1>'

@app.route('/home')
def home():
    return '<h1>This is my Home page<h1>'

if __name__=='__main__':
    app.run()
