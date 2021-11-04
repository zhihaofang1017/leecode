def Beautiful_Matrix():
    result = []
    for i in range(5):
        a = input()
        a = a.replace(" ","")
        a = list(a)
        result.append(a)
        for j in range(5):
            if result[i][j] == '1':
                return abs(i-2)+abs(j-2)

print(Beautiful_Matrix())