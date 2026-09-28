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
            incident.append(data)
            return jsonify(data)

if __name__=="__main__": 
    app.run(debug=True)
