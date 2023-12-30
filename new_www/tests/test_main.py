import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_articles():
    response = client.get("/articles/")
    assert response.status_code == 200


def test_oauth_erroe():
    response = client.post(
        "/token", data={"username": "kotki", "password": "pieski"}
    )
    access_token = response.json().get("access_token")
    message = response.json().get("detail")

    assert access_token is None
    assert message == "User not found"


def test_oauth_success():
    response = client.post(
        "/token", data={"username": "Mario", "password": "oko"}
    )
    access_token = response.json().get("access_token")
    message = response.json().get("username")

    assert access_token is not None
    assert message == "Mario"


def test_post_article():
    auth = client.post("/token", data={"username": "Mario", "password": "oko"})
    token = auth.json().get("access_token")

    response = client.post(
        "/articles/",
        content=json.dumps(
            {
                "title": "Test Article",
                "slug": "test_art",
                "thumbnail": "string",
                "abstract": "string",
                "author_id": "8953dcc3-9513-48fc-9401-19147b1c0786",
                "body": {
                    "blocks": [
                        {
                            "id": "mhTl6ghSkV",
                            "type": "paragraph",
                            "data": {
                                "text": (
                                    "Hey. Meet the new Editor. On this picture"
                                    " you can see it in action. Then, try a"
                                    " demo 🤓"
                                )
                            },
                        }
                    ]
                },
                "published": True,
                "date_created": "30-12-2023",
            }
        ),
        headers={"Authorization": "Bearer " + token},
    )

    assert response.status_code == 201
    assert response.json().get("title") == "Test Article"

    article_id = response.json().get("id")
    response = client.delete(
        f"/articles/{article_id}",
        headers={"Authorization": "Bearer " + token},
    )

    assert response.status_code == 200
    assert response.json().get("id") == article_id

    assert token
