import React, { useState } from "react";
import { chatInputContainer, buttonStyle, buttonHoverStyle, inputStyle, inputFocusStyle } from "../styles/styles";

const ChatInput = ({ input, setInput, sendMessage }) => {
  const [hover, setHover] = useState(false);
  const [isFocused, setIsFocused] = useState(false);

  const handleKeyPress = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  const combinedButtonStyle = {
    ...buttonStyle,
    ...(hover ? buttonHoverStyle : {}),
  };

  const combinedInputStyle = {
    ...inputStyle,
    ...(isFocused ? inputFocusStyle : {}),
  };

  return (
    <div style={chatInputContainer}>
      <input
        type="text"
        placeholder="Écrire un message..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyPress={handleKeyPress}
        style={combinedInputStyle}
        onFocus={() => setIsFocused(true)}
        onBlur={() => setIsFocused(false)}
      />
      <button
        onClick={sendMessage}
        style={combinedButtonStyle}
        onMouseEnter={() => setHover(true)}
        onMouseLeave={() => setHover(false)}
        aria-label="Envoyer message"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          viewBox="0 0 24 24"
        >
          <line x1="5" y1="12" x2="19" y2="12" />
          <polyline points="12 5 19 12 12 19" />
        </svg>
      </button>
    </div>
  );
};

export default ChatInput;

