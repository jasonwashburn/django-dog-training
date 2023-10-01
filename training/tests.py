import pytest
from django.contrib.auth import get_user_model

from .models import Owner, Pet


@pytest.fixture
def test_password():
    return "strong-test-pass"


@pytest.mark.django_db
def test_user_create():
    user = get_user_model().objects.create_user(
        username="testuser", email="testuser@example.com", password="secret"
    )
    assert user.username == "testuser"
    assert user.email == "testuser@example.com"
    assert user.check_password("secret") is True


@pytest.fixture
def create_user(db, test_password):
    def make_user(**kwargs):
        kwargs["password"] = test_password
        return get_user_model().objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def basic_owner(create_user):
    user = create_user(username="testuser", email="testuser@example.com")
    owner = Owner.objects.create(
        user=user,
        last_name="Smith",
        first_name="John",
        phone="555-555-5555",
        street_address_1="123 Main St",
        street_address_2="",
        city="Anytown",
        state="NY",
        zip_code="12345",
    )
    return owner


@pytest.mark.django_db
def test_can_create_owner(create_user):
    user = create_user(username="testuser", email="testuser@example.com")
    owner = Owner.objects.create(
        user=user,
        last_name="Smith",
        first_name="John",
        phone="555-555-5555",
        street_address_1="123 Main St",
        street_address_2="",
        city="Anytown",
        state="NY",
        zip_code="12345",
    )
    assert owner.user.username == "testuser"
    assert owner.user.email == "testuser@example.com"
    assert owner.last_name == "Smith"
    assert owner.first_name == "John"
    assert owner.phone == "555-555-5555"
    assert owner.street_address_1 == "123 Main St"
    assert owner.street_address_2 == ""
    assert owner.city == "Anytown"
    assert owner.state == "NY"
    assert owner.zip_code == "12345"


@pytest.mark.django_db
def test_can_create_pet(basic_owner):
    pet = Pet.objects.create(
        name="Fido", sex=0, age="2020-01-01", intact=True, owner=basic_owner
    )
    assert pet.name == "Fido"
    assert pet.sex == 0
    assert pet.age == "2020-01-01"
    assert pet.intact is True
    assert pet.owner.last_name == "Smith"
    assert pet.owner.first_name == "John"
