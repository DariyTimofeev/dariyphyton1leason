def contains_hand(hand):
    result = 'hand' in hand

    print("Есть ли 'hand' в списке:", result)

    return result

values_list = ["foot", "hand", "head", "eye"]
contains_hand(values_list)