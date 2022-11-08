from fixtures import client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 302
    assert b"Redirect" in response.data
