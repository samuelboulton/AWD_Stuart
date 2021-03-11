import json
from flask import Flask, jsonify, request, Response, render_template
from flaskext.mysql import MySQL
import hashlib

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'samuel.boulton'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Bonnie17.'
app.config['MYSQL_DATABASE_DB'] = 'samuelboulton'
app.config['MYSQL_DATABASE_HOST'] = 'cs2s.yorkdc.net'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/dbgetRest', methods=['GET'])
def get():
    resultList = []
    cursor.execute("SELECT * FROM Restaurants")
    result = cursor.fetchall()
    for i in result:
        dataout ={'RestaurantID' : i[0], 'Restaurant' : i[1], 'Website' : i[2], 'Review' : i[3]}
        resultList.append(dataout)
    return jsonify(resultList)

@app.route('/')
def insert():
    return "routePage"

if __name__ == '__main__':
    app.run(host="82.163.245.110", port=5008)