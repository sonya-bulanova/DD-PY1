import json

INPUT_FILE = "output.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename, "r") as file:
        ls = []
        for line in file:
            line = line.replace(new_line, "")
            ls.append(line.split(delimiter))
    for i in range(1, len(ls)):
        ls[i] = dict(zip(ls[0], ls[i]))
    fw = open("output.txt")
    return ls

    # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE)[1:], indent=4, ensure_ascii=False))
