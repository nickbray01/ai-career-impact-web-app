from flask import Flask, jsonify, request
from flask_cors import CORS
from server.gptAccess import validateOccupation, fillParagraph
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()


# generic prompt input

# @app.route('/ask-ai', methods=['POST'])
# def question():
#     response_object = {'status': 'success'}
#     post_data = request.get_json()
#     query = post_data.get('prompt')
#     response_object['query'] = query
#     response_object['response'] = ask_ai(query)
#     print(response_object)
#     return jsonify(response_object)


# validate the occupation being entered by the user
@app.route('/validate-occupation', methods=['POST'])
def validate():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    occupation = post_data.get('occupation')
    response_object['query'] = 'validate job: ' + occupation
    response_object['response'] = validateOccupation(occupation)
    print(response_object)
    return jsonify(response_object)

# generate the data to fill a component of the report
@app.route('/fill-paragraph', methods=['POST'])
def paragraph():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    occupation = post_data.get('occupation')
    section = post_data.get('section')
    response_object['query'] = 'fill paragraph: ' + section + "for occupation: " + occupation
    response_object['response'] = fillParagraph(occupation, section)
    print(response_object)
    return jsonify(response_object)