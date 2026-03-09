import axios from "axios";

export const analyzeRepo = async (repoUrl) => {

  const res = await axios.post(
    "https://3.237.18.233/analyze",
    {
      repo_url: repoUrl,
      explanation_type: "structure",
      abstraction_level: "developer"
    }
  );

  return res.data;
};