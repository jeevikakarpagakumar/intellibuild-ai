export default function ResultPanel({ result, loading }) {
    if (loading) return <p className="loading">Analyzing repository...</p>;
  
    return (
      <div className="result-panel">
        <pre>{result}</pre>
      </div>
    );
  }