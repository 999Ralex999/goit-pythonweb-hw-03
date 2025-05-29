from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

if not os.path.exists('storage'):
    os.makedirs('storage')
if not os.path.exists('storage/data.json'):
    with open('storage/data.json', 'w') as f:
        json.dump({}, f)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        username = request.form.get('username')
        message_text = request.form.get('message')

        if username and message_text:
            timestamp = str(datetime.now())
            with open('storage/data.json', 'r') as f:
                data = json.load(f)
            data[timestamp] = {
                'username': username,
                'message': message_text
            }
            with open('storage/data.json', 'w') as f:
                json.dump(data, f, indent=2)
            return redirect(url_for('read'))

    return render_template('message.html')


@app.route('/read')
def read():
    with open('storage/data.json', 'r') as f:
        messages = json.load(f)
    return render_template('read.html', messages=messages)


@app.errorhandler(404)
def not_found(e):
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(port=3000)

