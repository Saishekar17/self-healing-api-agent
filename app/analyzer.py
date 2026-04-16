from app.llm import generate
from db.vector_store import search_similar

def analyze_error(log):
    context = "\n".join(search_similar(log))

    prompt = f"""
    Analyze this API error.

    Past similar errors:
    {context}

    Error:
    {log}

    Return:
    - Root cause
    - Error type
    """

    return generate(prompt)