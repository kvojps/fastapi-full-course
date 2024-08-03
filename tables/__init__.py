from settings.db_settings import engine
from tables.user_tables import UserTable


def create_tables():
    UserTable.metadata.create_all(bind=engine)
