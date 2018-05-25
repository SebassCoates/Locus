import pickle
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import datetime
import random as rand

buckets = [b.split() for b in open('buckets.txt', 'r').read().split('\n')][0:3]

regionDict = {}
regionText = open("regions.txt", 'r').read().split('\n')
regionText.remove('')
for pair in regionText:
        try:
                name, index = pair.split(',')
                regionDict[name] = index
        except:
                print(pair)
maxRegion = max(np.array(list(regionDict.values()), dtype='int32'))

idDict = {}
idText = open("ids.txt", 'r').read().split('\n')
idText.remove('')
for pair in idText:
        name, index = pair.split(',')
        idDict[name] = index
maxID = max(np.array(list(idDict.values()), dtype = 'int32'))

pathDict = {}
pathText = open("paths.txt", 'r').read().split('\n')
pathText.remove('')
for pair in pathText:
        name, index = pair.split(',')
        pathDict[index] = name


classifier = pickle.load(open('page_predictor', 'rb'))

#date format: mm/dd/yyyy HH:MM:SS (A/P)M
def date_to_int(datestring):
        elements = datestring.split(' ')
        time = elements[1]
        hour = int(time.split(':')[0])
        if hour < 10:
                return 0
        if hour > 15: 
                return 2
        return 1

def fiscal_quarter(datestring):
        month = int(datestring.split(' ')[0].split('-')[1])
        if month < 3:
                return 0
        if month > 3 and month < 6:
                return 1
        if month > 6 and month < 9:
                return 2
        return 3

def day_of_week(datestring):
        ymd = datestring.split(' ')[0].split('-')
        date = datetime.date(int(ymd[0]), int(ymd[1]), int(ymd[2]))
        return date.weekday()

def duration(startTime, endTime):
        time1 = startTime.split(' ')[1].split(':')
        time2 = endTime.split(' ')[1].split(':')
        if int(time2[0]) < int(time1[0]): #time got wrapped after midnight
                time2[0] = int(time2[0]) + 24

        secondDifference = (int(time2[0]) - int(time1[0])) * 3600 + (int((time2[1])) - int((time1[1]))) * 60 + (int(float(time2[2])) - int(float(time1[2])))#convert to seconds
        
        return abs(secondDifference) 

def region_string_to_index(regionstring):
        return regionDict[regionstring]

def id_string_to_index(idstring):
        return idDict[idstring]

def id_to_page_name(index):
        return pathDict[index]


def probability_to_indices(guess):
        guess = guess[0]
        NUM_GUESSES = 10
        
        predictions = []

        for bestGuess in sorted(list(guess), reverse=True)[0:NUM_GUESSES]:
            #Note, because labels are ordered ascending by parser, no need to use classifier.classes_
            labelGuess = list(guess).index(bestGuess)
            predictions.append(labelGuess)
            if bestGuess == 0:
                break
        return predictions

def predict10(features):
        pages = []

        if features[0] in idDict:
            features[0] = id_string_to_index(features[0])
        else:
            features[0] = rand.randint(0,maxID)
        if features[2] in regionDict:
            features[2] = region_string_to_index(features[2])
        else:
            features[2] = rand.randint(0,maxRegion) 
        datestring = features[3]
        features[3] = date_to_int(datestring)
        features.append(fiscal_quarter(datestring))
        features.append(day_of_week(datestring))
        features.append(int(datestring.split(' ')[0].split('-')[1]))

        features = np.array(features, dtype='int32')

        for index in probability_to_indices(classifier.predict_proba(features.reshape(1, -1))):
                pages.append(id_to_page_name(str(index)))

        return pages

def explore10(date):
    pages = []
    for index in buckets[date_to_int(date)]:
        pages.append(id_to_page_name(str(index)))
    return list(pathDict.values())[0:10]

def next_sites(currentsite):
    return []   
