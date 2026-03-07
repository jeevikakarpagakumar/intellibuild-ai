import requests

def parse_repo_url(repo_url):
    parts = repo_url.replace("https://github.com/", "").split("/")
    return parts[0], parts[1]

def fetch_commits(repo_url, max_commits=15):
    owner, repo = parse_repo_url(repo_url)
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    data = response.json()

    commits = []

    for item in data[:max_commits]:
        sha = item["sha"]
        commit_details = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}"
        ).json()

        files = [f["filename"] for f in commit_details.get("files", [])]

        commits.append({
            "message": item["commit"]["message"],
            "author": item["commit"]["author"]["name"],
            "files": files,
            "additions": commit_details.get("stats", {}).get("additions", 0),
            "deletions": commit_details.get("stats", {}).get("deletions", 0),
        })

    return commits


def fetch_reviews(repo_url, max_prs=5):
    owner, repo = parse_repo_url(repo_url)
    pulls_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    pulls = requests.get(pulls_url).json()

    review_data = []

    for pr in pulls[:max_prs]:
        reviews_url = pr["review_comments_url"]
        reviews = requests.get(reviews_url).json()

        for r in reviews:
            review_data.append({
                "file": r.get("path"),
                "body": r.get("body")
            })

    return review_data