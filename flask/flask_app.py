from flask import Flask
app = Flask("first app")

@app.route('/')
def index():
	return "yes it is working"

@app.route('/next')
def next_route():
	return "this is next"

if __name__=="__main__":
	app.run()
