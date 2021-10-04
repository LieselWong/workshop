# Team Untitled (Jonathan Wu, Liesel Wong, Loki, King Hagrid)
#Soft Dev
#K10 - Putting Little Pieces Together/Flask/Devloping our first Flask thing
#2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")  #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__": # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

# If _name_ = _main_:
# We think this would print "about to print_name_... and then in the next line in terminal
# it will print _main_. It'll print then print no hablo queso! on the website you get
# from running the program.
# With app.debug on, the computer will spit out some debugging code or whatever.
#If _name != _main_:
#nothing will happen.
