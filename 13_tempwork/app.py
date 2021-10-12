# Team KingMlob: Liesel Wong, Yaying Liang, Rachel Xiao (Duckies: King Hagrid, Blob, and Mooana)
# SoftDev
# K13 -- Template for Success
# 2021-10-08

from flask import Flask, render_template
import csv
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

occupations = {}


with open('data/occupations.csv') as csv_file: #give access to the file by opening it
    reader = csv.reader(csv_file, delimiter=',') #delimeter puts values in a list for each row as it splits by commas
    for row in reader:
        if row[0] != "Job Class": #don't store the heading or total
            occupations[row[0]] = [float(row[1]), row[2]] #put the data in a dictionary

            
def make_choice():
    jobs = list(occupations.keys()) # convert the keys into a list
    jobs.pop(len(jobs)-1)
    values = list(occupations.values())
    values.pop(len(values)-1)
    percentages = []
    for arr in values:
        percentages.append(arr[0])
    choice = random.choices(jobs, weights = percentages, k=1)
    return choice[0] + " | Link: " + occupations[choice[0]][1]

@app.route("/occupyflaskst")

def test_tmplt():
    return render_template('tablified.html', dict = occupations, selected_occupation = make_choice())

if __name__ == "__main__":
    app.debug = True
    app.run()
