from flask import Blueprint, jsonify

metrics_bp = Blueprint("metrics", __name__)

@metrics_bp.route("/metrics", methods=["GET"])
def get_metrics():
    metrics = {
        "epochs": list(range(1, 11)),
        "accuracy": [0.6, 0.68, 0.71, 0.75, 0.78, 0.8, 0.82, 0.83, 0.84, 0.85]
    }
    return jsonify(metrics)
