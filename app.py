from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/incidents', methods=['GET','POST'])
def incidents():
    if request.method == 'GET':
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
    elif request.method == 'POST':
            data = request.json
            return jsonify(data)
            
    return jsonify(incident)

if __name__=="__main__": 
    app.run(debug=True)
