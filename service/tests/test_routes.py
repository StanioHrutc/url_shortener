from fixtures import client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"login" in response.data
    assert b"URL Shortener" in response.data
