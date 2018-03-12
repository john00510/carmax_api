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

@app.route("/api")
def carmax_api():
    make = request.args.get('make', default = "*", type = str)
    model = request.args.get('model', default = "*", type = str)

    query = "SELECT make, model, year, color, vin, mileage, url, nhtsa_rating, dealer, source, stock, price, photos, key_features, key_specs, _condition, reviews, base_features, base_specs, jd_rating FROM cars WHERE make = '{}' AND model = '{}'".format(make, model)
    cur.execute(query)
    row_headers = [x[0] for x in cur.description]
    data = cur.fetchall()
    json_data = []

    for t in data:
        json_data.append(dict(zip(row_headers, t)))

    return json.dumps(json_data, default = str)

