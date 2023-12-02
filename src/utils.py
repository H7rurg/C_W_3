import json
from datetime import datetime

from src.models import Operation


def load_operation(path: str) -> list[dict]:
    """
    Чтение операций из файла

    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_instances(operations: list[dict]) -> list[Operation]:
    """
    Функция приобразования операций из файла json в список

    """
    operation_instances = []
    for operation in operations:
        if operation:
            operation_instance = Operation(
                pk=operation["id"],
                state=operation["state"],
                date=operation["date"],
                operation_amount=operation["operationAmount"],
                description=operation["description"],
                from_=operation.get("from", ""),
                to=operation["to"],
            )
            operation_instances.append(operation_instance)
    return operation_instances


def get_executed_operations(operations: list[Operation]) -> list[Operation]:
    """
    Функция вывода выполненых операций

    """
    executed_operation = []
    for operation in operations:
        if operation.state == "EXECUTED":
            executed_operation.append(operation)
    return executed_operation


def sort_operations_by_date(operations: list[Operation]) -> list[Operation]:
    """
    Функция сортировки по дате

    """
    return sorted(operations, key=lambda operation: datetime.strptime(operation.date, "%d.%m.%Y"), reverse=True)

