from flask import Blueprint, jsonify
# This import path is corrected to reflect the new file structure
from api.services.circuit_draw import generate_circuit_image

circuit_bp = Blueprint("circuit", __name__)

@circuit_bp.route("/circuit-image", methods=["GET"])
def circuit_image():
    image_base64 = generate_circuit_image()
    return jsonify({"image": image_base64})
