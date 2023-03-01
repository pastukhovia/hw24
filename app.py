import os

from flask import Flask, abort, jsonify
from flask import request
from utils import query_handler

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query():
    req_data = request.get_json()
    query = [req_data.get('cmd1'), req_data.get('cmd2')]
    file_name = req_data.get('file_name')
    values = [req_data.get('val1'), req_data.get('val2')]

    if None in query:
        abort(400)

    if file_name is None:
        abort(400)

    if not os.path.exists(DATA_DIR + os.sep + file_name):
        abort(400)

    temp_res = None
    res = None
    for i in range(len(query)):
        res = query_handler(query[i], values[i], temp_res, DATA_DIR + os.sep + file_name)
        temp_res = res

    print(type(res))

    return jsonify(list(res))


if __name__ == '__main__':
    app.run(debug=True)
