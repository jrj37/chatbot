import React from "react";
import Message from "./Message";
import { chatBoxStyle, emptyMessageStyle } from "../styles/styles";

const ChatBox = ({ messages }) => {
  return (
    <div style={chatBoxStyle}>
      {messages.length === 0 && <p style={emptyMessageStyle}>Aucun message</p>}
      {messages.map((msg, idx) => (
        <Message text={msg.text} fromUser={msg.fromUser} />

      ))}
    </div>
  );
};

export default ChatBox;

