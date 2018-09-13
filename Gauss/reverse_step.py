def f(n, res):
    x = [0] * n
    x[n - 1] = res[n - 1][n]
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += res[i][j] * x[j]
        x[i] = res[i][n] - s
    return x
