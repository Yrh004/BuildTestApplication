from flask import *
import json,time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    data = {'Message':'Automate all the things!','timestamp':time.time()}
    json_dump = json.dumps(data)

    return json_dump

if __name__ == '__main__':
    app.run(port=5849)