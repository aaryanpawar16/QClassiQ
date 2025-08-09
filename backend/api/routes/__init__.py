from .predict import predict_bp
from .metrics import metrics_bp
from .circuit import circuit_bp

def register_routes(app):
    app.register_blueprint(predict_bp, url_prefix="/")
    app.register_blueprint(metrics_bp, url_prefix="/")
    app.register_blueprint(circuit_bp, url_prefix="/")
