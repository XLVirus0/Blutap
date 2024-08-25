from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data for valid licenses
valid_licenses = {
    "user1": "ABCD1234EFGH5678",
    "user2": "6MF6SNBH6HO99BMJ"
}

@app.route('/validate', methods=['POST'])
def validate_license():
    data = request.get_json()
    user_id = data.get('user_id')
    license_key = data.get('license_key')

    if valid_licenses.get(user_id) == license_key:
        return jsonify({"status": "valid"})
    else:
        return jsonify({"status": "invalid"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
