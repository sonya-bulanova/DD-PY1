import random as rand

def get_unique_list_numbers() -> set[int]:
    list_ = list()
    while len(list_) != 15:
        val = rand.randrange(-10, 11)
        if val not in list_:
            list_.append(val)
    return list_
      # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
