from flask import Flask, render_template, jsonify
from random import *
from random import choice
from flask_cors import CORS
import requests

app = Flask(__name__,
            static_folder = "./dist/static",
			template_folder = "./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})			
@app.route('/api/random')

#songs = ['Little Red Rooster, Key of G', 'Basic 12-bar Blues, Any Key',
 #    'Should I Stay or Should I Go?, Key of E']
 #response = {'Song': random.choice(songs)		
def random_song():
    response = {
        'randomSong': random.choice(songs)
        }
    return jsonify(response)
	
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
