from fastapi.testclient import TestClient

from fact_searcher.app import app
from fact_searcher.settings import Settings


client = TestClient(app)


def test_get_sights_by_city():
    response = client.post(
        "/facts_searcher/city",
        json=["Moscow"],
    )

    assert response.status_code == 200
    print(response.json())
