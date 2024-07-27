def abc(L, n):
    while True:
        if len(L) >= n:
            return L
        else:
            L.append(len(L)**2)


print(abc([20], 10))