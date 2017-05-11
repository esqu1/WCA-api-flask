from flask import jsonify
from api import app
import os
import MySQLdb


@app.route('/comps/<int:id>', methods=['GET'])
def get_comps(id):
    myConnection = MySQLdb.connect(user=os.getenv('SQL_USERNAME'), passwd=os.getenv('SQL_PASSWORD'), db=os.getenv('SQL_WCA_DB'))
    cur = myConnection.cursor()
    cur.execute('SELECT * FROM Competitions')
    s = cur.fetchall()    
    return jsonify({'result': s[id]})
