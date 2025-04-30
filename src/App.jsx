import { useState, useEffect } from 'react';
import './App.css';
import './index.css';

function App() {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState('');

  // Add greeting message when the component is mounted
  useEffect(() => {
    const initialMessage = {
      sender: 'bot',
      text: 'Automated Greeting message.',
    };
    setMessages([initialMessage]);
  }, []);

  // Auto-scroll to bottom when messages update
  useEffect(() => {
    const endDiv = document.getElementById('end-of-chat');
    if (endDiv) {
      endDiv.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages]);

  const handleSendMessage = () => {
    if (userInput.trim()) {
      setMessages([
        ...messages,
        { sender: 'user', text: userInput },
        { sender: 'bot', text: 'This is an automated response.' },
      ]);
      setUserInput('');
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">Mental Health Chatbot</div>
      <div className="chat-box">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`chat-message ${msg.sender === 'user' ? 'user' : 'bot'}`}
          >
            {msg.text}
          </div>
        ))}
        <div id="end-of-chat" />
      </div>
      <div className="chat-input-container">
        <textarea
          className="chat-input"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your message..."
        />
        <button className="chat-submit" onClick={handleSendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}

export default App;
