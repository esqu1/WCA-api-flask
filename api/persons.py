# -*- coding: utf-8 -*-
from flask import jsonify
from api import app, cur
from utils import convert_to_dict


KEYS = ['id', 'subid', 'name', 'countryId', 'gender']
cur.execute("SET NAMES 'utf8'")


@app.route('/persons', methods=['GET'])
def get_persons():
    cur.execute("SELECT * FROM Persons")
    s = cur.fetchall()
    return jsonify({'result': [convert_to_dict(i, KEYS) for i in s]})

@app.route('/persons/<wcaid>', methods=['GET'])
def get_person_id(wcaid):
    cur.execute("SET NAMES 'utf8'")