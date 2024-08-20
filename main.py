from core.infrastructure.persistence.user_repository_impl import UserRepositoryImpl

if __name__ == "__main__":
    repo = UserRepositoryImpl()
    created_user = repo.create_user(
        username="test2e", password="te2ste", email="teste@tes22te.com", is_active=True
    )
    print(created_user)

    users = repo.get_users(page=1, per_page=10)
    print(users)
