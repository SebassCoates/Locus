from flask import Flask, request
import os.path
from time import gmtime, strftime
from recommender import *
from collections import OrderedDict

app = Flask("DynamicLocus")

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'content.html')

@app.route('/', methods=["GET"])
def home():                                             #render home page
    return open('./home.html', 'r').read()

@app.route('/', methods=['POST', 'GET'])
def content():                                          #handle post request and render content page
    features = generateFeatureList(request.form)
    date = features[3]
    suggestionList = predict10(features)                #modifies features by reference
    exploreList = explore10(date)

    suggestionList = list(OrderedDict.fromkeys(suggestionList))     #remove duplicate suggestions
    exploreList = list(OrderedDict.fromkeys(exploreList))

    suggested = ''                                      #Start: document manipulation
    explore = ''
    for i in range(len(suggestionList)):
        suggested += '<a onClick="window.location.reload()" id="sug">'
        suggested += suggestionList[i]
        suggested += '</a>'
        suggested += '<br><br>'
    for i in range(len(exploreList)):
        explore += '<a onClick="window.location.reload()" id="sug">'
        explore += exploreList[i]
        explore += '</a>'
        explore += '<br><br>'
    content = open('./content.html', 'r').read()
    content = content.replace('ReplaceTextNodeWithSuggested', suggested)
    content = content.replace('ReplaceTextNodeWithExplore', explore)    #End: document manipulation

    return content

def generateFeatureList(postData):                      #formatted list of features from post data
    userID = postData.get('userID')
    isInternal = 1
    if postData.get('internal') != 'internal':
        isInternal = 0
    region = postData.get('region')
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    return [userID, isInternal, region, time]