from flask import Flask

app = Flask(__name__)


'''@app.route('/hello_world', methods=['GET'])'''


@app.route('/')
def hello_world():
    return 'Olá todo mundo ok2!'


if __name__ == '__main__':
    app.run(debug=True)
