from globalone.models import Base, User


def test_user_maps_existing_users_table():
    assert User.__tablename__ == "users"
    assert set(User.__table__.columns.keys()) == {
        "id",
        "name",
        "age",
        "email",
        "created_at",
    }
    assert User.__table__.metadata is Base.metadata
