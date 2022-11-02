from sqlalchemy import create_engine
from sqlalchemy.orm import Session, query

from service.utils.conf import get_config_vars_from_env

from service.db.models import (
    URLInformation, User,
    UserClick, Base
)


class Connection:
    """Context manager for convenient work with SQL Alchemy connection."""
    CONNECTION_STRING_PATTERN = "mysql+pymysql://{user}:{password}@{server}:{port}/{db}"

    def __init__(self):
        self.__session = self.__get_session()
        self.__credentials = get_config_vars_from_env()

    def __enter__(self):
        return self.__session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close_all()

    def __get_session(self) -> Session:
        """Generates session for working with the DB.
           Should be used as a context manager for security and correct state/resources handling.
           Besides, with the help of ORM creates tables in DB according to described models.
           If table was already created, command will be ignored automatically.

        Returns:
            Session - session object for the manipulation with the DB.
        """
        engine = create_engine(self.CONNECTION_STRING_PATTERN.format(**get_config_vars_from_env()))
        Base.metadata.create_all(engine, [
            User.__table__, URLInformation.__table__,
            UserClick.__table__
        ])
        with Session(engine) as connection:
            return connection


class DBHandler:
    """Class-cover for high level sql operations."""

    @staticmethod
    def create_new_user(username: str) -> None:
        """Creates user record in the DB.

        Params:
            username (str) - name of the user.
        """
        with Connection() as conn:
            try:
                user = User(name=username)
                conn.add(user)
                conn.commit()
            except:
                # Usually cases with the same User creation
                # skipping such errors for simplicity
                pass

    @staticmethod
    def create_url_record(url: str, short_url: str) -> None:
        """Creates URL record in the DB.

        Params:
            url (str) - full record's url.
            short_url (str) - short record's url.
        """
        with Connection() as conn:
            url_record = URLInformation(url=url, short_url=short_url)
            conn.add(url_record)
            conn.commit()

    @staticmethod
    def create_user_url_mapping(username: str, url: str) -> None:
        """Creates UserClick mapping record in the DB.

        Params:
            username (str) - name of the user.
            url (str) - full record's url.
        """
        with Connection() as conn:
            user_click_mapping = UserClick(pair_id=username+url, user_name=username, url=url)
            conn.add(user_click_mapping)
            conn.commit()

    @staticmethod
    def update_user_click_information(pair_id: str) -> None:
        """Updates click amount for URL mapping.

        Params:
            pair_id (str) - unique user+url pair for updating related table.
        """
        with Connection() as conn:
            conn\
                .query(UserClick)\
                .filter(UserClick.pair_id == pair_id)\
                .update({"clicks_amount": UserClick.clicks_amount + 1})
            conn.commit()

    @staticmethod
    def get_records(username: str) -> query.Query:
        """Returns joined information about User Click mapping and URL Information
         for further displaying on the UI.

        Params:
            username (str) - name of the user.

        Returns:
            query.Query - SQLAlchemy query object with DB results inside.
        """
        with Connection() as conn:
            records = conn\
                        .query(UserClick.user_name, UserClick.pair_id,
                               UserClick.url, UserClick.clicks_amount,
                               URLInformation.short_url)\
                        .join(URLInformation, UserClick.url == URLInformation.url)\
                        .filter(UserClick.user_name == username)

            return records
