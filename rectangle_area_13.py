def rectangle_area(length, width):
    """
    Обчислює площу прямокутника.
    :param length: Довжина прямокутника (число).
    :param width: Ширина прямокутника (число).
    :return: Площа прямокутника.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Довжина і ширина повинні бути додатними числами.")
    return length * width

if __name__ == "__main__":
    # Пример использования функции
    length = 5
    width = 3
    print(f"Площадь прямоугольника с длиной {length} и шириной {width}: {rectangle_area(length, width)}")