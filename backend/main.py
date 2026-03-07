from fastapi import FastAPI
from pydantic import BaseModel
from github_service import fetch_commits, fetch_reviews
from code_parser import clone_repo, parse_python_repo
from analysis_engine import analyze_commits, analyze_reviews
from explanation_engine import build_explanation_payload
from bedrock_service import generate_story

app = FastAPI(title="StoryCode")

class AnalyzeRequest(BaseModel):
    repo_url: str
    explanation_type: str = "structure"
    abstraction_level: str = "developer"

@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    repo_path = clone_repo(request.repo_url)

    code_info = parse_python_repo(repo_path)
    commits = fetch_commits(request.repo_url)
    reviews = fetch_reviews(request.repo_url)

    commit_analysis = analyze_commits(commits)
    review_analysis = analyze_reviews(reviews)

    structured_payload = build_explanation_payload(
        code_info,
        commits,
        commit_analysis,
        review_analysis,
        request.explanation_type
    )

    story = generate_story(
        structured_payload,
        request.explanation_type,
        request.abstraction_level
    )

    return {
        "repository": request.repo_url,
        "explanation_type": request.explanation_type,
        "abstraction_level": request.abstraction_level,
        "story": story
    }