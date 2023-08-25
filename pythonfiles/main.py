from flask import Flask, request, jsonify, send_file
from chatbot import process_query
from recommendation import recommend, temparatue
from flask_cors import CORS
from dashboard import add_model_to_room, add_room, makeProblem

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def other_routes():
    return jsonify({
        'message': "you are not allowed to access.",
    })


@app.route('/fetchData', methods=['GET', 'POST'])
def fetch():
    return send_file('rooms.json', mimetype='application/json')


@app.route('/addRoom', methods=['GET', 'POST'])
def addRoom():
    size = request.args.get('size')
    add_room(size)
    return jsonify({
        'message': "true",
    })


@app.route('/addACModel', methods=['GET', 'POST'])
def addACModel():
    model = request.args.get('model')
    roomname = request.args.get('temp')
    add_model_to_room(model, roomname)
    return jsonify({
        'message': "true",
    })


@app.route('/chatbot', methods=['GET'])
def get_chatbot_query():
    text = request.args.get('query')
    response = process_query(text)
    return jsonify({
        'response': response,
    })


@app.route('/recommend', methods=['GET'])
def get_recommend_ac():
    height, width, depth = list(
        map(float, request.args.get('size').split(" ")))
    lat, lon = list(map(float, request.args.get('location').split(" ")))
    return recommend(height, width, depth, lat, lon)


@app.route('/problem', methods=['GET'])
def problem():
    room = request.args.get('room')
    model = request.args.get('model')
    makeProblem(room, model)
    return jsonify({
        'message': "true",
    })


@app.route('/climate', methods=['GET'])
def climate():
    lat, lon = list(map(float, request.args.get('location').split(" ")))
    return jsonify({
        'celsius': (temparatue(lat, lon) - 32) * (5/9),
    })


if __name__ == '__main__':
    app.run(debug=True)
