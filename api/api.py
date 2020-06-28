import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>hello flask</h1>"


books = [
    {
        'id': 1,
        'title': 'Clean Code'
    },
    {
        'id': 2,
        'title': 'Pragmatic Programmer'
    }
]


@app.route('/api/v1/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.after_request
def add_header(response):
    if 'debug' in request.args:
        response.headers['magic-flask'] = 'foobar'
    return response


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404



app.run()

