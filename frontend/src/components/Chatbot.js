import React, { useState } from 'react';
import axios from 'axios';

function Chatbot() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponse(null);

    try {
      const res = await axios.post("http://127.0.0.1:8000/query", {
        user_input: input
      });
      setResponse(res.data);
    } catch (err) {
      setResponse({ error: err.message });
    }
    setLoading(false);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <textarea 
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Describe the patient's symptoms..."
          rows="5"
          cols="60"
        />
        <br />
        <button type="submit">Submit</button>
      </form>

      {loading && <p>Loading...</p>}

      {response && !response.error && (
        <div>
          <h2>Condition Inferred:</h2>
          <p>{response.condition}</p>
          <h2>First Aid Guidance:</h2>
          <pre style={{ whiteSpace: "pre-wrap" }}>{response.answer}</pre>
        </div>
      )}

      {response && response.error && (
        <p>Error: {response.error}</p>
      )}
    </div>
  );
}

export default Chatbot;
