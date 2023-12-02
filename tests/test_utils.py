from src.models import Operation
from src.utils import get_instances, get_executed_operations, sort_operations_by_date


def test_get_instances(operation_dict):
    operations = get_instances(operation_dict)
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operation)
    assert len(operations) == 1
    assert operations[0].pk == 939719570


def test_get_executed_operations(operation_instance):
    operations = get_executed_operations(operation_instance)
    assert len(operations) == 1
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operation)
    assert operations[0].state == "EXECUTED"


def test_sort_operations_by_date(operation_instance):
    operations = sort_operations_by_date(operation_instance)
    assert len(operations) == 2
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operation)
    assert operations[0].date > operations[1].date
