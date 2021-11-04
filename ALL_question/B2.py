def Computer_Game():
    result = []
    test_num = int(input())
    for i in range(test_num):
        row_num = int(input())
        line1 = list(input())
        line2 = list(input())
        if line2[row_num-1]=='1':
            result.append("NO")
            break
        for j in range(row_num - 1):
            if(line1[j]=='1' and line2[j]=='1'):
                result.append("NO")
                break
        if len(result)!= i+1:
            result.append("YES")
        print(result)
    txt = ''
    for i in range(len(result)-1):
        txt = txt + result[i] + '\n'
    txt = txt + result[-1]
    return txt




print(Computer_Game())