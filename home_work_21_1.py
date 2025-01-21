def calculate_sum():
    total = 0
    while True:
        number = int(input("Введіть число: "))
        if number == 0:
            break
        total += number
    print(f"Сума чисел: {total}")

# Виклик функції
calculate_sum()