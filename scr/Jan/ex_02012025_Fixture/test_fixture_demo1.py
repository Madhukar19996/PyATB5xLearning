import pytest


@pytest.fixture()
def create_token():
    return "abc1456@3*#"


@pytest.fixture()
def create_booking_id():
    return 121



@pytest.fixture()
def read_excel_file():
    return "XYZ"


def test_put(create_token, create_booking_id):
    print(create_token)
    print(create_booking_id)


def test_put_2(create_token, create_booking_id, read_excel_file):
    print(create_token)
    print(create_booking_id)
    print(read_excel_file)