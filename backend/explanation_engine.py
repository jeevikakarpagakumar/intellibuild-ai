def build_explanation_payload(code_info, commits, commit_analysis, review_analysis, explanation_type):

    payload = {}

    if explanation_type in ["structure", "full_analysis"]:
        # Reduce test dominance
        filtered_modules = [
            m for m in code_info["top_modules"]
            if not m[0].startswith("tests/")
        ][:10]

        payload["code_structure"] = {
            "total_functions": code_info["total_functions"],
            "total_classes": code_info["total_classes"],
            "top_modules": filtered_modules,
            "entry_points": code_info["entry_points"],
            "core_directory": code_info["core_directory"],
            "architectural_signals": code_info["architectural_signals"]
        }

    if explanation_type in ["evolution", "full_analysis"]:
        payload["commit_trends"] = commit_analysis
        payload["recent_commits"] = [c["message"] for c in commits]

    if explanation_type in ["risk", "full_analysis"]:
        payload["risk_signals"] = {
            "hotspot_files": commit_analysis["hotspot_files"],
            "classification": commit_analysis["classification"]
        }

    if explanation_type in ["review", "full_analysis"]:
        payload["review_concerns"] = review_analysis

    return payload