from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/incidents', methods=['GET'])
def incidents():
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

    return jsonify(incident)

if __name__=="__main__":
    app.run(debug=True)
