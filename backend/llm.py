import requests

PROMPT_TEMPLATE = """
You are an expert in regulatory compliance.

Given the following change in a document, provide a structured JSON with:
- "change_summary": a concise one-sentence summary of what changed
- "change_type": one of ["New Requirement", "Clarification of Existing Requirement", "Minor Edit", "Deletion of Requirement"]

The old text (if available) is:
"{old_text}"

The new text (if available) is:
"{new_text}"

Respond ONLY with the JSON.
"""

def analyze_change(change, model='phi'):
    prompt = PROMPT_TEMPLATE.format(
        old_text=change.get("old", "None"),
        new_text=change.get("new", "None")
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    result_text = response.json()["response"]

    try:
        json_start = result_text.index("{")
        json_end = result_text.rindex("}") + 1
        parsed = eval(result_text[json_start:json_end])
        return parsed
    except Exception as e:
        return {"change_summary": "LLM failed to analyze.", "change_type": "Unknown"}
