import { useState } from "react";
import TakeQuiz from "./TakeQuiz";

export default function GenerateQuiz() {
  const [url, setUrl] = useState("");
  const [quiz, setQuiz] = useState(null);

  const handleGenerate = async () => {
    const res = await fetch("http://127.0.0.1:8000/generate_quiz/?url=" + url, {
      method: "POST",
    });
    const data = await res.json();
    setQuiz(data.quiz);
  };

  return (
    <div className="max-w-2xl mx-auto">
      <input
        type="text"
        placeholder="Enter Wikipedia URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="border w-full p-2 rounded-lg mb-4"
      />
      <button
        onClick={handleGenerate}
        className="bg-blue-600 text-white px-4 py-2 rounded-lg"
      >
        Generate Quiz
      </button>
      {quiz && <TakeQuiz quiz={quiz} />}
    </div>
  );
}
