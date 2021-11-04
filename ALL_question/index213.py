def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 3:
        return max(nums)

    temp = [nums[0], nums[1]]
    judge = [1, 0]
    for i in range(2, len(nums)):
        index = temp.index(max(temp[:-1]))
        if judge[index] == 0 or temp[:-1].count(max(temp[:-1])) > 1:
            judge.append(0)
        else:
            judge.append(1)
        a = nums[i] + max(temp[:-1])
        temp.append(a)
    print(temp)
    print(judge)
    if judge[-1] == 0:
        return max(temp)
    else:
        last_max = 0
        for i in range(1, len(judge) - 2):
            if judge[i] == 0 and nums[-1] + temp[i] >= last_max:
                last_max = nums[-1] + temp[i]
            elif judge[i] == 1 and nums[-1] + temp[i] - nums[0] >= last_max:
                last_max = nums[-1] + temp[i] - nums[0]
        temp[-1] = last_max
    print(temp)
    return max(temp)


rob([2,1,2,6,1,8,10,10])
