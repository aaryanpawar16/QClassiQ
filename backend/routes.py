from flask import Blueprint, request, jsonify

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/run", methods=["POST"])
@predict_bp.route("/circuit", methods=["POST"])  # alias route
def run_model():
    data = request.get_json()
    qubits = data.get("qubits")
    layers = data.get("layers")
    # Dummy response
    return jsonify({
        "status": "success",
        "message": f"Ran quantum model with {qubits} qubits and {layers} layers.",
        "output": [0.5, 0.5]
    })
