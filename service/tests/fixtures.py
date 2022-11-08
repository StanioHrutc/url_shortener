import pytest

from service.main import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.app_context():
        with app.test_client() as client:
            with client.session_transaction() as session:
                session["username"] = "dummy"
            yield client
