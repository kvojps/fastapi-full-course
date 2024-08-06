from typing import List, Optional
from repositories.paginator import paginate_query
from settings.db_settings import repository
from tables.user_tables import UserTable


@repository
def create_user(
    email: str, username: str, password: str, is_active: bool, **kwargs
) -> dict:
    session = kwargs.get("session")
    user = UserTable(
        email=email, username=username, password=password, is_active=is_active
    )
    session.add(user)
    session.flush()

    return _entity_to_dict(user)


@repository
def get_users(page: int, per_page: int, **kwargs) -> List[dict]:
    session = kwargs.get("session")
    users = paginate_query(session.query(UserTable), page, per_page)

    return [_entity_to_dict(user) for user in users]


@repository
def get_user_by_id(user_id: int, **kwargs) -> Optional[dict]:
    session = kwargs.get("session")
    user = _get_user_by_id(session, user_id)

    return _entity_to_dict(user) if user else None

@repository
def get_user_by_email(email: str, **kwargs) -> Optional[dict]:
    session = kwargs.get("session")
    user = session.query(UserTable).filter(UserTable.email == email).first()

    return _entity_to_dict(user) if user else None


@repository
def update_user(
    user_id: int, username: str, password: str, is_active: bool, **kwargs
) -> Optional[dict]:
    session = kwargs.get("session")
    user = _get_user_by_id(session, user_id)
    if not user:
        return None

    user.username = username
    user.password = password
    user.is_active = is_active
    session.flush()

    return _entity_to_dict(user)


@repository
def delete_user(user_id: int, **kwargs) -> None:
    session = kwargs.get("session")
    user = _get_user_by_id(session, user_id)
    if not user:
        return None

    session.delete(user)


def _entity_to_dict(user: UserTable) -> dict:
    return {
        "id": user.id,
        "created_at": user.created_at,
        "updated_at": user.updated_at,
        "email": user.email,
        "username": user.username,
        "is_active": user.is_active,
    }


def _get_user_by_id(session, user_id: int) -> Optional[UserTable]:
    return session.query(UserTable).get(user_id)
