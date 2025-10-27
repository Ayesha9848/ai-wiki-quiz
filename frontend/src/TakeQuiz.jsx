import { useState } from "react";

export default function TakeQuiz({ quiz }) {
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);
  const [score, setScore] = useState(0);

  const handleSelect = (qIndex, opt) => {
    setAnswers({ ...answers, [qIndex]: opt });
  };

  const handleSubmit = () => {
    let s = 0;
    quiz.forEach((q, i) => {
      if (answers[i] === q.answer) s++;
    });
    setScore(s);
    setSubmitted(true);
  };

  return (
    <div className="mt-6">
      {quiz.map((q, i) => (
        <div key={i} className="p-4 border rounded-lg mb-4">
          <p className="font-semibold mb-2">{i + 1}. {q.question}</p>
          {q.options.map((opt, j) => (
            <label key={j} className="block mb-1">
              <input
                type="radio"
                name={`q-${i}`}
                disabled={submitted}
                onChange={() => handleSelect(i, opt)}
              />{" "}
              {opt}
            </label>
          ))}
          {submitted && (
            <p className={answers[i] === q.answer ? "text-green-600" : "text-red-600"}>
              {answers[i] === q.answer ? "✅ Correct" : `❌ Correct: ${q.answer}`}
            </p>
          )}
        </div>
      ))}
      {!submitted ? (
        <button
          onClick={handleSubmit}
          className="bg-green-600 text-white px-4 py-2 rounded-lg"
        >
          Submit Quiz
        </button>
      ) : (
        <div className="text-xl font-bold mt-4">
          Score: {score} / {quiz.length}
        </div>
      )}
    </div>
  );
}
