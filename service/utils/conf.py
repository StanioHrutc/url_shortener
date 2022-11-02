import os

from typing import Dict


def get_config_vars_from_env() -> Dict[str, str]:
    """Retrieves environment variables and forms a config with them.

    Returns:
        dict - configuration object.
    """
    conf = {
        "user": os.getenv("MYSQL_ROOT_USER"),
        "password": os.getenv("MYSQL_ROOT_PASSWORD"),
        "db": os.getenv("MYSQL_DATABASE"),
        "server": os.getenv("MYSQL_HOST"),
        "port": os.getenv("MYSQL_PORT")
    }

    return conf
