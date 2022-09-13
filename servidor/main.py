from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hola, ingenieros de software del mundo.'

if __name__ ==  '__main__':
    app.run()
