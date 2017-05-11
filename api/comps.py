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


@app.route('/comps/<int:id>', methods=['GET'])
def get_comp(id):
    cur.execute('SELECT * FROM Competitions')
    s = cur.fetchall()
    data = s[id]
    new_data = []
    for el in data:
        try:
            new_data.append(str(unicode(el, 'latin-1').encode('utf8')))
        except TypeError:
            new_data.append(str(el))
    return jsonify({'result': convert_to_dict(new_data)})


@app.route('/comps', methods=['GET'])
def get_all():
    cur.execute('SELECT * FROM Competitions')
    s = cur.fetchall()
    new_list = []
    for el in s:
        data = el
        new_data = []
        for l in data:
            try:
                new_data.append(str(unicode(l, 'latin-1').encode('utf8')))
            except TypeError:
                new_data.append(str(l))
        new_list.append(convert_to_dict(new_data))
    return jsonify({'result': new_list})
