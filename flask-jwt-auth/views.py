from run import app
from flask import jsonify


@app.route('/')
def index():
    return jsonify({'message': 'Demo Page 1.0.5'})
