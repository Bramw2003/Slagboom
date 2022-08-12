import json
from flask import Flask, request, render_template, url_for, jsonify
from os import system

app = Flask(__name__)

@app.route('/open')
def open_gate():
    exitCode = system("exit 0")
    if(exitCode == 0):
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "something went wrong"})

@app.route("/")
def hello_world():
    return render_template('slagboom.html.j2', url=url_for('open_gate'))
