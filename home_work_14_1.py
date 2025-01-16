def rectangle_area(length, width):

    if length <= 0 or width <= 0:
        raise ValueError("Довжина і ширина повинні бути позитивними числами.")
    return length * width