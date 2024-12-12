from robot import run


def run_tests_in_priority_order(test_file, priorities):
    for priority in priorities:
        print(f"Running tests with tag {priority}...")
        run(test_file, include=priority)


if __name__ == "__main__":
    # Define the path to your Robot Framework test file

    test_file = 'CGI.robot'

    # Define the priorities in the order you want them to execute
    priorities = [
        'priority=1',  # Critical
        'priority=2',  # High Priority
        'priority=3',  # Medium Priority
        'priority=4'  # Low Priority
    ]

    # Run tests in the defined priority order
    run_tests_in_priority_order(test_file, priorities)