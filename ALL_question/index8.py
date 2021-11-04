def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    import re
    judge = 0

    s = s.replace(' ', '')
    s_list = list(s)

    if s_list[0] == "-":
        judge = 1
        s_list = s_list[1:]
    elif s_list[0] == "+":
        s_list = s_list[1:]
    result_list = []

    for i in range(0,len(s_list)):
        if re.match('\d',s_list[0]) != None:
            result_list.append(s_list[0])
            s_list = s_list[1:]
        else:
            break
    result = 0

    for i in range(0, len(result_list)):
        result = result + int(result_list[len(result_list)-i-1])*(10**i)
    print(result)
    if result > 2**31-1:
        return 2**31 - 1
    elif result < -2**31:
        return -2147483648
    if judge == 0:
        return result
    else:
        return -result

myAtoi("   +0 123")