from flask import jsonify
from api import app
import os
import MySQLdb

myConnection = MySQLdb.connect(host=os.getenv('SQL_HOST'), user=os.getenv('SQL_USERNAME'), passwd=os.getenv('SQL_PASSWORD'), db=os.getenv('SQL_WCA_DB'))
cur = myConnection.cursor()

@app.route('/comps/<int:id>', methods=['GET'])
def get_comp(id):    
    cur.execute('SELECT * FROM Competitions')
    s = cur.fetchall()    
    return jsonify({'result': s[id]})

#@app.route('/comps', methods=['GET'])
