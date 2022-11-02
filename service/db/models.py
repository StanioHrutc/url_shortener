from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    Column, ForeignKey,
    String, Integer
)


Base = declarative_base()


class URLInformation(Base):
    """Model for describing URL Information"""
    __tablename__ = "URLInformation"

    url = Column(String(150), primary_key=True)
    short_url = Column(String(20))


class User(Base):
    """Model for describing User Information"""
    __tablename__ = "User"

    name = Column(String(25), primary_key=True)


class UserClick(Base):
    """Model for describing User Click mapping Information"""
    __tablename__ = "UserClicks"

    pair_id = Column(String(200), primary_key=True)
    user_name = Column(String(25), ForeignKey("User.name"))
    url = Column(String(150), ForeignKey("URLInformation.url"))
    clicks_amount = Column(Integer, default=0)
