from flask import Flask
import MySQLdb
import os
app = Flask(__name__)



myConnection = MySQLdb.connect(
    host=os.getenv('SQL_HOST'),
    user=os.getenv('SQL_USERNAME'),
    passwd=os.getenv('SQL_PASSWORD'),
    db=os.getenv('SQL_WCA_DB'),
    use_unicode=True)

cur = myConnection.cursor()

import api.comps
import api.pbs
import api.events
import api.persons

@app.route('/')
def main():
    return "oh hei"

if __name__ == "__main__":
    app.run()
