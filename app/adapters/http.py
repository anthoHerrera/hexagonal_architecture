from flask import Blueprint, jsonify, request
from app.application.user_service import UserService

bp = Blueprint("users", __name__)

@bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = UserService.create_user(data['name'], data['email'])
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 201

@bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = UserService.get_user(user_id=user_id)
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 200
    return jsonify({"error": "User not found"}), 404

@bp.route("/users", methods=["GET"])
def get_all_users():
    users = UserService.get_all_users()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users]), 200