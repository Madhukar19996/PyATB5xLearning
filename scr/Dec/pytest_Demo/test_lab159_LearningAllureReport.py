import pytest
import allure



@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase check for the negative  create booking")

@pytest.mark.positive
def test_create_booking_negative():
    print("Test_Case1")
    assert 1-1 == 2

@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase check for the positpscr/Dec/pytest_Demo/test_lab159_LearningAllureReport.pyive  create booking")

@pytest.mark.negative
def test_create_booking_positive_1():
    print("Test_Case2")
    assert 1 + 1 == 2


@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase check for the positive  create booking")
@pytest.mark.negative
def test_create_booking_positive_2():
    print("Test_Case2")
    assert 1 + 1 == 2