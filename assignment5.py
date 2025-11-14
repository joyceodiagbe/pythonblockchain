# 1) Normal function that accepts another function as an argument
def normal_function(func):
    result = func()
    print(result)

# Example function to test


def print_hello_world():
    return "Hello, world!"


normal_function(print_hello_world)

# 2) Call your normal function by passing a lambda function
normal_function(lambda: 5 * 10)

# 3) Modify normal_function to accept an infinite number of arguments


def normal_function(func, *args):
    result = func(*args)  # Call the function with the provided arguments
    # 4) Format output nicely (centered in 20-character column)
    print(f"Result: {result:^20}")


# Example function to test
normal_function(lambda x, y: x + y, 10, 20)
normal_function(lambda *nums: sum(nums) / len(nums), 10, 20, 30, 40)
normal_function(lambda x: x**2, 7)
