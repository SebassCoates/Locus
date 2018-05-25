from flask import Flask, request
import os.path
from time import gmtime, strftime
from recommender import *

app = Flask("DynamicLocus")

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'content.html')

@app.route('/', methods=["GET"])
def home():
    return open('./home.html', 'r').read()

@app.route('/', methods=['POST', 'GET'])
def content():
    postData = request.form
    userID = postData.get('userID')
    isInternal = 1
    if postData.get('internal') != 'internal':
        isInternal = 0
    region = postData.get('region')
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    features = [userID, isInternal, region, time]

    suggestions = predict10(features)

    



