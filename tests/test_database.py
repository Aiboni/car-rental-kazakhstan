import pytest
from sqlalchemy import inspect, text
from backend.database import engine


def test_database_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1


def test_users_table_exists():
    inspector = inspect(engine)
    assert "users" in inspector.get_table_names()


def test_users_columns():
    inspector = inspect(engine)
    columns = {
        column["name"]
        for column in inspector.get_columns("users")
    }

    required = {
        "id",
        "phone_number",
        "full_name",
        "role",
        "verification_status",
        "created_at",
    }

    assert required.issubset(columns)


def test_phone_number_unique():
    inspector = inspect(engine)
    constraints = inspector.get_unique_constraints("users")

    assert any(
        "phone_number" in constraint["column_names"]
        for constraint in constraints
    )
