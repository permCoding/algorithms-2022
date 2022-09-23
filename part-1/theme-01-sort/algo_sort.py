from time import sleep
from random import randint


def get_lst(count):
    return [randint(0, count) for _ in range(count)]


def sort_sleep():
    sleep(2)  # имитация измеряемой функции
    return True


def sort_insert(lst):
    pass
    pass
    return lst


def sort_select():
    pass
    pass
    return True


def sort_bubble(lst):
    n = len(lst)
    for j in range(1, n):
        for i in range(n-j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst


def sort_bubble_plus(lst):
    ''' усовершенствованная сортировка пузырьком '''
    n = len(lst)
    for j in range(1, n):
        swap = False  # была ли замена элементов
        for i in range(n-j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swap = True
        if not swap:  # всё уже отсортировано
            break
    return lst


def sort_bubble_while(lst):
    ''' усовершенствованная сортировка пузырьком while'''
    n = len(ls
    swap = False
    j = n-1  # правая граница
    while not(swap):
        swap = False
        for i in range(0, j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swap = True
        j -= 1
    return lst


def sort_sh():
    """
    написать самостоятельно
    провести эксперимент
    """
    return


def quick_sort():
    return
