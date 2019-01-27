from flask import Flask, render_template, request, jsonify
from geopy.distance import great_circle
from DatabaseInteraction import Database, Person
import json

app = Flask(__name__)

mode = 'DEV'
# mode = 'PROD'


# get intersecting radii
def get_neighors(lat, lng, radius, interest):
    db = Database.Database()
    db.get_json('DatabaseInteraction/db.json')
    data = db.database
    neighbors = []
    for key, person in data['interests'][interest]['people'].items():
        cur_lat = person['latitude']
        cur_long = person['longitude']
        
        distance = great_circle((lat, lng), (cur_lat, cur_long)).miles
        if(distance - radius - person['radius']):
            neighbors.append(person)
    
    return neighbors

@app.route('/')
def home_page():
    db = Database.Database()

    return render_template('index.html')


@app.route('/getpyram', methods=['POST'])
def get_pyram():
    DB_NAME = 'DatabaseInteraction/db.json'
    assert(request.method=='POST')
    
    
    payload = json.loads(request.get_data())

    


    neighbors = get_neighors(payload['lat'], payload['lng'], payload['radius'], payload['interest'])
    db = Database.Database()
    db.get_json(DB_NAME)
    pers = Person.Person(payload['name'], payload['email'], payload['lng'], payload['lat'], payload['radius'], payload['interest'], payload['contact'])
    db.add_person(pers)
    db.export_json(DB_NAME)
    print(neighbors)
    return jsonify(neighbors)



@app.route('/map/<interest>')
def map(interest):
    
    # assert that this interest exists in our database of interests
    return render_template('map.html', interest=interest)


if __name__ == "__main__":
    if mode == 'DEV':
        app.run(host='0.0.0.0', debug=True, port=5000)
    else:
        app.run(host='0.0.0.0', port=80)
