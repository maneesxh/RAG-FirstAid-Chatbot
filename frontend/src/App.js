import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import Footer from './Footer';
import ReactMarkdown from 'react-markdown';  // <-- import react-markdown

function App() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResponse(null);

    try {
      const res = await axios.post('http://127.0.0.1:8000/query', { user_input: input });
      setResponse(res.data);
    } catch (err) {
      setError('Something went wrong. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1 className="title">🩺 First Aid Chatbot</h1>

      <form onSubmit={handleSubmit} className="form-container">
        <textarea
          className="input-box"
          placeholder="Enter patient symptoms..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          rows="5"
        />
        <button type="submit" className="submit-button" disabled={loading}>
          {loading ? 'Processing...' : 'Get First Aid Advice'}
        </button>
      </form>

      {error && <div className="error">{error}</div>}

      {response && (
        <div className="response-box">
          <h2>First Aid Advice:</h2>
          <div className="answer-text">
            <ReactMarkdown>{response.answer}</ReactMarkdown>
          </div>
        </div>
      )}

      <Footer />
    </div>
  );
}

export default App;
