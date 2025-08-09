import { useState, useEffect } from "react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Cell } from 'recharts';
import { Cpu, Zap, SlidersHorizontal, BarChart2 } from 'lucide-react';
import './App.css';

const GATE_OPTIONS = [
  { value: 'i', label: 'Identity' },
  { value: 'h', label: 'Hadamard' },
  { value: 'x', label: 'Pauli-X' },
  { value: 'cnot', label: 'CNOT' },
];

const COLORS = ['#8884d8', '#82ca9d', '#ffc658', '#ff8042', '#0088FE', '#00C49F', '#FFBB28', '#FF8042'];

export default function QuantumSimulator() {
  const [qubits, setQubits] = useState(2);
  const [layers, setLayers] = useState(1);
  const [gateGrid, setGateGrid] = useState([]);
  
  const [circuitImage, setCircuitImage] = useState(null);
  const [simulationResults, setSimulationResults] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  // Initialize or update the gate grid when qubits or layers change
  useEffect(() => {
    setGateGrid(
      Array(layers).fill(null).map(() => 
        Array(qubits).fill('i') // Default to Identity gate
      )
    );
  }, [qubits, layers]);

  const handleGateChange = (layerIndex, qubitIndex, gate) => {
    const newGrid = [...gateGrid];
    newGrid[layerIndex][qubitIndex] = gate;
    setGateGrid(newGrid);
  };

  const runSimulation = async () => {
    setLoading(true);
    setMessage("");
    setCircuitImage(null);
    setSimulationResults(null);

    try {
      const res = await fetch("http://localhost:5000/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ qubits, layers, gates: gateGrid }),
      });

      const data = await res.json();

      if (data.status === "success") {
        setMessage(data.message);
        setCircuitImage(data.circuit_image);
        setSimulationResults(data.simulation_results);
      } else {
        setMessage(data.message || "Something went wrong.");
      }
    } catch (err) {
      setMessage("Server error. Could not connect to the backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header>
        <Zap className="logo-icon" />
        <h1>QClassiQ Simulator</h1>
      </header>
      
      {/* --- CONTROLS --- */}
      <div className="controls-card">
        <h2 className="card-title"><SlidersHorizontal size={20} /> Controls</h2>
        <div className="input-section">
          <label>
            Qubits:
            <input type="number" min="1" max="5" value={qubits} onChange={(e) => setQubits(Number(e.target.value))} />
          </label>
          <label>
            Layers:
            <input type="number" min="1" max="8" value={layers} onChange={(e) => setLayers(Number(e.target.value))} />
          </label>
        </div>
        <button onClick={runSimulation} disabled={loading} className="run-button">
          {loading ? "Simulating..." : "Run Simulation"}
        </button>
      </div>

      {/* --- CIRCUIT BUILDER --- */}
      <div className="builder-card">
        <h2 className="card-title"><Cpu size={20} /> Circuit Builder</h2>
        <div className="gate-grid">
          {gateGrid.map((layer, layerIndex) => (
            <div key={layerIndex} className="gate-layer">
              <div className="layer-label">L{layerIndex + 1}</div>
              {layer.map((gate, qubitIndex) => (
                <div key={qubitIndex} className="gate-qubit-wrapper">
                  <span className="qubit-label">q<sub>{qubitIndex}</sub></span>
                  <select
                    value={gate}
                    onChange={(e) => handleGateChange(layerIndex, qubitIndex, e.target.value)}
                    className="gate-select"
                  >
                    {GATE_OPTIONS.map(opt => (
                      <option key={opt.value} value={opt.value}>{opt.label}</option>
                    ))}
                  </select>
                </div>
              ))}
            </div>
          ))}
        </div>
      </div>
      
      {loading && (
        <div className="spinner-container">
          <div className="spinner"></div>
          <p>Running quantum simulation...</p>
        </div>
      )}

      {message && !loading && <p className="message">{message}</p>}

      {/* --- RESULTS --- */}
      <div className="results-container">
        {circuitImage && !loading && (
          <div className="output-section">
            <h3>Quantum Circuit</h3>
            <img src={circuitImage} alt="Quantum Circuit" className="circuit-img" />
          </div>
        )}

        {simulationResults && !loading && (
          <div className="output-section">
            <h3><BarChart2 size={20} /> Simulation Results</h3>
            <div style={{ width: '100%', height: 300 }}>
              <ResponsiveContainer>
                <BarChart data={simulationResults} margin={{ top: 20, right: 30, left: 0, bottom: 5 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#4A5568" />
                  <XAxis dataKey="name" stroke="#A0AEC0" />
                  <YAxis label={{ value: 'Probability (%)', angle: -90, position: 'insideLeft', fill: '#A0AEC0' }} stroke="#A0AEC0" />
                  <Tooltip
                    cursor={{ fill: 'rgba(113, 128, 150, 0.2)' }}
                    contentStyle={{ backgroundColor: '#1A202C', border: '1px solid #4A5568' }}
                  />
                  <Bar dataKey="probability" name="Probability" unit="%" fill="#8884d8">
                     {simulationResults.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                     ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
