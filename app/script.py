from flask import  Flask, render_template, request, redirect, url_for, flash, make_response, session


app = Flask(__name__)
app.secret_key = "super secret key"


@app.route("/")
def home():
	return render_template("home.html")


@app.route('/visits-counter')
def visits():
	if 'visits' in session:
		session['visits'] = session.get('visits') + 1
	else:
		session['visits'] = 1
	return render_template("visits.html", session = session)


@app.route('/delete-visits')
def delete_visits():
	session.pop('visits', None) 
	return render_template("delete_visits.html")

if __name__ == "__main__":
	app.run(port=80, host='0.0.0.0',debug=True)
