import json
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def read(key='time'):
    # read start_time and end_time from url
    start_time = request.args.get("start_time", "2021-01-28 18:30:00")
    end_time = request.args.get("end_time", "2021-01-28 20:10:00")

    # opening of json file
    with open('db.json', 'r') as r:
        data = json.load(r)

    # making of list of dictionary for storig value of belt1 belt2 and their count in given duration for each id
    array = [{}]*10
    # initialize with 0 value
    array[0] = {'belt1': 0, 'belt2': 0, 'cnt': 0}
    array[1] = {'belt1': 0, 'belt2': 0, 'cnt': 0}
    array[2] = {'belt1': 0, 'belt2': 0, 'cnt': 0}
    array[3] = {'belt1': 0, 'belt2': 0, 'cnt': 0}
    array[4] = {'belt1': 0, 'belt2': 0, 'cnt': 0}
    array[5] = {'belt1': 0, 'belt2': 0, 'cnt': 0}
    array[6] = {'belt1': 0, 'belt2': 0, 'cnt': 0}
    array[7] = {'belt1': 0, 'belt2': 0, 'cnt': 0}
    array[8] = {'belt1': 0, 'belt2': 0, 'cnt': 0}
    array[9] = {'belt1': 0, 'belt2': 0, 'cnt': 0}

    # traversing data
    for i in range(len(data)):
        # checking for given duration
        if(data[i][key] >= start_time and data[i][key] <= end_time):
            # if state true then belt1 = 0
            if(data[i]['state'] == True):
                array[int(data[i]['id'][2:5])]['belt1'] += 0
                array[int(data[i]['id'][2:5])]['belt2'] += data[i]['belt2']
                array[int(data[i]['id'][2:5])]['cnt'] += 1
            # if state true then belt1 = 0
            else:
                array[int(data[i]['id'][2:5])]['belt2'] += 0
                array[int(data[i]['id'][2:5])]['belt1'] += data[i]['belt1']
                array[int(data[i]['id'][2:5])]['cnt'] += 1

    # creating array for storing dictionaries
    a = []
    for i in range(len(array)):
        if (array[i]['cnt'] != 0):
            dict1 = {"Id": i, "avg_belt1": array[i]['belt1'] // array[i]['cnt'],
                     "avg_belt2": array[i]['belt2']//array[i]['cnt']
                     }
            a.append(dict1)
    return(jsonify(a))
    
