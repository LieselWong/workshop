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

#Since the program only returns "No hablo queso!"
# and never prints main, the result
# will be "no hablo queso!" displayed on the webpage.

#Runtime Result: same


