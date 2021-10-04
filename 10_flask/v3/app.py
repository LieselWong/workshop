# Team Untitled (Jonathan Wu, Liesel Wong, Loki, King Hagrid)
#Soft Dev
#K10 - Putting Little Pieces Together/Flask/Devloping our first Flask thing
#2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")   #assign fxn to route    
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

#We know from K09 that the debug statement is off by default. The difference
#here is that the code turns on the debugger. We can safely predict that the
#terminal will spit out some debugging code or something similar.

