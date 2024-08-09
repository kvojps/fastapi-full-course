from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.infrastructure.settings.env_settings import settings

engine = create_engine(
    f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

session_local = sessionmaker(bind=engine)

SqlAlchemyBaseEntity = declarative_base()


@contextmanager
def get_session():
    session = session_local()
    try:
        yield session
    except IntegrityError as e:
        session.rollback()
        raise e
    finally:
        session.close()


def repository(func):
    def wrapper(*args, **kwargs):
        session = session_local()
        try:
            result = func(*args, **kwargs, session=session)
            session.commit()

            return result
        except IntegrityError as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    return wrapper
