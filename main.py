from flask import Flask, request

app = Flask(__name__)

@app.route("/hello")
def hello():
    name = request.args.get('name')
    if name:
        return("Hello " + name.capitalize())
    else:
        return("Hello World")

if __name__  == '__main__':
    app.run(debug=True,host='0.0.0.0')