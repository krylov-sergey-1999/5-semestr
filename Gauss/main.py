from Gauss.input import *
from Gauss.direct_step import *
from Gauss.reverse_step import *

n = in_characteristic()  # вводим порядок матрицы
arr = in_matrix(n)  # вводим матрицу
m = calculation_matrix(arr, n)  # вычисляем матрицу при помощи прямого хода
for i in m:
    print(i)
print(f(n,m))

