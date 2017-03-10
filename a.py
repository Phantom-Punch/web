#!/usr/bin/env python3
import os
from flask import Flask, url_for, render_template
from flask import request
from flask import send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
    #return '<h1>Hello World</h1>'
    #user_agent = request.headers.get('User-Agent')
    return render_template('index.html')

@app.route('/user/<string>')
def user(string):
    roll = string[0:6]
    credits = string[6:8]
    courses = string[8:27]
    email = string[27:]
    time = os.popen('date').read()
    output_string = time[:-1] + " , " + roll + " , " + credits + " , " + email
    for i in range(len(courses)):
        output_string = output_string + " , " + courses[i]
    file = open("data.csv", "a")
    file.write("%s\n" % output_string)
    file.close()
    return '<h1>Your preferences have been submitted %s!</h1>' % roll

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
