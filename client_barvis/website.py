import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the homepage"

@app.route('/req')
def req():
    jsonResponse = requests.get("http://localhost:8080/api/listElements").json()
    print(jsonResponse["_embedded"]["listElements"][0]["name"])

    return "succesfull get"

def run():
    app.run(debug=False)
