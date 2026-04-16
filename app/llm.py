import ollama

MODEL = "phi3"  # lightweight for your Mac

def generate(prompt):
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"num_predict": 200}
    )
    return response["message"]["content"]