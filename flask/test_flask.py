from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return "goodbye world"

@app.route("/user/<username>")
def lala(username):
		#return "hello " + username + " dude!!"
		return render_template('profile.html' ,name=username)

if __name__== "__main__":
	app.run(debug=True)

#one script infinite number of urls!!