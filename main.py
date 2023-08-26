from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/guide')
def scholarship_Guide():
	return render_template('scolarship_guide.html')

	

if __name__ == "__main__":
	app.run(debug=True)