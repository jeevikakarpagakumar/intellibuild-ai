import axios from "axios";

const API = axios.create({
  baseURL: "https://fsws8w9yzf.execute-api.us-east-1.amazonaws.com/prod"
});

export const analyzeRepo = async (repoUrl) => {
  const res = await API.post("/analyze", {
    repo_url: repoUrl,
    explanation_type: "structure",
    abstraction_level: "developer"
  });

  return res.data;
};