from time import monotonic


def find_line(fw):
    for i in range(len(words)):
        if words[i] == fw:
            return i  # вернуть позицию слова
    return -1


def find_bin_rec(fw, x, y):  # recursia
    if x == y and words[x] != fw: return -1
    m = x + (y-x)//2
    if fw == words[m]: return m
    if fw > words[m]: return find_bin(fw,m+1,y)
    if fw < words[m]: return find_bin(fw,x,m-1)


def find_bin(fw, x, y):  # без рекурсии - циклом
    # тут напишите функцию бинарного поиска
    # без использования рекурсии, циклом while
    # если слово не найдено
    # то возвращается позиция -1
    return -1


words = open("./words.csv", mode="r", encoding="windows-1251").read().split('\n')

find_words = [
    "ящик", "абак", "кукуруза", "комарик", "як", 
    "ящик", "яхта", "яхта", "яхта", "яхта"
]
find_words *= 50

a = monotonic()
# results = [find_line(word) for word in find_words]  # 8.7 sek
results = [find_bin_rec(word,0,len(words)-1) for word in find_words]  # 0.007 sek
# results = [find_bin(word) for word in find_words]  # проведите замеры своей функции
b = monotonic()

print(round(b-a, 3))
# print(results)
