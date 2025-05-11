# test_calculator_visual.py
from calculator import square

# ANSI colour codes (work in PyCharm, VS Code, most terminals)
GREEN = "\033[92m"
RED   = "\033[91m"
RESET = "\033[0m"

def main() -> None:
    tests = [
        (2, 4),
        (3, 9),
        (4, 16),
        (5, 25),
        (6, 36),
    ]

    for i, (value, expected) in enumerate(tests, start=1):
        actual = square(value)
        if actual == expected:
            print(f"{GREEN}✓ Test {i} PASSED!{RESET}")
        else:
            print(f"{RED}✗ Test {i} failed: expected {expected}, got {actual}{RESET}")

if __name__ == "__main__":
    main()
