from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

# The app runs only if scripot is ran directly
if __name__ == '__main__':
    app.run(debug=True)
