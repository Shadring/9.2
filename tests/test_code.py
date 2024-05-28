import pytest
from src.masks import card_number, account_number
from src.widget import time_formator


@pytest.mark.parametrize("x,y", [("Maestro 7000 7922 8960 6361", "Maestro 7000 79** **** 6361"),
                                 ("MasterCard 7158 3007 3472 6758", "MasterCard 7158 30** **** 6758"),
                                 ("Visa Classic 6831 9824 7673 7658", "Visa Classic 6831 98** **** 7658")])
def test_masks(x, y):
    assert card_number(x) == y


@pytest.mark.parametrize("x,y",
                         [("Счет 73654108430135874305", "Счет **4305"), ("Счет 35383033474447895560", "Счет **5560"),
                          ("Счет 64686473678894779589", "Счет **9589")])
def test_masks(x, y):
    assert account_number(x) == y


@pytest.mark.parametrize("x,y",
                         [("2018-07-11T02:26:18.671407", "11.07.2018"), ("2019-08-12T02:26:18.671407", "12.08.2019"),
                          ("2020-11-30T02:26:18.704176", "30.11.2020")])
def test_widget(x, y):
    assert time_formator(x) == y
