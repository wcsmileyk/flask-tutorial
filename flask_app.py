from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'This is a web page!'


if __name__ == '__main__':
    app.run(debug=True)
