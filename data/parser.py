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

num_rows = np.shape(rawData)[0]
data = np.zeros((num_rows, num_features), dtype='int32')

for i, row in enumerate(rawData):
        for j, value in enumerate(row):
                if j == 0: #id
                        if value not in ids:
                                ids[value] = numIds
                                numIds += 1
                        data[i][0] = ids[value]

                elif j == 2: #ext/int
                        if value == 'external':
                                data[i][1] = 0
                        else:
                                data[i][1] = 1

                elif j == 4: #region
                        if value not in regions:
                                regions[value] = numRegions
                                numRegions += 1
                        data[i][2] = regions[value]

                elif j == 5: #time block, morning midday night (0, 1, 2)
                        data[i][3] = date_to_int(value)
                        data[i][6] = day_of_week(value)

                elif j == 6:
                        data[i][4] = duration(rawData[i][5], value)

                elif j == 7:
                        if "\\\\" in value[:2]: #ignore local files
                                data[i][5] = -1 #signals invalid row, DON'T PRINT
                                continue
                        if value not in paths:
                                paths[value] = numPaths
                                numPaths += 1
                        data[i][5] = paths[value]

pathCounts = np.zeros((numIds, numPaths), dtype='int32')

doNotPrint = set()
for i in range(num_rows):
        userid = data[i][0]
        pathid = data[i][5]

        if pathid != -1:
                pathCounts[userid][pathid] += 1
        else:
                doNotPrint.add(i)

labels = []
for pathCount in pathCounts:
        labels.append((list(pathCount).index(max(pathCount))))

feature_file = open("features.txt", 'w')
label_file = open("labels.txt", "w")
for i, row in enumerate(data):
        if i not in doNotPrint:
            for j, elem in enumerate(row):
                    feature_file.write(str(elem) + ", ")
            feature_file.write("\n")
            label_file.write(str(labels[data[i][0]]) + ", ")
feature_file.close()
label_file.close()

