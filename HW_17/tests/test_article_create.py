from conftest import client
import json


def test_article_create_(client):
    response = client.get('/article/create')
    assert response.status_code == 200

    headers = {
        "Content-Type": "application/json"
    }

    json = {
        "title": "test",
        "slug": "test-article",
        "short_description": "bla bla bla bla bla bla bla ",
        "description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla ",
        "img": "https://img1.goodfon.ru/original/1920x1080/9/bc/gorod-moskva-moscow-mashiny.jpg",
    }
    response = client.post("/article/store", headers=headers, json=json)
    assert response.status_code == 500