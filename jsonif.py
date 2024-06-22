from flask import Flask, request, jsonify
from flask import SSLify

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/secure-endpoint', methods=['POST'])
def secure_endpoint():
    data = request.json
    return jsonify({"message": "Secure data received"}), 200

if __name__ == '__main__':
    app.run(ssl_context='adhoc')