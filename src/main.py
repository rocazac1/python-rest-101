from flask import Flask, request
import  json
from models import Person

app = Flask(__name__)

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
        print(person)
        return (person.toJson())
    except (ValueError, KeyError, TypeError):
        return "Invalid Request", 400


if __name__  == '__main__':
    app.run(debug=True, host='0.0.0.0')
