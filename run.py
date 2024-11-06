from time import sleep
from flask import Flask, request, jsonify
from app.adapters.postgresql_adapter import PostgresqlAdapter
from app.application.services import UserService
from app.adapters.postgresql_adapter import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

sleep(10)

db.init_app(app)

with app.app_context():
    db.create_all()

user_service = UserService(user_port=PostgresqlAdapter())

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email})
    return jsonify({'error': 'User not found'}), 404

@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    user = user_service.create_user(data['username'], data['email'])
    return jsonify({"id": user.id, 'username': user.username, 'email': user.email}), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)