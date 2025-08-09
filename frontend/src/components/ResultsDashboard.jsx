import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { Cpu, BrainCircuit, Scale, BarChart2, Zap } from 'lucide-react';

const ResultsDashboard = ({ analysisData, optunaResult, isRunning }) => {
    const { results, xai } = analysisData;
    const renderSkeleton = () => <div className="animate-pulse h-64 bg-gray-700/50 rounded-md"></div>;

    return (
        <div className="bg-white/10 backdrop-blur-md rounded-2xl p-6 shadow-lg border border-white/20 mt-8">
            <h2 className="text-2xl font-bold mb-6 flex items-center"><BarChart2 className="mr-3" />Results</h2>
            <div className="grid lg:grid-cols-2 gap-8">
                {/* Analysis Table */}
                <div>
                    <h3 className="text-xl font-semibold mb-4 flex items-center"><Scale className="mr-2" />Comparative Analysis</h3>
                    {isRunning && !results.length ? renderSkeleton() : (
                        <table className="w-full text-left">
                            <thead>
                                <tr className="text-white/70">
                                    <th className="p-2">Model</th><th>Accuracy</th><th>F1-Score</th><th>Params</th>
                                </tr>
                            </thead>
                            <tbody>
                                {results.map(res => (
                                    <tr key={res.name} className={`border-t border-white/20 ${res.name === 'QClassiQ Hybrid' ? 'text-cyan-300' : ''}`}>
                                        <td className="p-2 flex items-center">{res.name === 'QClassiQ Hybrid' ? <BrainCircuit className="mr-2"/> : <Cpu className="mr-2"/>}{res.name}</td>
                                        <td>{res.accuracy}</td><td>{res.f1}</td><td>{res.params}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    )}
                </div>
                {/* Feature Importance Chart */}
                <div>
                    <h3 className="text-xl font-semibold mb-4 flex items-center"><BrainCircuit className="mr-2" />Feature Importance (XAI)</h3>
                    <div className="h-64">
                        {isRunning && !xai.length ? renderSkeleton() : (
                            <ResponsiveContainer width="100%" height="100%">
                                <BarChart data={xai} layout="vertical">
                                    <XAxis type="number" hide />
                                    <YAxis type="category" dataKey="name" stroke="white" width={80} />
                                    <Tooltip cursor={{fill: 'rgba(255,255,255,0.1)'}} contentStyle={{background: "#2d3748"}}/>
                                    <Bar dataKey="importance" fill="#4dd0e1" />
                                </BarChart>
                            </ResponsiveContainer>
                        )}
                    </div>
                </div>
                {/* Optuna Results */}
                <div className="lg:col-span-2">
                    <h3 className="text-xl font-semibold mb-4 flex items-center"><Zap className="mr-2" />Hyperparameter Optimization</h3>
                    <div className="bg-black/20 p-4 rounded-lg text-center">
                        {isRunning && !optunaResult ? renderSkeleton() : optunaResult ? (
                            <div>
                                <p className="text-lg">Best Accuracy: <span className="font-bold text-2xl text-purple-300">{(optunaResult.best_accuracy * 100).toFixed(2)}%</span></p>
                                <p className="text-gray-400 mt-2">Found with {optunaResult.best_layers} layers and a learning rate of {optunaResult.best_lr}</p>
                            </div>
                        ) : <p className="text-gray-400">Run optimization to see results.</p>}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ResultsDashboard;
