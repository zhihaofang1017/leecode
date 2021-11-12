def getMoneyAmount(n) :
    f = [[0] * (n + 1) for _ in range(n + 1)]
    print(f)
    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n + 1):
            temp_min = []
            for k in range(i, j):
                temp = max(f[i][k - 1], f[k + 1][j]) + k
                temp_min.append(temp)
                print("i:"+str(i)+" "+"j:"+str(j)+" "+"k:"+str(k)+" temp:"+str(temp))
            f[i][j] = min(temp_min)
            print(f)
    return f[1][n]

getMoneyAmount(4)
