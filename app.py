import json
import sqlite3
from flask import Flask, request, jsonify
from models import init_db


app = Flask(__name__)


@app.route('/api/songs', methods=['GET', 'POST'])
def songs():
    if request.method == 'GET':
        return not_implemented_yet_response()
    elif request.method == 'POST':
        return not_implemented_yet_response()


@app.route('/api/song/<song_id>', methods=['GET', 'PUT', 'DELETE'])
def song(song_id):
    if request.method == 'GET':
        return not_implemented_yet_response()
    elif request.method == 'PUT':
        return not_implemented_yet_response()
    elif request.method == 'DELETE':
        return not_implemented_yet_response()

def not_implemented_yet_response():
    return jsonify({'status': 'NOT_IMPLEMENTED_YET'})

if __name__ == '__main__':
    init_db()
    app.debug = True
    app.run()
