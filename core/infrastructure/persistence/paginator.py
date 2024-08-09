from sqlalchemy.orm import Query


def paginate_query(query: Query, page: int, per_page: int):
    return query.limit(per_page).offset((page - 1) * per_page).all()
