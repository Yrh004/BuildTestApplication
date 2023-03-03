from flask import Flask
import json,time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set ={'Message':'Automate all the things!','timestamp':time.time()}
    json_dump = json.dumps(data_set)

    return json_dump
