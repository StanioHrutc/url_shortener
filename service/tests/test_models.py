from service.db.models import (
    URLInformation, User,
    UserClick
)


def test_user_model():
    user = User(name="Target Dummy")

    assert user.name == "Target Dummy"
    assert user.__tablename__ == "User"


def test_url_information_model():
    url_info = URLInformation(
        url="https://dummy.com", short_url="bb.by/asdjJFsdd"
    )

    assert url_info.url == "https://dummy.com"
    assert url_info.short_url == "bb.by/asdjJFsdd"
    assert url_info.__tablename__ == "URLInformation"


def test_user_click_model():
    url, user, clicks_amount = "https://dummy.com", "dummy", 10
    user_click = UserClick(
        pair_id=user + url, user_name=user,
        url=url, clicks_amount=clicks_amount
    )

    assert user_click.url == url
    assert user_click.pair_id == user + url
    assert user_click.clicks_amount == 10
    assert user_click.__tablename__ == "UserClicks"
