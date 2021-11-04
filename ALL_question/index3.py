def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    s_list = list(s)
    s_len = len(s_list)
    temp_list = []
    possible_answer = []
    for i in range(0, s_len):
        if s_list[i] not in temp_list:
            temp_list.append(s_list[i])
        else:
            possible_answer.append(len(temp_list))
            position = temp_list.index(s_list[i])
            temp_list = temp_list[(position+1)::]
            temp_list.append(s_list[i])
    possible_answer.append(len(temp_list))
    return possible_answer[possible_answer.index(max(possible_answer))]

print(lengthOfLongestSubstring("1", "pwawkew"))