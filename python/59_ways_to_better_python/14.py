"""Prefer returning Exceptions instead of None"""
def divide_no_raise(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Invalid inputs")


def divide_two_return_values(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


success, result = divide_two_return_values(1, 0)
if not success:
    print("Code has errors")


# The good way

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid inputs") from e

x, y = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print("Invalid inputs")
else:
    print(f"Result is {result}")
