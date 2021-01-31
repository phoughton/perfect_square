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
    else:
        print("This should not happen")

print(perfect_square(10))
print()
print(perfect_square(9))
print()
print(perfect_square(25))
print()
print(perfect_square(2))
print()
print(perfect_square(1))
print()
print(perfect_square(0))
print()
print(perfect_square(11))
print()
print(perfect_square(12))
print()
print()
print(perfect_square(80))
print()
print(perfect_square(81))
print()
print(perfect_square(82))