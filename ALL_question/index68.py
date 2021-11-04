def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    count_list = []
    temp = []
    count = 0
    for i in range(len(words)):
        count = count + len(words[i])
        if count > maxWidth:
            count_list.append(temp)
            temp = []
            count = len(words[i])
        if i == len(words) - 1:
            count_list.append(temp)
        count = count + 1
        temp.append(len(words[i]))

    print(count_list)
    a = solution(count_list, maxWidth)

    result1 = []
    b = 0
    c = 0
    for i in range(len(count_list)):
        temp_str = ""
        for k in range(len(count_list[i])):
            temp_str = temp_str + words[b]
            if k != len(count_list[i]) - 1 or len(count_list[i]) == 1:
                temp_str = temp_str + a[c]*" "
                c = c + 1
            b = b + 1
        temp_str = temp_str[0:maxWidth]
        result1.append(temp_str)

    print(result1)
    if len(result1[-1]) != maxWidth:
        result1[-1] = result1[-1] + " "*(maxWidth - len(result1[-1]))
    print(a)
    print(result1)




def solution(count_list, maxWidth):
    result = []
    for i in range(len(count_list) - 1):
        interval = 0
        total = 0
        count = 0
        if len(count_list[i]) == 1:
            interval = 1
        else:
            interval = len(count_list[i]) - 1

        for j in range(len(count_list[i])):
            total = total + count_list[i][j]

        judge = 0
        import copy
        total1 = copy.deepcopy(total)
        while (maxWidth - total) % interval != 0:
            total = total + 1
            count = count + 1
            judge = 1

        print(count)
        print(total)
        print(total1)
        for k in range(interval):
            if count != 0:
                result.append(((maxWidth - total1) // interval) + 1)
                count = count - 1
            else:
                result.append(((maxWidth - total1) // interval))
    for i in range(len(count_list[-1])):
        result.append(1)
    print(result)
    return result


fullJustify(["a"], 1)
