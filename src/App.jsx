import { useState, useEffect } from "react";
import "./App.css";
import "./index.css";

function App() {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState("");

  // Add greeting message when the component is mounted
  useEffect(() => {
    const initialMessage = {
      sender: "bot",
      text: "Automated Greeting message.", // Greeting message
    };
    setMessages([initialMessage]);
  }, []);

  const handleSendMessage = () => {
    if (userInput.trim()) {
      fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userInput }),
      })
        .then((res) => res.json())
        .then((data) => {
          setMessages((prevMessages) => [
            ...prevMessages,
            { sender: "user", text: userInput },
            { sender: "bot", text: data.response },
          ]);
        })
        .catch((error) => {
          setMessages((prevMessages) => [
            ...prevMessages,
            { sender: "user", text: userInput },
            { sender: "bot", text: "Sorry, something went wrong." },
          ]);
          console.error("Error:", error);
        });

      setUserInput("");
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault(); // Prevent default behavior (line break)
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
            className={`chat-message ${msg.sender === "user" ? "user" : "bot"}`}
          >
            {msg.text}
          </div>
        ))}
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
