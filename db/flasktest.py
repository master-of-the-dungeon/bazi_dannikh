import threading
import sqlite3

from flask import Flask
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
@app.route("/api/allitems", methods=['POST'])
def allitems():
    mutex.acquire()
    try:
        return python_splite_api.getallitems(cur)
    finally:
        mutex.release()
@app.route("/api/cheapest", methods=['POST'])
def cheapest():
    mutex.acquire()
    try:
        return python_splite_api.cheapest(cur)
    finally:
        mutex.release()
@app.route("/api/mostexpensive", methods=['POST'])
def mostexpensive():
    mutex.acquire()
    try:
        return python_splite_api.mostexpensive(cur)
    finally:
        mutex.release()
@app.route("/api/sortedgetpricerange", methods=['POST'])
def getpricerange():
    mutex.acquire()
    try:
        return python_splite_api.getitems_sortedpricerange(cur)
    finally:
        mutex.release()

# @app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
# def add_message(uuid):
#     content = request.json
#     print(content['mytext'])
#     return jsonify({"uuid":uuid})

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)

app.run(host='0.0.0.0', port=80)
