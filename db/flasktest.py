import threading
import sqlite3
import flask
from flask import Flask, request, jsonify
import python_splite_api
cur = sqlite3.connect('peniss.db',check_same_thread=False).cursor()
app = Flask(__name__)
mutex = threading.Lock()
@app.route("/")
def hello_world():
    mutex.acquire()
    try:
        return python_splite_api.getitems_sortedpricerange(cur)
    finally:
        mutex.release()
@app.route("/api", methods=['POST'])
def api_json():
    if (flask.request.headers.get('Content-Type') == 'application/json'):
        req = flask.request.json()['Im tired']
        if req == 'Yes':
            return 'Работай, даун'
        else:
            return 'Иди в жопу'

@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.json
    print(content['mytext'])
    return jsonify({"uuid":uuid})

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)

app.run(host='0.0.0.0', port=80)
