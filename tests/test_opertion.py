from src.models import Operation


def test_operation_convert_date():
    operation = Operation(
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
    assert operation.convert_date("2019-08-26T10:50:58.294041") == "26.08.2019"
