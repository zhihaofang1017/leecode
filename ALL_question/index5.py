def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    list_s = list(s)
    max_num = 1
    result_list = []
    for i in range(0, len(list_s)):
        temp = 1
        list1 = list_s[0:i]
        list2 = list_s[i+1:len(list_s)]
        len_min = min(len(list1), len(list2))
        for j in range(0, len_min):
            if list1[-1-j] == list2[0+j]:
                temp += 2
            else:
                break
        if temp >= max_num:
            result_list = list_s[i-int((temp+1)/2)+1:i+int((temp+1)/2)]
            max_num = temp

        if i != len(list_s)-1:
            if list_s[i] == list_s[i+1]:
                temp2 = 2
                list2 = list_s[i + 2:len(list_s)]
                len_min = min(len(list1), len(list2))
                for j in range(0, len_min):
                    if list1[-1 - j] == list2[0 + j]:
                        temp2 += 2
                    else:
                        break
                if temp2 >= max_num:
                    result_list = list_s[i-int(temp2/2)+1:i+int(temp2/2)+1]
                    max_num = temp2
    result = ''.join(result_list)
    return result

longestPalindrome("abbc")

