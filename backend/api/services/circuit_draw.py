from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer
from io import BytesIO
import base64
import numpy as np

def generate_circuit_image():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.ry(np.pi/4, 0)
    qc.ry(np.pi/4, 1)

    img = circuit_drawer(qc, output='mpl', style='iqx', scale=0.8)
    buffer = BytesIO()
    img.savefig(buffer, format='png')
    buffer.seek(0)
    encoded = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    return encoded
