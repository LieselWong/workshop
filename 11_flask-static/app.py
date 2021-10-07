#Team Untitled - Jonathan W. , Liesel W. , Loki , King Hagrid
#SoftDev
#K11 -- Some Thing Never Change/basics of /static folder/We first observed the behavior of foo and foo.html, took notes, and then composed and stored another html with some html so that flask can serve that staticly.
#2021-10--06

# DEMO 
# basics of /static folder

from flask import Flask
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
