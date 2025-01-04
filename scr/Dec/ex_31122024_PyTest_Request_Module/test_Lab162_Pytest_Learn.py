import pytest
import allure
import requests


@allure.title("TC#1 - Verify that 2-2 == 0")
@allure.description("This is a Basic Math Test")
@pytest.mark.smoke
def test_basic_math():
    assert 2-2 == 0


@allure.title("TC#2 - Verify that 3-3 == 0")
@allure.description("This is a Regression test case which checks 3-3 == 0")
@pytest.mark.regression
def test_sub1():
    assert 3-3 == 0


@allure.title("TC#3 - Verify that 3-3 == 0")
@allure.description("This is a Smoke test case which checks 3-3 == 0")
@pytest.mark.smoke
def test_sub2():
    assert 3-3 == 0


@pytest.mark.skip(reason = "Not working, Skip it")
def test_sub3():
    assert 0-0 != 0