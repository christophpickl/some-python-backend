from flask import Blueprint, jsonify

from .logic import BookService, InMemoryBookRepository

api_bp = Blueprint("api", __name__)

books = BookService(InMemoryBookRepository())


@api_bp.route("/", methods=['GET'])
def home():
    return "<h1>hello flask</h1>"


@api_bp.route('/api/v1/books', methods=['GET'])
def get_books():
    return jsonify(books.all())

