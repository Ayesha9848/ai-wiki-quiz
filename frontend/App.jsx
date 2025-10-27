import GenerateQuiz from "./components/GenerateQuiz";
export default function App() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold text-center mb-6">
        🧠 AI Wiki Quiz Generator
      </h1>
      <GenerateQuiz />
    </div>
  );
}
