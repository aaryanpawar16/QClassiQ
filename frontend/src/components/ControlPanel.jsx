const runQuantumModel = async () => {
  try {
    const response = await fetch("http://localhost:5000/run", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ qubits: 2, layers: 1 })
    });

    const data = await response.json();
    console.log("Backend response:", data);
  } catch (error) {
    console.error("Error calling backend:", error);
  }
};
