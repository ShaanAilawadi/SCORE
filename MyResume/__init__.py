from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
from MyResume import routes

if __name__ == '__main__':
    app.run(threaded=True)
