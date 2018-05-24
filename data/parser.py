# File for reading csv data, extracting and coverting necessary features, and
# writing appropriate file. 

import pandas as pd 
import numpy as np
import datetime

rawData = np.array(pd.read_csv('page_hits.csv', encoding='latin-1'))


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
        time1 = startTime.split(' ')[1]
        time2 = endTime.split(' ')[1]
        if int(time2[0]) < int(time1[0]): #time got wrapped after midnight
                time2[0] = int(time2[0]) + 24

        return (int(time2[0]) - int(time1[0])) * 3600 + (int(time2[1]) - int(time1[1])) * 60 + (int(time2[0]) - int(time1[0]))#convert to seconds


#Map the following features to unique indices
ids = {}
numIds = 0
regions = {}
numRegions = 0
paths = {}
numPaths = 0


num_features = 7 #id, ext/int, region, time, duration, path

num_rows = np.shape(rawData)[0]
data = np.empty((num_rows, num_features), dtype='int32')

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
                        if "//" == value:
                                continue
                                print('ignoring local file')
                        if value not in paths:
                                paths[value] = numPaths
                                numPaths += 1
                        data[i][5] = paths[value]

print(data)               