from flask import jsonify
from api import app, cur
from utils import convert_to_dict


KEYS = ['personId', 'eventId', 'best', 'worldRank', 'continentRank', 'countryRank']


@app.route('/pbs/<wcaid>', methods=['GET'])
def pbs(wcaid):
    cur.execute("SELECT * FROM RanksSingle WHERE personId = '%s'" % wcaid)
    s = cur.fetchall()
    single_list = [convert_to_dict(i, KEYS) for i in s]

    cur.execute("SELECT * FROM RanksAverage WHERE personId = '%s'" % wcaid)
    s = cur.fetchall()
    average_list = [convert_to_dict(i, KEYS) for i in s]
    return jsonify({'result': {'single': single_list, 'average': average_list}})
