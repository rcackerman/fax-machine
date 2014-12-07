from datetime import datetime
import json
import os


from flask import Flask, jsonify
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import class_mapper
from twilio.rest import TwilioRestClient

'''
Config
POSTGRES: postgresql://localhost/test
'''


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['POSTGRES']
db = SQLAlchemy(app)

# client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'],
# os.environ['TWILIO_TOKEN'])

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(256))
    body = db.Column(db.Text)
    date = db.Column(db.DateTime)

    def __init__(self, sender, body, date=False):
        self.sender = sender
        self.body = body
        self.date = date
        if date is False:
            self.date = datetime.utcnow()

    def __repr__(self):
        return self.body


# Create the tables if needed.
db.create_all()


@app.route("/messages", methods=['GET', 'POST'])
def messages():
    if request.method == 'POST':
        # Receives text messages and records who it's from and the text
        sender = request.form['From']
        body = request.form['Body']

        # save to db
        m = Message(sender, body)
        db.session.add(m)
        db.session.commit()
        return "OK", 201

    if request.method == 'GET':
        messages =  Message.query.all()
        message_dict = [dict(sender = m.sender, date = m.date.isoformat(), body = m.body) for m in messages]
        return json.dumps(message_dict)



if __name__ == "__main__":
    app.run(debug=True)
