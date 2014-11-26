import datetime
import os

from flask import Flask
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
from twilio.rest import TwilioRestClient


app = Flask(__name__)
client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'], 
    											os.environ['TWILIO_TOKEN'])

@app.route("/", methods=['GET', 'POST'])
def incoming():
	# Receives text messages and records who it's from and the text
	from_number = request.form['From']
	the_text = request.form['Body']

	# save to db

@app.route("/whatwegot", method=['POST'])
def display():
	# displays what we got, for easy retrieving
	
 
if __name__ == "__main__":
    app.run(debug=True)