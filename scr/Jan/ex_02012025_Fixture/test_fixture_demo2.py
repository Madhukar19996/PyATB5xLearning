import pytest


@pytest.fixture()
def create_token():
    return "ABC"


@pytest.fixture()
def create_booking_id():
    return 1234


def test_update_req_1(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)