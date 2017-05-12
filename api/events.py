from flask import jsonify
from api import app, cur
from utils import convert_to_dict


KEYS = ['id', 'name', 'rank', 'format', 'cellName']

@app.route('/events', methods=['GET'])
def get_events():
    cur.execute("SELECT * FROM Events")
    s = cur.fetchall()
    return jsonify({'result': [convert_to_dict(i, KEYS) for i in s]})