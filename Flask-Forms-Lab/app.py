from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]
username = "a"
password = "a"



@app.route('/', methods = ['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		if request.form["username"] == username and request.form["password"] == password:
			return render_template("home.html",friends = facebook_friends)

@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/friends_exists/<string:friendname>',methods = ['GET','POST'])
def friends1(friendname):
	if (friendname in facebook_friends):
		return render_template("friend_exists.html",hi = "true")
	else:
		return render_template("friend_exists.html",hi = "false")



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)