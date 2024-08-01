from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from settings.db_settings import SqlAlchemyBaseEntity


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
