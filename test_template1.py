import pytest

# NOTE: pip install pytest
@pytest.mark.parametrize("input,expected", [(2,4), (3,9), (4,16), (5,25), (6,36)])
def test_square(input, expected):
    assert square(input) == expected


from calculator import square


def main():
    test_square()


def test_square():
    # Simulate PyCharm's test session header
    print("\n============================= Test Session Starts ==============================")
    
    test_cases = [
        ("Test 1 (input=2)", 2, 4),
        ("Test 2 (input=3)", 3, 9),
        ("Test 3 (input=4)", 4, 16),
        ("Test 4 (input=5)", 5, 25),
        ("Test 5 (input=6)", 6, 36)
    ]

    passed = 0
    failed = 0

    for name, n, expected in test_cases:
        try:
            result = square(n)
            assert result == expected
            print(f"{name} PASSED!")  # PyCharm uses green text here
            passed += 1
        except AssertionError:
            print(f"\033[31m{name} FAILED\033[0m")  # Red text for failures
            print(f"  \033[34mExpected:\033[0m {expected}")
            print(f"  \033[34mActual:\033[0m   {result}")
            print("  \033[90mAssertionError: assert {expected} == {result}\033[0m".format(
                expected=expected, result=result))
            failed += 1
        print()  # Spacing between tests

    # Simulate PyCharm's test summary
    print(f"\n=========================== short test summary info ===========================")
    print(f"\033[32m{passed} passed\033[0m", end="")
    if failed > 0:
        print(f", \033[31m{failed} failed\033[0m", end="")
    print(f" in 0.02s\n")

    # Simulate PyCharm's closing banner
    print("============================== Test Session Ends ===============================")



if __name__ == "__main__":
    main()
