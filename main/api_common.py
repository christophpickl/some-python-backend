from flask import request, Response
from flask import Blueprint

api_common_bp = Blueprint("api_common", __name__)


@api_common_bp.after_app_request
def add_header(response: Response):
    if 'debug' in request.args:
        response.headers['magic-flask'] = 'foobar'
    return response


@api_common_bp.app_errorhandler(404)
def page_not_found(code_or_exception):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
