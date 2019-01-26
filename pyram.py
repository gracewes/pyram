from flask import Flask, render_template
app = Flask(__name__)

mode = 'DEV'
# mode = 'PROD'

@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == "__main__":
    if mode == 'DEV':
        app.run(host='0.0.0.0', debug=True)
    else:
        app.run(host='0.0.0.0:8080')