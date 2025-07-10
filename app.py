from flask import Flask, render_template, jsonify
from scraper.steam_data import famous__games

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/famous')
def famous():
    return jsonify(famous__games())

if __name__ == '__main__':
    app.run(debug=True)