import { useState } from "react";
import Header from "./components/Header";
import RepoInput from "./components/RepoInput";
import ResultPanel from "./components/ResultPanel";
import { analyzeRepo } from "./services/api";
import "./App.css";

function App() {
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async (repoUrl) => {
    setLoading(true);
    setResult("");

    try {
      const data = await analyzeRepo(repoUrl, "structure", "developer");
      setResult(data.story || JSON.stringify(data));
    } catch (err) {
      setResult("Error contacting backend.");
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <Header />
      <RepoInput onAnalyze={handleAnalyze} />
      <ResultPanel result={result} loading={loading} />
    </div>
  );
}

export default App;