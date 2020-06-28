from flask import Blueprint, jsonify

from .dependencies import Dependencies

api_bp = Blueprint("api", __name__)


@api_bp.route("/", methods=['GET'])
def home():
    return "<h1>hello flask</h1>"


@api_bp.route('/api/v1/books', methods=['GET'])
def get_books():
    return jsonify(Dependencies.bookService().all())
