from flask import Flask
app = Flask(__name__)

import api.comps
import api.pbs

@app.route('/')
def main():
    return "oh hei"

if __name__ == "__main__":
    app.run()
