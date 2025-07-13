import React from "react";

const Message = ({ text, fromUser }) => {
  const styleUser = {
    backgroundColor: "#5a63b3ff",
    color: "white",
    padding: "8px 14px",
    borderRadius: "18px 18px 0 18px",
    marginBottom: 8,
    maxWidth: "70%",
    alignSelf: "flex-end",
    wordBreak: "break-word",
  };

  const styleBot = {
    backgroundColor: "#e9efff",
    color: "#3b4291",
    padding: "8px 14px",
    borderRadius: "18px 18px 18px 0",
    marginBottom: 8,
    maxWidth: "70%",
    alignSelf: "flex-start",
    wordBreak: "break-word",
  };

  return <div style={fromUser ? styleUser : styleBot}>{text}</div>;
};

export default Message;

