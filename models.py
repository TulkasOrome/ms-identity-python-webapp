from sqlalchemy import String
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

    account_id: Mapped[int]
    role: Mapped[str] = mapped_column(String(30))
    user_id: Mapped[str] = mapped_column(String(30), autoincrement=True, primary_key=True)

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    uid: Mapped[str] = mapped_column(String(30))
    display_name: Mapped[str] = mapped_column(String(30))
    available_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    account_id: Mapped[int]
    role: Mapped[str] = mapped_column(String(30))
    confirmed: Mapped[str] = mapped_column(String(30))
    custom_attributes: Mapped[str] = mapped_column(String(30))
    accounts: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))


