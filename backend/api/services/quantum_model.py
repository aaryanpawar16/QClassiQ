def run_quantum_model(qubits, layers):
    print(f"Running quantum model with qubits={qubits}, layers={layers}")
    try:
        # TEMP DUMMY OUTPUT FOR DEBUGGING
        return [0.5, 0.3, 0.2]
        
        # If you have real quantum code, wrap it in try/except:
        # result = quantum_circuit(qubits, layers)
        # return result

    except Exception as e:
        print("Quantum circuit error:", str(e))
        return None
