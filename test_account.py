import pytest
from account import Account


def test_init():
    account = Account("Tom")
    assert account.get_name() == "Tom"
    assert account.get_balance() == 0


def test_deposit():
    account = Account("Tom")

    # Successful deposit
    assert account.deposit(150) == True
    assert account.get_balance() == 150

    # Negative deposit (shouldn't affect the balance)
    assert account.deposit(-60) == False
    assert account.get_balance() == 150

    # Zero deposit (shouldn't affect the balance)
    assert account.deposit(0) == False
    assert account.get_balance() == 150


def test_withdraw():
    account = Account("Tom")
    account.deposit(150)

    # Successful withdrawal
    assert account.withdraw(60) == True
    assert account.get_balance() == 90

    # Negative withdrawal (shouldn't affect the balance)
    assert account.withdraw(-30) == False
    assert account.get_balance() == 90

    # Zero withdrawal (shouldn't affect the balance)
    assert account.withdraw(0) == False
    assert account.get_balance() == 90

    # Excessive withdrawal (more than balance, shouldn't affect the balance)
    assert account.withdraw(110) == False
    assert account.get_balance() == 90
