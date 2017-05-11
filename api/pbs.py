from flask import jsonify
from api import app, cur


KEYS = ['personId', 'eventId', 'best', 'worldRank', 'continentRank', 'countryRank']

def fetch_events():
    cur.execute("SELECT id FROM Events WHERE id NOT IN ('magic','mmagic','333mbo')")
    return [i[0] for i in cur.fetchall()]


def convert_to_dict(tup):
    return {key: value for (key, value) in zip(KEYS, tup)}

@app.route('/pbs/<wcaid>', methods=['GET'])
def pbs(wcaid):
    cur.execute("SELECT * FROM RanksAverage WHERE personId = '%s'" % wcaid)
    s = cur.fetchall()
    new_list = [convert_to_dict(i) for i in s]
    return jsonify({'result': new_list})
