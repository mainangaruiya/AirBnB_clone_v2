from flask import Flask
''''start web flask and display hello world'''
app = Flask(__name__)

@app.route('/airbnb-onepage/', methods=['GET'])
def hello_hbnb():
    return "Hello HBNB!"
