# QClassiQ - Hybrid Quantum-Classical ML Model 🧠⚛️

QClassiQ is a hybrid machine learning model that combines the strengths of **quantum computing** (via PennyLane) and **classical deep learning** (via PyTorch) to classify the famous **Iris flower dataset**.

Trained over 20 epochs, QClassiQ achieves an impressive **93.3% accuracy**, outperforming several baseline models — while using **fewer parameters**.

---

## 🌟 Features

- 🧬 Quantum Circuit using PennyLane with 4 qubits
- 🔗 Classical Neural Network layers for feature fusion
- ⚗️ Quantum-Classical hybrid training loop
- 📊 Trained on Iris dataset (3-class classification)
- 🧠 Achieves >93% test accuracy
- 📈 Live Demo with **Streamlit**
- 🎥 AI-generated explainer video support

---

## 🚀 Getting Started

1. Clone the repo

git clone https://github.com/aaryanpawar16/QClassiQ.git
cd QClassiQ

2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

3. Install dependencies
pip install -r requirements.txt
🧪 Run the Model
python qclassiq.py
💡 Run Streamlit App
streamlit run app.py

📂 Project Structure

QClassiQ/

├── qclassiq.py          # Hybrid model training script

├── app.py               # Streamlit UI

├── scaler.pkl           # Saved StandardScaler

├── hybrid_model.pt      # Trained PyTorch model

├── requirements.txt     # Dependencies

└── README.md

✨ Credits
Built with PennyLane, PyTorch, Streamlit

Developed by Aaryan Pawar
