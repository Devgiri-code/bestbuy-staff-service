from flask import Flask, jsonify, request
import uuid
import os

app = Flask(__name__)

# In-memory storage for staff information
staff_data = {}

# Root route for the application
@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to the Staff-Service API!",
        "endpoints": {
            "POST /staff": "Create a new staff member",
            "GET /staff": "Retrieve all staff members",
            "GET /staff/<staff_id>": "Retrieve a specific staff member",
            "PUT /staff/<staff_id>": "Update a staff member",
            "DELETE /staff/<staff_id>": "Delete a staff member"
        }
    }), 200

# Handle favicon.ico requests
@app.route('/favicon.ico')
def favicon():
    return '', 204

# Create staff member
@app.route('/staff', methods=['POST'])
def create_staff():
    data = request.json
    staff_id = str(uuid.uuid4())  # Generate a unique ID
    staff_data[staff_id] = {
        'id': staff_id,
        'name': data.get('name'),
        'position': data.get('position'),
        'department': data.get('department'),
        'email': data.get('email'),
        'phone': data.get('phone')
    }
    return jsonify({'message': 'Staff created successfully', 'staff': staff_data[staff_id]}), 201

# Retrieve all staff members
@app.route('/staff', methods=['GET'])
def get_all_staff():
    return jsonify(list(staff_data.values())), 200

# Retrieve a single staff member
@app.route('/staff/<staff_id>', methods=['GET'])
def get_staff(staff_id):
    staff = staff_data.get(staff_id)
    if not staff:
        return jsonify({'error': 'Staff not found'}), 404
    return jsonify(staff), 200

# Update a staff member
@app.route('/staff/<staff_id>', methods=['PUT'])
def update_staff(staff_id):
    if staff_id not in staff_data:
        return jsonify({'error': 'Staff not found'}), 404
    data = request.json
    staff_data[staff_id].update({
        'name': data.get('name', staff_data[staff_id]['name']),
        'position': data.get('position', staff_data[staff_id]['position']),
        'department': data.get('department', staff_data[staff_id]['department']),
        'email': data.get('email', staff_data[staff_id]['email']),
        'phone': data.get('phone', staff_data[staff_id]['phone'])
    })
    return jsonify({'message': 'Staff updated successfully', 'staff': staff_data[staff_id]}), 200

# Delete a staff member
@app.route('/staff/<staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    if staff_id not in staff_data:
        return jsonify({'error': 'Staff not found'}), 404
    del staff_data[staff_id]
    return jsonify({'message': 'Staff deleted successfully'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
