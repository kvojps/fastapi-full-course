from repositories.user_repository import create_user
from tables import create_tables

if __name__ == "__main__":
    create_tables()
    create_user(
        username="admin", password="admin", email="admin@admin.com", is_active=True
    )
