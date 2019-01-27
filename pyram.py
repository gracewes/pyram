from flask import Flask, render_template
from Database import *

app = Flask(__name__)

mode = 'DEV'
# mode = 'PROD'

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/map/<interest>')
def map(interest):
    # assert that this interest exists in our database of interests
    return render_template('map.html', interest=interest)


if __name__ == "__main__":
    if mode == 'DEV':
        app.run(host='0.0.0.0', debug=True, port=5000)
    else:
        app.run(host='0.0.0.0', port=80)