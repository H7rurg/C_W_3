import pytest

from src.models import Operation


@pytest.fixture
def operation_instance():
    operation_executed = Operation(
        pk=123,
        date="2019-08-26T10:50:58.294041",
        state="EXECUTED",
        operation_amount={
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        description="sadsad",
        from_="Счет 75106830613657916952",
        to="MasterCard 7158300734726758"
    )
    operation_canceled = Operation(
        pk=678,
        date="2018-07-26T10:50:58.294041",
        state="CANCELED",
        operation_amount={
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        description="sadsad",
        from_="MasterCard 75106830613657916952",
        to="MasterCard 7158300734726758"
    )
    return [operation_executed, operation_canceled]


@pytest.fixture
def operation_dict():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {}
    ]
