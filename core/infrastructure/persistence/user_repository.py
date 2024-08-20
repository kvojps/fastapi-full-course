from abc import ABC, abstractmethod
from typing import List


class IUserRepository(ABC):
    @abstractmethod
    def create_user(
        self, email: str, username: str, password: str, is_active: bool, **kwargs
    ) -> dict: ...

    @abstractmethod
    def get_users(self, page: int, per_page: int, **kwargs) -> List[dict]: ...

    @abstractmethod
    def get_user_by_id(self, user_id: int, **kwargs) -> dict: ...

    @abstractmethod
    def get_user_by_email(self, email: str, **kwargs) -> dict: ...

    @abstractmethod
    def update_user(
        self, user_id: int, username: str, password: str, is_active: bool, **kwargs
    ) -> dict: ...

    @abstractmethod
    def delete_user(self, user_id: int, **kwargs) -> None: ...
