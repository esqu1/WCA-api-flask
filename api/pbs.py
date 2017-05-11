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


def fetch_events():
	cur.execute("SELECT id FROM Events WHERE id NOT IN ('magic','mmagic','333mbo')")
	return [i[0] for i in cur.fetchall()]

@app.route('/pbs/<wcaid>', methods=['GET'])
def pbs(wcaid):
	cur.execute("SELECT * FROM RanksAverage WHERE personId = '%s'" % wcaid)
	s = cur.fetchall()
	return jsonify({'result': s})