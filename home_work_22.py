def check_and_add(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            return result + 10
        return result
    return wrapper

@check_and_add
def my_function(a, b):
    return a + b

print(my_function(5, 3))
print(my_function(5, 3.5))