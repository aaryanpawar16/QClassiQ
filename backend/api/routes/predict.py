import matplotlib
matplotlib.use('Agg')

import io
import base64
from flask import Blueprint, request, jsonify
from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer
from qiskit_aer import AerSimulator

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/run", methods=["POST"])
def run_quantum_model():
    try:
        data = request.get_json()
        qubits = int(data.get("qubits", 2))
        # The 'gates' parameter is a 2D array of gate selections from the frontend
        gate_grid = data.get("gates", [])

        if not gate_grid or not gate_grid[0]:
            return jsonify({"message": "Gate layout is missing or invalid.", "status": "error"}), 400

        layers = len(gate_grid)
        
        # --- Build the circuit dynamically based on frontend input ---
        qc = QuantumCircuit(qubits)
        for layer_index in range(layers):
            for qubit_index in range(qubits):
                gate = gate_grid[layer_index][qubit_index]
                if gate == 'h':
                    qc.h(qubit_index)
                elif gate == 'x':
                    qc.x(qubit_index)
                elif gate == 'cnot' and qubit_index < qubits - 1:
                    # Apply CNOT with control on current qubit and target on the next
                    qc.cx(qubit_index, qubit_index + 1)
                # Add more gates here as needed (e.g., 'y', 'z', 'ry', etc.)
            qc.barrier() # Add a barrier for visual separation between layers

        # --- Simulate the circuit ---
        # Add measurement gates to get the outcome
        qc.measure_all()

        # Use the AerSimulator
        simulator = AerSimulator()
        # Run the simulation
        result = simulator.run(qc, shots=1024).result()
        # Get the measurement counts
        counts = result.get_counts(qc)

        # Format counts for the recharts library on the frontend
        # e.g., {'00': 512, '11': 512} -> [{'name': '00', 'probability': 50.0}, ...]
        total_shots = sum(counts.values())
        simulation_results = [
            {"name": state, "probability": (count / total_shots) * 100}
            for state, count in counts.items()
        ]

        # --- Draw the circuit image ---
        # We remove the measurement bits from the drawing for a cleaner look
        qc.remove_final_measurements()
        figure = circuit_drawer(qc, output='mpl', style='iqx', fold=-1)
        
        image_stream = io.BytesIO()
        figure.savefig(image_stream, format='png', bbox_inches='tight')
        image_stream.seek(0)
        encoded_image = base64.b64encode(image_stream.read()).decode("utf-8")

        return jsonify({
            "message": f"Successfully simulated a {qubits}-qubit circuit.",
            "status": "success",
            "circuit_image": f"data:image/png;base64,{encoded_image}",
            "simulation_results": simulation_results
        })

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({
            "message": "Error running quantum simulation.",
            "error": str(e),
            "status": "error"
        }), 500
