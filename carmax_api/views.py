from flask import render_template, request
import MySQLdb as mdb
from carmax_api import app
import sys, json
sys.path.append("..")
from settings import *

conn = mdb.connect(
    user = user,
    passwd = passwd,
    host = host,
    db = db
)
cur = conn.cursor()

@app.route("/")
def index():
    return "Index Page"

@app.route("/api/model/*")
def carmax_api_model():
    model = request.url.split('/')[-1]
    data = "{'status': 'OK', 'mode': '{}'}".format(model)
    return json.dumps(data)

@app.route("/api/type/*")
def carmax_api_type():
    _type = request.url.split('/')[-1]
    data = "{'status': 'OK', 'mode': '{}'}".format(_type)
    return json.dumps(data)

@app.route("/api")
def carmax_api():
    make = request.args.get('make', default = "*", type = str)
    model = request.args.get('model', default = "*", type = str)
    year = request.args.get('year', default = "*", type = str)

    query = "SELECT * FROM CARS WHERE make = '{}' AND model = '{}' AND year = '{}'".format(make, model, year)
    cur.execute(query)
    row_headers = [x[0] for x in cur.description]
    data = cur.fetchall()
    json_data = []

    for t in data:
        json_data.append(dict(zip(row_headers, t)))

    return json.dumps(json_data, default = str)

