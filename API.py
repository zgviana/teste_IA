from flask import Flask

app = Flask(__name__)


'''@app.route('/hello_world', methods=['GET'])'''


@app.route('/')
def hello_world():
    return 'Olá mundo!'


if __name__ == '__main__':
    app.run(debug=True)
