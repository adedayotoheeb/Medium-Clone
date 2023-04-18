import pytest
from pytest_factoryboy import register
from core_apps.core.test.factories import UserFactory

register(UserFactory)

@pytest.fixture
def base_user(db, user_factory):
    new_user = user_factory.create()
    return new_user


@pytest.fixture
def super_user(db, user_factory):
    new_user = user_factory.create(is_staff=True, is_superuser=True)
    return new_user


@pytest.fixture
def profile(db, profile_factory):
    user_profile = profile_factory.create()
    return user_profile


@pytest.fixture
def test_user(db, user_factory):
    user = user_factory.create()
    yield user