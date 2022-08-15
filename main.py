from random import randint
from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, request, render_template, url_for, jsonify
from os import system
import os

app = Flask(__name__)


app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route('/open')
def open_gate():
    user = os.popen('whoami').read()
    exitCode = system("python3 /home/pi/python-host/switchbot_py3.py -d 'id'")
    if(exitCode == 0):
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": user})

@app.route("/")
def hello_world():
    return render_template('slagboom.html.j2', url=url_for('open_gate'))
