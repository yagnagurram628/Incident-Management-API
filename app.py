from flask import Flask, jsonify, request
app = Flask(__name__)

incident = [{
            'id': 1,
            'title': "Payment",
            'severity': "HIGH"
        },
        {
            'id': 2,
            'title': "Server",
            'severity': "CRITICAL"
        },
        {
            'id': 3,
            'title': "Backend",
            'severity': "LOW"
        }]

@app.route('/incidents', methods=['GET','POST'])
def incidents():
    if request.method == 'GET':
        return jsonify(incident)
    elif request.method == 'POST':
        data = request.json
        data['id'] = len(incident) + 1
        incident.append(data)
        return jsonify(data)

@app.route('/incidents/<id>', methods = ['GET'])
def idfetch(id):
    id = int(id)
    for i in incident:
        if id == i['id']:
            return jsonify(i)
        
    error = {
        "error": "Incident not found"
    }
    return jsonify(error), 404

@app.route('/incidents/<id>', methods = ['PUT'])
def update(id):
    id=int(id)
    data = request.json
    for i in incident:
        if id == i['id']:
            i['title'] = data['title']
            i['severity'] = data['severity']
            return jsonify(i)

    error = {
        "error": "Incident not found"
    }
    return jsonify(error), 404

@app.route('/incidents/<id>', methods = ['DELETE'])
def delete(id):
    id=int(id)
    for i in incident:
        if id == i['id']:
            index = incident.index(i)
            incident.pop(index)
            return jsonify({
                "message": "Incident deleted successfully"
            })

    error = {
        "error": "Incident not found"
    }
    return jsonify(error), 404

if __name__=="__main__": 
    app.run(debug=True)
