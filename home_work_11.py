def long_strings(strings):
    long_strings = [s for s in strings if len(s) > 10]

    print("Строчки длиной более 10 символов:", long_strings)

    return long_strings

strings_list = ["короткий", "длинныйстрокдлинный", "ещеодин", "строчка", "очень-очень-длинаястрочка"]
long_strings(strings_list)