from flask import jsonify
from api import app, cur
from utils import convert_to_dict

KEYS = [
    'id', 'name', 'cityName', 'countryId', 'information', 'year', 'month',
    'day', 'endMonth', 'endDay', 'eventSpecs', 'wcaDelegate', 'organiser',
    'venue', 'venueAddress', 'venueDetails', 'external_website', 'cellName',
    'latitude', 'longitude'
]

cur.execute("SET NAMES 'utf8'")


@app.route('/comps/<int:id>', methods=['GET'])
def get_comp(id):
    cur.execute('SELECT * FROM Competitions')
    s = cur.fetchall()
    data = [s[id]]
    return jsonify({'result': [convert_to_dict(i, KEYS) for i in data]})


@app.route('/comps', methods=['GET'])
def get_all():
    cur.execute('SELECT * FROM Competitions')
    s = cur.fetchall()
    return jsonify({'result': [convert_to_dict(i, KEYS) for i in s]})


@app.route('/comps/<date>', methods=['GET'])
def choose_from_date(date):
    cur.execute("SELECT * FROM Competitions WHERE ABS(DATEDIFF('%s', CONCAT_WS('-', CONCAT(year), LPAD(CONCAT(endMonth),2,'0'), LPAD(CONCAT(day), 2, '0')))) < 5" % date)
    s = cur.fetchall()
    return jsonify({'result': [convert_to_dict(i, KEYS) for i in s]})
