from flask import Flask, request, redirect, jsonify, url_for
import mysql_mongodb as connector
import mongo_to_mongo as conn2
import csv_mongodb as conn3
import json
import io
from NLP import chatopenai, levenshtein2, rootcheckmodel, ftest

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'task is: %s' % name


@app.route('/mysql_mongo', methods=['post', 'get'])
def hello_world():
    host_mo = request.form['host_mo']
    host_mysql = request.form['host_mysql']
    client_mo = request.form['client_mo']
    db_mysql = request.form['db_mysql']
    user_mysql = request.form['user_mysql']
    pass_mysql = request.form['pass_mysql']
    val = connector.migrate(host_mo, host_mysql, client_mo,
                            db_mysql, user_mysql, pass_mysql)
    print(val)
    return redirect("http://127.0.0.1:5500/webserver/templates/index.html")


@app.route('/mongo', methods=['post'])
def new():
    path = request.form['path']
    val = conn2.migrate(path)
    print(val)
    return redirect("http://127.0.0.1:5500/webserver/templates/index.html")


@app.route('/csv', methods=['post'])
def new2():
    path = request.form['path']
    val = conn3.mongoimportcsv(path, 'local', 'startup_log')
    print(val)
    return redirect("http://127.0.0.1:5500/webserver/templates/index.html")


@app.route('/index', methods=['post'])
def login():
    email = request.form['email']
    password = request.form['password']
    # we plan to integrate Login using database here
    if (email == "harsh@gmail.com" and password == "harsh"):
        print("Successful login")
        return redirect("http://127.0.0.1:5500/webserver/templates/index.html")


@app.route('/dashboard', methods=['post'])
def buttonclick():
    data = json.load(io.BytesIO(request.data))

    func = data["funcName"]
    print("Dashboard function call:", func)
    if (func == "openai"):
        a = chatopenai.nlp()
        print(a)
        return redirect("http://127.0.0.1:5500/webserver/templates/index.html")
    elif (func == "leven"):
        levenshtein2.nlp()
    elif (func == "root"):
        rootcheckmodel.nlp()
    elif (func == "ftest"):
        ftest.nlp()
    elif (func == "spacy"):
        # call spacy func here
        print("spacy will come here")

    return redirect("http://127.0.0.1:5500/webserver/templates/index.html")


if __name__ == '__main__':
    app.run()
