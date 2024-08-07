from typing import List
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.infrastructure.settings.db_settings import SqlAlchemyBaseEntity


class UserTable(SqlAlchemyBaseEntity):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.current_timestamp()
    )
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    account: Mapped["AccountTable"] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class AccountTable(SqlAlchemyBaseEntity):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.current_timestamp()
    )
    total_balance = Column(Float, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    user: Mapped["UserTable"] = relationship(back_populates="account")
    transactions: Mapped[List["TransactionTable"]] = relationship(
        back_populates="account", cascade="all, delete-orphan"
    )


class TransactionTable(SqlAlchemyBaseEntity):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.current_timestamp()
    )
    amount = Column(Float, nullable=False)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    account: Mapped["AccountTable"] = relationship(back_populates="transactions")
