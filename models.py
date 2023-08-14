from sqlalchemy import String, PickleType, Integer
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Account(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))


class Account_User(Base):
    __tablename__ = "account_user"

    account_id: Mapped[int] = mapped_column(String(30))
    role: Mapped[str] = mapped_column(String(30))
    user_id: Mapped[str] = mapped_column(String(30))
    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    uid: Mapped[str] = mapped_column(String(30))
    display_name: Mapped[str] = mapped_column(String(30), nullable=True)
    available_name: Mapped[str] = mapped_column(String(30), nullable=True)
    email: Mapped[str] = mapped_column(String(30))
    account_id: Mapped[int] = mapped_column(nullable=True)
    role: Mapped[str] = mapped_column(String(30), nullable=True)
    confirmed: Mapped[str] = mapped_column(String(30), nullable=True)
    custom_attributes: Mapped[list] = mapped_column(MutableList.as_mutable(PickleType),
                                                    default=[], nullable=True)
    accounts: Mapped[list] = mapped_column(MutableList.as_mutable(PickleType),
                                                    default=[], nullable=True)
    password: Mapped[str] = mapped_column(String(30), nullable=True)
