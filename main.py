from config import OPERATIONS_PATH
from src.utils import load_operation, get_instances, get_executed_operations, sort_operations_by_date


def main():
    operations = load_operation(OPERATIONS_PATH)
    instances = get_instances(operations)
    executed_operations = get_executed_operations(instances)
    sorted_operations = sort_operations_by_date(executed_operations)
    for operation in sorted_operations[:5]:
        print(operation)
        print()

if __name__ == '__main__':
    main()
