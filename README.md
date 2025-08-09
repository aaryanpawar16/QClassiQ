QClassiQ - The Interactive Quantum Simulator
QClassiQ is an intuitive, web-based platform that demystifies quantum computing by allowing users to visually build, simulate, and understand quantum circuits in real-time, right from their browser.

Watch Demo on YouTube:
(QClassiQ)[https://youtu.be/iuT6PGkJWz4]

🚀 About The Project
Quantum computing holds the promise of solving some of the world's most complex problems, but its steep learning curve creates a significant barrier to entry. Aspiring developers and researchers often get bogged down by complex mathematics and boilerplate code before they can even run a simple experiment.

QClassiQ was built to break down this barrier. We've replaced intimidating lines of code with a clean, interactive graphical interface, making the fundamental concepts of quantum mechanics—like superposition and entanglement—accessible to everyone.

Our mission is to empower the next generation of quantum innovators by providing a tool that is not only powerful but also a joy to use.

✨ Key Features
Interactive Circuit Builder: Visually design quantum circuits by selecting gates from a simple dropdown menu for each qubit and layer.

Real-Time Quantum Simulation: Run your circuits on a high-performance backend powered by Qiskit's Aer Simulator to see the probabilistic outcomes of your quantum experiments.

Dynamic Visualization: Instantly view both the quantum circuit diagram you've built and a bar chart of the simulation results, providing clear, immediate feedback.

Seamless Frontend-Backend Integration: A modern React frontend communicates smoothly with a robust Flask backend API.

🛠️ Tech Stack
Frontend
React.js: For building a fast and responsive user interface.

Vite: As the next-generation build tool for a rapid development experience.

Recharts: For creating beautiful and interactive data visualizations.

CSS with Flexbox & Grid: For modern, responsive layouts and custom styling.

Backend
Flask: A lightweight and powerful Python web framework for our API.

Qiskit: The leading open-source quantum computing software development kit.

Matplotlib: For generating high-quality visualizations of quantum circuits.

Flask-CORS: To handle cross-origin requests from the frontend.

🏁 Getting Started
To get a local copy up and running, follow these simple steps.

Prerequisites
Node.js & npm: Make sure you have Node.js (which includes npm) installed. You can download it here.

Python: Make sure you have Python (version 3.8 or newer) and pip installed. You can download it here.

⚙️ Installation & Setup
Clone the repository:

git clone https://github.com/aaryanpawar16/QClassiQ.git
cd QClassiQ

Setup the Backend:

Navigate to the backend directory:

cd backend

Create and activate a virtual environment:

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install the required Python packages:

pip install -r requirements.txt

Setup the Frontend:

In a new terminal window, navigate to the frontend directory:

cd frontend

Install the required npm packages:

npm install

▶️ Running the Application
You need to have both the backend and frontend servers running simultaneously in their separate terminals.

Start the Backend Server:

In your backend terminal (from the backend directory):

python app.py

The server should now be running on http://127.0.0.1:5000.

Start the Frontend Server:

In your frontend terminal (from the frontend directory):

npm run dev

The application should automatically open in your browser at http://localhost:5173.

License
Distributed under the MIT License. See LICENSE for more information.
