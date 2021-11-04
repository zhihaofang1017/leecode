def Hit():
    num = input()
    num = int(num)
    count = 0
    count = count + num//100
    num = num - 100*count
    temp = num//20
    num = num - 20*temp
    count = count+temp
    temp = num // 10
    num = num - 10 * temp
    count = count + temp
    temp = num // 5
    num = num - 5 * temp
    count = count + temp
    temp = num // 1
    num = num - 1 * temp
    count = count + temp
    return count

print(Hit())