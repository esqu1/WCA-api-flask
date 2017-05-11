from flask import jsonify
from api import app
import os
import MySQLdb

myConnection = MySQLdb.connect(
    host=os.getenv('SQL_HOST'),
    user=os.getenv('SQL_USERNAME'),
    passwd=os.getenv('SQL_PASSWORD'),
    db=os.getenv('SQL_WCA_DB'))
cur = myConnection.cursor()

COMP_KEYS = [
    'id', 'name', 'cityName', 'countryId', 'information', 'year', 'month',
    'day', 'endMonth', 'endDay', 'eventSpecs', 'wcaDelegate', 'organiser',
    'venue', 'venueAddress', 'venueDetails', 'external_website', 'cellName',
    'latitude', 'longitude'
]


def convert_to_dict(tup):
    return {key: value for (key, value) in zip(COMP_KEYS, tup)}

def encode_utf8(fetch):
    new_list = []
    for el in fetch:
        data = el
        new_data = []
        for l in data:
            try:
                new_data.append(str(unicode(l, 'latin-1').encode('utf8')))
            except TypeError:
                new_data.append(str(l))
        new_list.append(convert_to_dict(new_data))
    return jsonify({'result': new_list})


@app.route('/comps/<int:id>', methods=['GET'])
def get_comp(id):
    cur.execute('SELECT * FROM Competitions')
    s = cur.fetchall()
    data = [s[id]]
    return encode_utf8(data)


@app.route('/comps', methods=['GET'])
def get_all():
    cur.execute('SELECT * FROM Competitions')
    s = cur.fetchall()
    return encode_utf8(s)

@app.route('/comps/<date>', methods=['GET'])
def choose_from_date(date):
    cur.execute("SELECT * FROM Competitions WHERE ABS(DATEDIFF('%s', CONCAT_WS('-', CONCAT(year), LPAD(CONCAT(endMonth),2,'0'), LPAD(CONCAT(day), 2, '0')))) < 5" % date)
    s = cur.fetchall()
    return encode_utf8(s)