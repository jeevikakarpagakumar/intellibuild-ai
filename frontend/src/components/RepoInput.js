import { useState } from "react";

export default function RepoInput({ onAnalyze }) {
  const [repo, setRepo] = useState("");

  return (
    <div className="input-box">
      <input
        placeholder="Paste GitHub repository URL"
        value={repo}
        onChange={(e) => setRepo(e.target.value)}
      />

      <button onClick={() => onAnalyze(repo)}>
        Analyze Repository
      </button>
    </div>
  );
}