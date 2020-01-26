from flask import Flask, request
from waitress import serve
from paste.translogger import TransLogger
import logging
import os

from models import Person


app = Flask(__name__)
logger = logging.getLogger('waitress')
logging.basicConfig(level=logging.DEBUG, filemode="w", filename=os.getenv('LOG_DIR', '.') + "/app.log")


@app.route("/health", methods=['GET'])
def health():
    return ("OK")


@app.route("/hello", methods=['GET'])
def hello():
    name = request.args.get('name')
    if name:
        return ("Hello " + name.capitalize())
    else:
        return ("Hello World")


@app.route("/todos", methods=['POST'])
def createToDos():
    try:
        jsonObject = request.get_json()
        name, age = jsonObject["name"], jsonObject["age"]
        person = Person(name, age)
        logger.info(person)
        return (person.toJson())
    except (ValueError, KeyError, TypeError):
      return "Invalid Request", 400


if __name__  == '__main__':
    serve(TransLogger(app, setup_console_handler = True), host='0.0.0.0', port=5000)
