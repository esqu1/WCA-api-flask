from flask import jsonify
import json
from api import app
import os
import MySQLdb

myConnection = MySQLdb.connect(host=os.getenv('SQL_HOST'), user=os.getenv('SQL_USERNAME'), passwd=os.getenv('SQL_PASSWORD'), db=os.getenv('SQL_WCA_DB'))
cur = myConnection.cursor()

@app.route('/comps/<int:id>', methods=['GET'])
def get_comp(id):    
    cur.execute('SELECT * FROM Competitions')
    s = cur.fetchall()
    data = s[id]
    new_data = []
    for el in data:
        try:
            new_data.append(str(unicode(el,'latin-1').encode('utf8')))
        except TypeError:
            new_data.append(str(el))
    return jsonify({'result': new_data})
    

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
                new_data.append(str(unicode(l,'latin-1').encode('utf8')))
            except TypeError:
                new_data.append(str(l))
        new_list.append(new_data)
    return jsonify({'result': new_list})