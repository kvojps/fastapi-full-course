from typing import List
from core.infrastructure.persistence.paginator import paginate_query
from core.infrastructure.persistence.entities import UserTable
from core.infrastructure.settings.db_settings import repository
from core.infrastructure.persistence.user_repository import IUserRepository


class UserRepositoryImpl(IUserRepository):
    @repository
    def create_user(
        self, email: str, username: str, password: str, is_active: bool, **kwargs
    ) -> dict:
        session = kwargs.get("session")
        user = UserTable(
            email=email, username=username, password=password, is_active=is_active
        )
        session.add(user)
        session.flush()

        return self._entity_to_dict(user)

    @repository
    def get_users(self, page: int, per_page: int, **kwargs) -> List[dict]:
        session = kwargs.get("session")
        users = paginate_query(session.query(UserTable), page, per_page)

        return [self._entity_to_dict(user) for user in users]

    @repository
    def get_user_by_id(self, user_id: int, **kwargs) -> dict:
        session = kwargs.get("session")
        user = _get_user_by_id(session, user_id)

        return _entity_to_dict(user)

    @repository
    def get_user_by_email(self, email: str, **kwargs) -> dict:
        session = kwargs.get("session")
        if (
            user := session.query(UserTable).filter(UserTable.email == email).first()
        ) is None:
            raise KeyError(f"User not found")

        return _entity_to_dict(user)

    @repository
    def update_user(
        self, user_id: int, username: str, password: str, is_active: bool, **kwargs
    ) -> dict:
        session = kwargs.get("session")
        user = self._get_user_by_id(session, user_id)
        user.username = username
        user.password = password
        user.is_active = is_active
        session.flush()

        return self._entity_to_dict(user)

    @repository
    def delete_user(self, user_id: int, **kwargs) -> None:
        session = kwargs.get("session")
        user = self._get_user_by_id(session, user_id)
        session.delete(user)

    def _entity_to_dict(self, user: UserTable) -> dict:
        return {
            "id": user.id,
            "created_at": user.created_at,
            "updated_at": user.updated_at,
            "email": user.email,
            "username": user.username,
            "is_active": user.is_active,
        }

    def _get_user_by_id(self, session, user_id: int) -> UserTable:
        if (user := session.query(UserTable).get(user_id)) is None:
            raise KeyError(f"User not found")
        return user
