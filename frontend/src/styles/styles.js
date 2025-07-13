// src/styles/styles.js

export const appContainer = {
  height: "100vh",
  display: "flex",
  flexDirection: "column",
  fontFamily: "Arial, sans-serif",
};

export const headerStyle = {
  padding: "20px",
  textAlign: "center",
  borderBottom: "1px solid #ccc",
};

export const mainStyle = {
  flex: 1,
  display: "flex",
  flexDirection: "column",
  justifyContent: "space-between",
  padding: "20px",
  maxWidth: 800,
  margin: "0 auto",
  width: "100%",
};

export const chatBoxStyle = {
  flex: 1,
  borderRadius: 12,
  padding: 12,
  overflowY: "auto",
  backgroundColor: "rgba(240, 244, 255, 0.8)", // fond clair bleuté
  boxShadow: "0 2px 8px rgba(90, 99, 179, 0.2)", // ombre douce assortie au dégradé
  marginBottom: 12,
  display: "flex",
  flexDirection: "column",
};


export const emptyMessageStyle = {
  color: "#888",
};

export const messageStyle = {
  backgroundColor: "#e1ffc7",
  padding: "8px 12px",
  borderRadius: 15,
  marginBottom: 8,
  maxWidth: "70%",
  alignSelf: "flex-start",
};

export const chatInputContainer = {
  display: "flex",
};

export const inputStyle = {
  flex: 1,
  padding: "10px 14px",
  fontSize: 16,
  borderRadius: 20,
  border: "1.5px solid #5a63b3ff",
  outline: "none",
  fontFamily:
    '-apple-system, BlinkMacSystemFont, "San Francisco", "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
  color: "#3b4291",
  backgroundColor: "white",
  boxShadow: "0 1px 3px rgba(90, 99, 179, 0.2)",
  transition: "border-color 0.3s ease, box-shadow 0.3s ease",
  marginRight: "8px", // <-- ajoute cet espace ici
};


export const inputFocusStyle = {
  borderColor: "#35408f",
  boxShadow: "0 0 8px rgba(53, 64, 143, 0.6)",
};
export const buttonStyle = {
  padding: "10px 16px",
  fontSize: 16,
  borderRadius: 5,
  border: "none",
  backgroundColor: "#5a63b3ff", // bleu/violet foncé, comme la bulle utilisateur
  color: "white",
  cursor: "pointer",
  transition: "background-color 0.3s ease",
};

export const buttonHoverStyle = {
  backgroundColor: "#454f9cff", // légèrement plus foncé au hover
};
