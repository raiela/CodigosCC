from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from uuid import uuid4
from flask_uuid import FlaskUUID

app = Flask(__name__)
FlaskUUID(app)

casters = [
    {
        'id': uuid4(),
        'nome': 'Bida',
        'disponibilidade': 'Segunda-Terca-'
    },
    {
        'id': uuid4(),
        'nome': 'Raiela',
        'disponibilidade': 'Terca-Quarta'
    },
]

@app.route('/casters', methods=['GET'])
def get_casters():
    return jsonify({'casters': casters})

@app.route('/casters', methods=['POST'])
def add_caster():
    if not request.json or not 'disponibilidade' in request.json and not 'nome' in request.json:
        abort(400)
    caster = {
        'id': uuid4(),
        'nome': request.json['nome'],
        'disponibilidade': request.json['disponibilidade'],
    }
    casters.append(caster)
    return jsonify({'caster': caster}), 201

@app.route('/casters/<uuid:casterId>', methods=['GET'])
def get_caster_byId(casterId):
    result = [result for result in casters if result['id'] == casterId]
    if len(result) == 0:
        abort(404)
    return jsonify({'caster': result[0]})

@app.route('/casters/<uuid:casterId>', methods=['DELETE'])
def delete_caster(casterId):
    result = [result for result in casters if result['id'] == casterId]
    if len(result) == 0:
        abort(404)
    casters.remove(result[0])
    return jsonify({'result': True})

@app.route('/casters/<uuid:casterId>', methods=['PUT'])
def update_caster(casterId):
    result = [result for result in casters if result['id'] == casterId]
    if len(result) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if ('nome' in request.json and type(request.json['nome']) != str) or ('disponibilidade' in request.json and type(request.json['disponibilidade']) is int):
        abort(400)
    
    result[0]['nome'] = request.json.get('nome', result[0]['nome'])
    result[0]['disponibilidade'] = request.json.get('disponibilidade', result[0]['disponibilidade'])
    return jsonify({'caster': result[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Resource not found'}), 404)

if __name__ == "__main__":
    print("Server live in port:5000")
    app.run(host='0.0.0.0', debug=True)