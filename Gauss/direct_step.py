def elem(i, j, k, arg, n):
    res = 0
    if k == -1:
        return arg[i][j]
    if i == k and k <= j <= n:
        res = elem(k, j, k - 1, arg, n) / elem(k, k, k - 1, arg, n)
    else:
        if k + 1 <= i <= n - 1 and k <= j <= n:
            res = elem(i, j, k - 1, arg, n) - elem(k, j, k, arg, n) * elem(i, k, k - 1, arg, n)
    return res

def calculation_matrix(arr,n):
    res = [[int(0) for j in range(n + 1)] for i in range(n)]
    for i in range(n):
        for j in range(n + 1):
            res[i][j] = elem(i, j, i, arr,n)
    return res