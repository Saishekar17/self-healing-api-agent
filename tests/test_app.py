import sys
import os
from unittest.mock import patch, MagicMock
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


# --- Test Vector Store ---

def test_add_to_memory():
    from db.vector_store import add_to_memory, memory, index

    initial_count = len(memory)

    with patch("db.vector_store.save_memory"):
        add_to_memory(
            "ConnectionError: timeout",
            "Server not responding",
            "Increase timeout to 30s"
        )

    assert len(memory) == initial_count + 1
    assert memory[-1]["error"] == "ConnectionError: timeout"
    assert memory[-1]["analysis"] == "Server not responding"
    assert memory[-1]["fix"] == "Increase timeout to 30s"


def test_memory_record_structure():
    from db.vector_store import memory

    if len(memory) > 0:
        record = memory[-1]
        assert "error" in record
        assert "analysis" in record
        assert "fix" in record


def test_search_similar_returns_list():
    from db.vector_store import search_similar, memory

    if len(memory) > 0:
        results = search_similar("timeout error", k=2)
        assert isinstance(results, list)


def test_search_similar_empty_memory():
    from db.vector_store import search_similar, index, memory
    import db.vector_store as vs

    # Save original
    original_memory = vs.memory.copy()

    # Empty it
    vs.memory = []

    results = search_similar("some error")
    assert results == []

    # Restore
    vs.memory = original_memory


# --- Test Scorer ---

def test_confidence_score_returns_float():
    with patch("app.scorer.generate", return_value="0.85"):
        from app.scorer import confidence_score
        score = confidence_score("TypeError: NoneType", "Add null check")
        assert isinstance(score, float)
        assert 0 <= score <= 1


def test_confidence_score_handles_bad_llm_output():
    with patch("app.scorer.generate", return_value="not a number"):
        from app.scorer import confidence_score
        score = confidence_score("some error", "some fix")
        assert score == 0.5  # fallback value


# --- Test Analyzer ---

def test_analyze_error_returns_string():
    with patch("app.analyzer.generate", return_value="Root cause: null pointer"):
        with patch("app.analyzer.search_similar", return_value=[]):
            from app.analyzer import analyze_error
            result = analyze_error("NullPointerException at line 42")
            assert isinstance(result, str)
            assert len(result) > 0


# --- Test Fixer ---

def test_suggest_fix_returns_string():
    with patch("app.fixer.generate", return_value="Add try-except block"):
        with patch("app.fixer.search_similar", return_value=[]):
            from app.fixer import suggest_fix
            result = suggest_fix("TimeoutError", "Server not responding")
            assert isinstance(result, str)
            assert len(result) > 0


# --- Test API Endpoint ---

def test_heal_endpoint():
    with patch("app.analyzer.generate", return_value="Connection issue"):
        with patch("app.fixer.generate", return_value="Retry with backoff"):
            with patch("app.scorer.generate", return_value="0.9"):
                with patch("db.vector_store.save_memory"):
                    from fastapi.testclient import TestClient
                    from app.main import app

                    client = TestClient(app)
                    response = client.post(
                        "/heal",
                        json={"log": "ConnectionError: max retries exceeded"}
                    )

                    assert response.status_code == 200
                    data = response.json()
                    assert "analysis" in data
                    assert "fix" in data
                    assert "confidence" in data


def test_history_endpoint():
    with patch("db.vector_store.save_memory"):
        from fastapi.testclient import TestClient
        from app.main import app

        client = TestClient(app)
        response = client.get("/history")

        assert response.status_code == 200
        assert isinstance(response.json(), list)