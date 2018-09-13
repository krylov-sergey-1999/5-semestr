# Мы должны ввести матрицу [n*(n+1)]

def in_matrix(n):
    arr = []
    for i in range(n):
        s = list(map(int, input().split()))
        while len(s) != n + 1:
            print("Введите строку заново, вы ввели недостаточно элементов.")
            s = list(map(int, input().split()))
        arr.append(s)
    return arr


def in_characteristic():
    x = int(input("Введите порядок матрицы: "))
    return x
