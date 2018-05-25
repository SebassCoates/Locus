from flask import Flask, request
import os.path
app = Flask("DynamicLocus")

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'content.html')

@app.route('/', methods=["GET"])
def home():
    return open('./home.html', 'r').read()

@app.route('/', methods=['POST', 'GET'])
def content():

    postData = request.form
    print(postData.get('userID'))