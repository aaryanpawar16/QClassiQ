import pennylane as qml
from pennylane import numpy as np
import torch
from torch import nn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import TensorDataset, DataLoader
import joblib
from tqdm import tqdm

# Set up quantum device
n_qubits = 4
try:
    dev = qml.device("qiskit.aer", wires=n_qubits)
except Exception:
    print("⚠️ qiskit.aer not available. Using default.qubit.")
    dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev, interface="torch")
def quantum_circuit(inputs):
    for i in range(n_qubits):
        qml.RY(inputs[i], wires=i)
    for i in range(n_qubits - 1):
        qml.CNOT(wires=[i, i + 1])
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]

# Hybrid Model Definition
class HybridModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.pre_net = nn.Sequential(
            nn.Linear(4, 4),
            nn.ReLU()
        )
        self.post_net = nn.Sequential(
            nn.Linear(8, 4),
            nn.ReLU(),
            nn.Linear(4, 3)
        )

    def forward(self, x):
        q_outs = []
        for sample in x:
            q_result = quantum_circuit(sample)
            q_outs.append(torch.tensor(q_result, dtype=torch.float32))
        q_out = torch.stack(q_outs).to(x.device)  # Ensure q_out is on the same device
        x_classical = self.pre_net(x)
        x_combined = torch.cat((x_classical, q_out), dim=1)
        return self.post_net(x_combined)

# Main training block
if __name__ == "__main__":
    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Preprocessing
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    joblib.dump(scaler, "scaler.pkl")  # Save for Streamlit

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    X_train_tensor = torch.tensor(X_train, dtype=torch.float32).to(device)
    y_train_tensor = torch.tensor(y_train, dtype=torch.long).to(device)
    X_test_tensor = torch.tensor(X_test, dtype=torch.float32).to(device)
    y_test_tensor = torch.tensor(y_test, dtype=torch.long).to(device)

    train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
    train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)

    model = HybridModel().to(device)
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    # Training loop
    epochs = 20
    for epoch in range(epochs):
        model.train()
        epoch_loss = 0.0
        for X_batch, y_batch in tqdm(train_loader, desc=f"Epoch {epoch+1}", leave=False):
            optimizer.zero_grad()
            predictions = model(X_batch)
            loss = loss_fn(predictions, y_batch)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
        print(f"Epoch {epoch+1} - Loss: {epoch_loss / len(train_loader):.4f}")

    torch.save(model.state_dict(), "hybrid_model.pt")
    print("✅ Model saved as 'hybrid_model.pt'")

    # Evaluation
    model.eval()
    with torch.no_grad():
        test_preds = model(X_test_tensor)
        predicted = torch.argmax(test_preds, dim=1)
        accuracy = (predicted == y_test_tensor).float().mean()
        print(f"\n🎯 Test Accuracy: {accuracy.item():.4f}")
