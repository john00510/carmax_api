from flask import render_template, request
import MySQLdb as mb
from carmax_api import app

@app.route("/")
def index():
    return "Index Page"

@app.route("/api")
def carmax_api():
    return 'test'
