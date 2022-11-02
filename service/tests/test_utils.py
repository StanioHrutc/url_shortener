import os

from service.utils.conf import get_config_vars_from_env
from service.utils.url_shortener import generate_random_short_url


def test_get_config_vars_from_env():
    os.environ["MYSQL_ROOT_USER"] = "dummy"
    os.environ["MYSQL_ROOT_PASSWORD"] = "strongpassword"

    env_vars = get_config_vars_from_env()

    assert env_vars["password"] == "strongpassword"
    assert env_vars["user"] == "dummy"


def test_generate_random_short_url():
    random_url = generate_random_short_url()

    assert len(random_url) == 14
