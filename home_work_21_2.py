def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Приклади використання
print(multiply(2, 3, 4))
print(multiply(5, 6))