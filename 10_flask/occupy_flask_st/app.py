#Team Untitled - Jonathan W., Liesel W., Loki, King Hagrid
#SoftDev
#K10 -- Putting Little Pieces Together/Flask and Python/Putting all the knowledge from the previous classwork and homework into one app.
#2021-10--04

from flask import Flask
import pandas as pd
import random
import requests
import io

app = Flask(__name__)

@app.route("/")
def jobHunting():
    url = "https://raw.githubusercontent.com/stuy-softdev/notes-and-code/main/smpl/k06/occupations.csv?token=ARNHYM3SD5ALBEMZCWSKJQLBLS7EQ"
    download = requests.get(url).content
    df = pd.read_csv(io.StringIO(download.decode('utf-8')))
    dataDict = {}
    weighted = []
    percentSum, jobIndex = 0, 0
    jobRandom = random.randint(0,998)
    for i in df.index:
        if (df['Job Class'][i] != "Total"):
            dataDict[df['Job Class'][i]] = df['Percentage'][i]
            percentSum += df['Percentage'][i]*10
            if jobRandom >= percentSum:
                jobIndex += 1
            weighted.append(percentSum)
    keyList = list(dataDict)
    occupationList = "";
    for name in keyList:
        occupationList += name + "<br/>"
    stringText = "<h2>Team Untitled - Jonathan W. , Liesel W. , Loki , King Hagrid</h2>" + "<h2>Chosen Occupation: " + (keyList[jobIndex]) + "</h2> <h3>List of Occupations: </h3>" + occupationList
    return stringText

app.run()