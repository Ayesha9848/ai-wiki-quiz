export default function QuizCard({ question, options }) {
  return (
    <div>
      <h3>{question}</h3>
      <ul>
        {options.map((opt, i) => (
          <li key={i}>{opt}</li>
        ))}
      </ul>
    </div>
  );
}
