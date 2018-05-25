# File for reading csv data, extracting and coverting necessary features, and
# writing appropriate file. 

import pandas as pd 
import numpy as np
import datetime

rawData = np.array(pd.read_csv("page_hits.csv", encoding='latin-1'))


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
        month = int(value.split(' ')[0].split('-')[1])
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


#Map the following features to unique indices
ids = {}
numIds = 0
regions = {}
numRegions = 0
paths = {}
numPaths = 0


num_features = 7 #id, ext/int, region, time, duration, path

valueseries = []
for i, row in enumerate(rawData):
        value = row[7]
        if "\\\\" == value[:2]: #ignore local files
                continue
        if ">": #get last in path, if path
                values = value.split(">") 
        else:
                values = [value]
        for value in values:
            if value not in paths:
                    paths[value] = numPaths
                    numPaths += 1
            valueseries.append(paths[value])

feature_file = open("time_features.txt", 'w')
label_file = open("time_labels.txt", "w")
for i, value in enumerate(valueseries):
    if i == len(valueseries) - 2:
        break
    else:
        feature_file.write(str(value))
        feature_file.write("\n")
        label_file.write(str(valueseries[i + 1]))

feature_file.close()
label_file.close()
