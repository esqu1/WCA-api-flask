from flask import jsonify
from api import app, cur


KEYS = ['personId', 'eventId', 'best', 'worldRank', 'continentRank', 'countryRank']


def convert_to_dict(tup):
    return {key: value for (key, value) in zip(KEYS, tup)}

@app.route('/pbs/<wcaid>', methods=['GET'])
def pbs(wcaid):
    cur.execute("SELECT * FROM RanksSingle WHERE personId = '%s'" % wcaid)
    s = cur.fetchall()
    single_list = [convert_to_dict(i) for i in s]

    cur.execute("SELECT * FROM RanksAverage WHERE personId = '%s'" % wcaid)
    s = cur.fetchall()
    average_list = [convert_to_dict(i) for i in s]
    return jsonify({'result': {'single': single_list, 'average': average_list}})
