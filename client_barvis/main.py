import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the homepage"

@app.route('/testReq')
def testReq():
    jsonResponse = requests.get("http://localhost:8080/api/listElements").json()
    print(jsonResponse["_embedded"]["listElements"][0]["name"])

    return "succesfull get"

if __name__ == "__main__":
    app.run(debug=True)