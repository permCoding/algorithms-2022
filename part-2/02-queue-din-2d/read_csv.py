import csv


def get_tpl(file_name, sep=','):
    with open(file_name) as f:
        lines = f.readlines()
    return [tuple(map(int, line.split(sep))) for line in lines[1:]]


def get_lst(file_name, sep=','):
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=sep)
        return [line for line in reader][1:]


def get_lst_dct(file_name, sep=','):
    with open(file_name, 'r', encoding='utf8') as f:
        reader = csv.DictReader(f, delimiter=sep)
        return [line for line in reader]


lst = get_tpl('./csv/input.csv')
for elm in lst:
    print(elm)

lst = get_lst('./csv/input.csv')
for elm in lst:
    print(elm)

lst = get_lst_dct('./csv/input.csv')
for elm in lst:
    print(elm)

print(lst[0]['p'])
print(int(lst[0]['p'])/int(lst[0]['w']))
