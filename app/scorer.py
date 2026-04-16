from app.llm import generate

def confidence_score(log, fix):
    prompt = f"""
    Rate confidence of this fix from 0 to 1.

    Error:
    {log}

    Fix:
    {fix}

    Only return number.
    """

    try:
        return float(generate(prompt).strip())
    except:
        return 0.5