import { useState } from "react";
import InputBox from "./components/InputBox";
import Button from "./components/Button";
import "./index.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState("");

  const checkSpam = async () => {
    if (!text) return;
    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      setResult(data.prediction);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gradient-to-r from-green-500 to-emerald-900 p-4">
      <h1 className="text-3xl font-extrabold text-white mb-6 drop-shadow-lg">
        🚀 Spam Detector
      </h1>
      <InputBox text={text} setText={setText} />
      <Button onClick={checkSpam} />
      {result && (
        <p
          className={`mt-4 text-lg font-semibold ${
            result === "spam" ? "text-red-600" : "text-white"
          } bg-white/20 px-4 py-2 rounded-lg shadow-md`}
        >
          {result === "spam" ? "🚨 Spam Detected!" : "✅ Not Spam"}
        </p>
      )}
    </div>
  );
}

export default App;
