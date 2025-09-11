import time
import requests 
BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts(session):
    start = time.time()
    resp = session.get(f"{BASE_URL}/posts")
    elapsed = (time.time() - start) * 1000  # в миллисекундах

    # статус
    assert resp.status_code == 200

    # заголовки
    assert "application/json" in resp.headers.get("Content-Type", "")

    # время ответа
    assert elapsed < 500

    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0

    for post in data:
        assert set(post.keys()) == {"userId", "id", "title", "body"}
        assert isinstance(post["userId"], int)
        assert isinstance(post["id"], int)
        assert isinstance(post["title"], str) and len(post["title"]) > 0
        assert isinstance(post["body"], str) and len(post["body"]) > 0


def test_create_post(session):
    payload = {
        "title": "fooCopy",
        "body": "bar",
        "userId": 1
    }

    start = time.time()
    resp = session.post(f"{BASE_URL}/posts", json=payload)
    elapsed = (time.time() - start) * 1000

    # статус
    assert resp.status_code == 201

    # время ответа
    assert elapsed < 700

    data = resp.json()
    assert set(data.keys()) == {"id", "title", "body", "userId"}
    assert isinstance(data["id"], int) and data["id"] >= 0
    assert isinstance(data["userId"], int) and data["userId"] >= 0
    assert isinstance(data["title"], str) and len(data["title"]) > 0
    assert isinstance(data["body"], str) and len(data["body"]) > 0

def test_put_update_post():
    payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }

    response = requests.put(f"{BASE_URL}/posts/1", json=payload)

    # Проверка статус-кода
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    # Проверка времени ответа
    assert response.elapsed.total_seconds() < 1, "Response took too long"

    data = response.json()

    # Проверка что ответ содержит все нужные поля
    assert isinstance(data, dict)
    assert set(data.keys()) == {"id", "title", "body", "userId"}

    # Проверка id
    assert isinstance(data["id"], int) and data["id"] >= 0

    # Проверка userId
    assert isinstance(data["userId"], int) and data["userId"] >= 0

    # Проверка что title и body не пустые строки
    assert isinstance(data["title"], str) and len(data["title"]) > 0
    assert isinstance(data["body"], str) and len(data["body"]) > 0
