import pytest

# Given a positive integer n, write a function that returns true if it is a perfect square and false otherwise. 
# Don’t use any built-in math functions like sqrt. Hint: Use binary search!
# Examples: 
# $ perfectSquare(25)
# $ true
# $ perfectSquare(10) $ false

def perfect_square(target, left=None, right=None):
    if left is None or right is None:
        left = 0
        right = target

    mid = int((left+right)/2.0)
    print(f"Target:#{target}, Left:#{left}, Right:#{right}, Mid:#{mid}")

    if target == 1:
        return True

    try_square = mid * mid
    if try_square == target:
        return True
    elif abs(left-right) == 1:
        return False
    elif try_square < target:
        return perfect_square(target, mid, right)
    elif try_square > target:
        return perfect_square(target, left, mid)



@pytest.mark.parametrize("num, answer", [
        (0, True),
        (1, True),
        (2, False),
        (3, False),
        (4, True),
        (9, True),
        (10, False),
        (12, False),
        (13, False),
        (25, True),
        (49, True),
        (50, False),
        (99, False),
        (100, True),
        (101, False)
    ])
def test_perfect_square(num, answer):
    assert perfect_square(num) == answer, f"num: {num}"
