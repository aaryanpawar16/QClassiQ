import streamlit as st
import torch
import numpy as np
import joblib
import pennylane as qml
from qclassiq import HybridModel, quantum_circuit  # Make sure qclassiq.py is in the same folder

# Load scaler and model
scaler = joblib.load("scaler.pkl")

model = HybridModel()
model.load_state_dict(torch.load("hybrid_model.pt", map_location=torch.device("cpu")))
model.eval()

# Draw the circuit
draw_circuit = qml.draw(quantum_circuit)

# Streamlit UI
st.title("🌸 Iris Flower Predictor (Quantum + Classical)")
st.markdown("Enter flower measurements to classify it and visualize the quantum circuit.")

sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.8)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.3)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.3)

if st.button("🔍 Predict"):
    user_input = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    user_scaled = scaler.transform(user_input)
    input_tensor = torch.tensor(user_scaled, dtype=torch.float32)

    with torch.no_grad():
        prediction = model(input_tensor)
        predicted_class = torch.argmax(prediction, dim=1).item()

    iris_labels = ['Setosa', 'Versicolor', 'Virginica']
    st.success(f"🌼 Predicted Iris Class: **{iris_labels[predicted_class]}**")

    # 🎯 Show the quantum circuit for the input
    st.subheader("🔬 Quantum Circuit Visualization")
    circuit_diagram = draw_circuit(input_tensor[0])
    st.code(circuit_diagram, language='text')
