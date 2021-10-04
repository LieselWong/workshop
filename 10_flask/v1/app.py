# Team Untitled (Jonathan Wu, Liesel Wong, Loki, King Hagrid)
#Soft Dev
#K10 - Putting Little Pieces Together/Flask/Devloping our first Flask thing
#2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of the class

@app.route("/")  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

#This version differs from the previous one in that it doesn't have the print statement
#in the function. I think this will result in the difference of the program not printing
#_main_ to the terminal. Otherwise, everything else looks like the same.



