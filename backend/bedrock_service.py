import boto3
import json

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def generate_story(payload, explanation_type, abstraction_level):

    tone_map = {
        "beginner": "Explain clearly for a beginner. Avoid jargon and define terms briefly.",
        "developer": "Explain for a developer. Discuss structure and responsibilities clearly.",
        "architect": "Provide architectural reasoning, layering analysis, and systemic insight.",
        "audit": "Focus on structural risk, dependency concentration, and fragility."
    }

    tone = tone_map.get(abstraction_level, tone_map["developer"])

    prompt = f"""
You are StoryCode, an explainability-first AI system.

Explanation Type: {explanation_type}
Audience Level: {abstraction_level}

Audience Guidance:
{tone}

Structured Evidence:
{json.dumps(payload, indent=2)}

Rules:
- Base explanation ONLY on structured evidence.
- Do NOT assume repository identity unless explicitly stated.
- If inference is made, label it as "Likely" or "Appears to".
- Avoid listing repetitively.
- Synthesize architectural patterns.
- Start directly with analysis.

For structure explanations:
1. Focus primarily on core source directories.
2. Mention tests briefly as validation layer.
3. Identify architectural layering.
4. Conclude with:
   - Architectural Pattern Identified
   - System Boundary Overview
   - Confidence Level
"""

    body = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1000,
        "temperature": 0.3
    }

    response = bedrock.invoke_model(
        modelId="qwen.qwen3-coder-next",
        body=json.dumps(body)
    )

    response_body = json.loads(response["body"].read())
    return response_body["choices"][0]["message"]["content"]