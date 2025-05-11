from calculator import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print(f"❌ Test 1 failed: Expected 4, Actual {square(2)}")
    else:
        print("✅ Test 1 PASSED!")
    try:
        assert square(3) == 9
    except AssertionError:
        print(f"❌ Test 2 failed: Expected 9, Actual {square(3)}")
    else:
        print("✅ Test 2 PASSED!")
    try:
        assert square(4) == 16
    except AssertionError:
        print(f"❌ Test 3 failed: Expected 16, Actual {square(4)}")
    else:
        print("✅ Test 3 PASSED!")
    try:
        assert square(5) == 25
    except AssertionError:
        print(f"❌ Test 4 failed: Expected 25, Actual {square(5)}")
    else:
        print("✅ Test 4 PASSED!")
    try:
        assert square(6) == 36
    except AssertionError:
        print(f"❌ Test 5 failed: Expected 36, Actual {square(6)}")
    else:
        print("✅ Test 5 PASSED!")


if __name__ == "__main__":
    main()
