import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the homepage"

@app.route('/testReq')
def testReq():
    bla = requests.get("https://httpbin.org/get")
    print(bla.url)
    return "succesfull get"

if __name__ == "__main__":
    app.run(debug=True)