import time

# NOTE: pip install alive-progress
from alive_progress import alive_bar
from calculator import square  # Import your function

def run_test_cases(test_cases, func):
    results = []
    print("\n============================= Test Session Starts ==============================")
    with alive_bar(len(test_cases), spinner='dots_waves', title='Running tests') as bar:
        for idx, (name, args, expected) in enumerate(test_cases, 1):
            try:
                result = func(args)  # square() only takes 1 argument
                if result == expected:
                    print(f"\r{idx}. {name} ... \033[32m✅ PASSED\033[0m", end='', flush=True)
                    results.append((name, True, expected, result))
                else:
                    print(f"\r{idx}. {name} ... \033[31m❌ FAILED\033[0m", end='', flush=True)
                    results.append((name, False, expected, result))
                time.sleep(0.1)  # Reduce sleep for faster execution
            except Exception as e:
                print(f"\r{idx}. {name} ... \033[31m❌ ERROR\033[0m", end='', flush=True)
                results.append((name, False, expected, str(e)))
            bar()
            print()

    # Summary
    passed = sum(1 for r in results if r[1])
    failed = len(results) - passed
    print(f"\n=========================== Test Summary Info ===========================")
    print(f"\033[32m{passed} passed\033[0m", end="")
    if failed > 0:
        print(f", \033[31m{failed} failed\033[0m", end="")
    print(f" in {len(results)*0.1:.2f}s\n")  # Adjusted time
    print("============================== Test Session Ends ===============================")

    # Failure details
    for name, ok, expected, actual in results:
        if not ok:
            print(f"\033[31m{name} FAILED\033[0m")
            print(f"  Expected: {expected}")
            print(f"  Actual:   {actual}")

if __name__ == "__main__":
    test_cases = [
        ("Test 1 (input = 2)", 2, 4),
        ("Test 2 (input = 3)", 3, 9),
        ("Test 3 (input = 4)", 4, 16),
        ("Test 4 (input = 5)", 5, 25),
        ("Test 5 (input = 6)", 6, 36),
        ("Test 6 (input = 0)", 0, 0),
        ("Test 7 (input = -4)", -4, 16),
    ]
    run_test_cases(test_cases, square)  # Test your square function
