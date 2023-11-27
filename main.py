from config import OPERATIONS_PATH
from src.utils import load_operation, get_instances, get_executed_operations


def main():
    operations = load_operation(OPERATIONS_PATH)
    instances = get_instances(operations)
    executed_operations = get_executed_operations(instances)
    print()

if __name__ == '__main__':
    main()
