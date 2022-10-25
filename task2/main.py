
def get_count_char(str_):
    dict_str = {}
    str_ = str_.lower()
    for letter in str_:
        if letter.isalpha():
            dict_str[letter] = str_.count(letter)
    return(dict_str)
    # TODO посчитать количество каждой буквы в строке в аргументе str_


def get_procentage(dict_str):
    for letter in dict_str:
        dict_str[letter] = round(dict_str[letter]*100/sum(dict_str.values()), 2)
    return(dict_str)

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
dict = get_count_char(main_str)
print(get_procentage(dict))