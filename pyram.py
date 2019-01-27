from flask import Flask, render_template, request, jsonify
from geopy.distance import great_circle
from DatabaseInteraction import Database
import json

app = Flask(__name__)

mode = 'DEV'
# mode = 'PROD'


# get intersecting radii
def get_neighors(longitude, latitude, radius, interest):
    db = Database.Database()
    db.get_json('DatabaseInteraction/db.json')
    data = db.database
    neighbors = []

    for key, person in data['interests'][interest]['people'].items():
        cur_long = person['longitude']
        cur_lat = person['latitude']
        distance = great_circle((longitude, latitude), (cur_long, cur_lat)).miles
        if(distance - radius - person['radius']):
            neighbors.append(person)
    
    return neighbors

@app.route('/')
def home_page():
    db = Database.Database()

    return render_template('index.html')

@app.route('/getpyram', methods=['POST'])
def get_pyram():
    assert(request.method=='POST')
    
    
    # payload = request.form
    # name = payload['name']
    # print(name)
    

    get_neighors(30.611676, -96.341768, 300, "rock climbing")
    db = Database.Database()
    db.get_json('DatabaseInteraction/db.json')
    
    #db.add_person()
    return "complete"



@app.route('/map/<interest>')
def map(interest):
    
    # assert that this interest exists in our database of interests
    return render_template('map.html', interest=interest)


if __name__ == "__main__":
    if mode == 'DEV':
        app.run(host='0.0.0.0', debug=True, port=5000)
    else:
        app.run(host='0.0.0.0', port=80)
