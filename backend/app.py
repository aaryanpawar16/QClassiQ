import sys
import os

# This adds the 'backend' directory to Python's path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS
# This import is now updated to match your new file structure
from api.routes.predict import predict_bp 

app = Flask(__name__)
CORS(app)

app.register_blueprint(predict_bp)

if __name__ == "__main__":
    app.run(debug=True)
