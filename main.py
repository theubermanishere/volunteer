from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola peeps!'

# @app.route

if __name__ == '__main__':
    app.run(debug=True)

