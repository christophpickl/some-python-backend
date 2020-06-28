from flask import request, Flask

from .api_common import api_common_bp
from .api import api_bp

app = Flask(__name__)
app.config["DEBUG"] = True
app.register_blueprint(api_bp)
app.register_blueprint(api_common_bp)


if __name__ == "__main__":
    app.run()

