def classify_commit(message):
    msg = message.lower()
    labels = []

    if "fix" in msg or "bug" in msg:
        labels.append("bug_fix")
    if "refactor" in msg:
        labels.append("refactor")
    if "add" in msg or "feature" in msg:
        labels.append("feature")

    return labels


def analyze_commits(commits):
    file_frequency = {}
    classification_counts = {"bug_fix": 0, "refactor": 0, "feature": 0}

    for c in commits:
        labels = classify_commit(c["message"])
        for label in labels:
            classification_counts[label] += 1

        for f in c["files"]:
            file_frequency[f] = file_frequency.get(f, 0) + 1

    hotspot_files = [
        f for f, count in file_frequency.items() if count > 2
    ]

    return {
        "classification": classification_counts,
        "hotspot_files": hotspot_files
    }


def analyze_reviews(reviews):
    concerns = []
    for r in reviews:
        body = r.get("body", "").lower()
        if "performance" in body:
            concerns.append("performance")
        if "security" in body:
            concerns.append("security")
        if "error" in body:
            concerns.append("error handling")

    return list(set(concerns))