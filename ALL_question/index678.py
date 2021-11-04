def checkValidString(s):
    """
    :type s: str
    :rtype: bool
    """
    left_count = 0
    right_count = 0
    star_count = 0
    for item in list(s):
        if item == "(":
            right_count += 1
        elif item == ")":
            left_count += 1
        else:
            star_count += 1
    if abs(left_count - right_count) > star_count:
        return False

    print(left_count)
    print(right_count)
    print(star_count)
    list_s = list(s)

    temp1 = 0
    temp2 = 0
    temp3 = 0
    for item in list_s:
        if item == "(":
            temp1 += 1
        elif item == ")":
            temp2 += 1
            if temp1 + temp3 < temp2:
                print("aaaa")
                return False
        else:
            temp3 += 1
    print(list_s)
checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())")
