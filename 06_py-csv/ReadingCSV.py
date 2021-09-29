#Liesel Wong (Untitled - Jonathan W., Liesel W.)
#SoftDev
#K06 -- Reading and sampling from a CSV file
#2021-09-28

# Findings:
# - We found an effective way to download the CSV from Github using the link
# - We learned about new functions including download.decode, meaning it's decoding the file from Unicode.
#   Then io.StringIO coverts into a stream that read_csv then turns into a data frame.
# - We learned how to use and print both the key and value in Dictionaries
# - We developed an algorithm which effectively to weight the jobs based on their given percentages and
#   pick a random job. Specifically, we added the given percentages into one variable, and added an index
#   until the variable was greater than the random number generated. In this way, we checked that the random
#   number was between an interval: value of index before < random number < value of index after

#imports many libraries like panda, random, requests, and io
import pandas as pd
import random
import requests
import io

#would split the .csv file into a dictionary and then prints a job based on its weighted percents
def jobHunting():
    #stores the RAW url file from GitHub
    url = "https://raw.githubusercontent.com/stuy-softdev/notes-and-code/main/smpl/k06/occupations.csv?token=ARNHYM3SD5ALBEMZCWSKJQLBLS7EQ"
    #retrives the url from GitHub
    download = requests.get(url).content
    #converts the URL and decodes it into a readable 
    df = pd.read_csv(io.StringIO(download.decode('utf-8')))

    #variables to separate the dataframe into workable data and then generate a random job that is weighted
    dataDict = {}
    weighted = []
    percentSum, jobIndex = 0, 0
    jobRandom = random.randint(0,998)

    #loops through the dataframe, converts it into a dictionary that we want to use: 'Job Name' - 'Percentage'.
    #then it takes the percent, multiplies it by 10, adds onto itself and then adds that value to a list
    #based on the random integer generate, it compares it all the cumulative values unless it finds a value l
    for i in df.index:
        if (df['Job Class'][i] != "Total"):
            dataDict[df['Job Class'][i]] = df['Percentage'][i]
            percentSum += df['Percentage'][i]*10
            if jobRandom >= percentSum:
                jobIndex += 1
            weighted.append(percentSum)

    #Converts the keys in the main dictionary into a list with only the key
    keyList = list(dataDict)
    #prints the randomly generated job
    print(keyList[jobIndex])

jobHunting()