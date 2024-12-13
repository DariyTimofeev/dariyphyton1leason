def long_strings(strings):
    long_strings = [s for s in strings if len(s) > 10]

    print("Строчки длиной более 10 символов:", long_strings)

    return long_strings

strings_list = ["1234", "1234567890,10", "123", "12345", "1234567890,10,11"]
long_strings(strings_list)