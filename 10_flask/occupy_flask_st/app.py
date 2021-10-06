#Team Untitled - Jonathan W., Liesel W., Loki, King Hagrid
#SoftDev
#K10 -- Putting Little Pieces Together/Flask and Python/Putting all the knowledge from the previous classwork and homework into one app.
#2021-10--04

from flask import Flask
import csv
import random

app = Flask(__name__)

@app.route("/")
def jobHunting():
    dataDict = {}
    with open('occupations.csv', mode='r') as inp:
        reader = csv.reader(inp)
        next(reader)
        dataDict = {rows[0]:float(rows[1]) for rows in reader}
    dataDict.pop('Total')
    weighted = []
    percentSum, jobIndex = 0, 0
    jobRandom = random.randint(0,998)
    for num in dataDict.values():
        percentSum += num*10
        if jobRandom >= percentSum:
            jobIndex += 1
        weighted.append(percentSum)
    keyList = list(dataDict)
    occupationList = ""
    for name in keyList:
        occupationList += name + "<br/>"
    stringText = "Team Untitled - Jonathan W. , Liesel W. , Loki , King Hagrid</br></br>" + "Chosen Occupation: " + (keyList[jobIndex]) + "</br></br> List of Occupations: </br></br>" + occupationList
    return stringText

app.run()