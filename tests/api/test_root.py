from fastapi.testclient import TestClient

from app.config import settings


def test_healt_check(test_app: TestClient):
    expected_response = {
        "title": settings.TITLE,
        "description": settings.DESCRIPTION,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
    }

    response = test_app.get("/api/healt-check")
    assert response.status_code == 200
    assert response.json() == expected_response
