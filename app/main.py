from fastapi import FastAPI
from app.analyzer import analyze_error
from app.fixer import suggest_fix
from app.scorer import confidence_score
from db.vector_store import add_to_memory, load_memory

app = FastAPI()
load_memory()

@app.post("/heal")
def heal(data: dict):
    log = data["log"]

    analysis = analyze_error(log)
    fix = suggest_fix(log, analysis)
    score = confidence_score(log, fix)

    add_to_memory(log, analysis, fix)

    return {
        "analysis": analysis,
        "fix": fix,
        "confidence": score
    } 

@app.get("/history")
def get_history():
    from db.vector_store import memory
    return memory[::-1]  # latest first