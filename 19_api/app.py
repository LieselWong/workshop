#*V-***: Liesel Wong (King Hagrid), Austin Ngan (Gerald)
#SoftDev
#K19 -- A RESTful Journey Skyward
#2021-11-22


from flask import Flask, render_template
import urllib.request
import json

app = Flask(__name__)

@app.route("/")
def test():
	data=urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=A6sYUc7R6zCWzLWQTrcuf2Kw2QclDsBJRr3TsGbg")
	html=json.loads(data.read())
	#print(html)
	pic=html['url']
	explanation=html['explanation']
	title=html['title']
	return render_template('main.html', title=title, pic=pic, explanation=explanation)


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
