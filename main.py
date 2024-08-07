from repositories.user_repository import (
    create_user,
    delete_user,
    get_user_by_email,
    get_user_by_id,
    get_users,
    update_user,
)
from settings.logging_settings import logger

if __name__ == "__main__":
    logger.debug("teste debug")
    logger.info("teste info")
    logger.warning("teste warning")
    logger.error("teste error")
    # created_user = create_user(
    #     username="teste", password="teste", email="teste@teste.com", is_active=True
    # )
    # print(created_user)

    # users = get_users(page=1, per_page=10)
    # print(users)

    # user_by_id = get_user_by_id(user_id=6)
    # print(user_by_id)

    # user_by_email = get_user_by_email(email="admin4@admin.com")
    # print(user_by_email)

    # updated_user = update_user(user_id=5, username="UPDATED", password="UPDATED", is_active=True)
    # print(updated_user)

    # delete_user(user_id=9)
