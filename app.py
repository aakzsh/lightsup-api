import os
from flask import Flask, render_template, request, redirect
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from twilio.rest import Client
from sendgrid.helpers.mail import Mail




app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return "hello"



@app.route('/send/<email>', methods=["GET"])
def send(email):
    message = Mail(
        from_email='aakashferrari@gmail.com',
        to_emails=email,
        subject='new note ❤️',
        html_content=f'hey, youve received a new note from your partner, view it on Light Up!!')
    sg = SendGridAPIClient('api keyyyyyyyyy')
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
    return str(response.status_code)



if __name__ == '__main__':
    app.run(debug=True)