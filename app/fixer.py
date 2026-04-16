from app.llm import generate
from db.vector_store import search_similar

def suggest_fix(log, analysis):
    context = "\n".join(search_similar(log))

    prompt = f"""
    Suggest a fix for this error.

    Past fixes:
    {context}

    Error:
    {log}

    Analysis:
    {analysis}

    Return:
    - Steps to fix
    - Code patch if possible
    """

    return generate(prompt)