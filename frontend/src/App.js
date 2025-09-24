import React, { useState } from "react";
import ChatBox from "./components/ChatBox";
import ChatInput from "./components/ChatInput";

const sendPromptToAgent = async (prompt) => {
  try {
    const response = await fetch(`http://backend:8000/agent?prompt=${encodeURIComponent(prompt)}`);
    if (!response.ok) throw new Error("Erreur API");
    const data = await response.json();
    return data.response;
  } catch (error) {
    console.error("Erreur lors de l'appel à l'agent :", error);
    return `Erreur du chatbot : ${error.message}`;
  }
};

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (input.trim() === "") return;

    // Ajouter message utilisateur
    setMessages((prev) => [...prev, { text: input.trim(), fromUser: true }]);
    setInput("");

    // Appeler API backend
    const response = await sendPromptToAgent(input.trim());

    // Ajouter réponse bot
    setMessages((prev) => [...prev, { text: response, fromUser: false }]);
  };

  return (
    <div
      style={{
        height: "100vh",
        display: "flex",
        flexDirection: "column",
        fontFamily:
          '-apple-system, BlinkMacSystemFont, "San Francisco", "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
        backgroundColor: "#f0f4ff",
        color: "#3b4291",
      }}
    >
      <header
        style={{
          padding: "16px 0",
          textAlign: "center",
          borderBottom: "none",
        }}
      >
        <h1
          style={{
            margin: 0,
            fontSize: "24px",
            fontWeight: 700,
            color: "#3b4291",
            textShadow: "0 1px 4px rgba(255, 255, 255, 0.6)",
          }}
        >
          TW3partner Chat
        </h1>
      </header>
      <main
        style={{
          flex: 1,
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          padding: "20px",
          maxWidth: 800,
          margin: "0 auto",
          width: "100%",
        }}
      >
        <ChatBox messages={messages} />
        <ChatInput input={input} setInput={setInput} sendMessage={sendMessage} />
      </main>
    </div>
  );
}

export default App;