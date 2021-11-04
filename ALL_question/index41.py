def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # nums = list(set(nums))
    # import copy
    # nums_2 = copy.deepcopy(nums)
    # for i in range(len(nums)):
    #     if nums[i] <= 0:
    #         nums_2.remove(nums[i])
    # count = 1
    # while count != 0:
    #     count = 0
    #     for item in nums_2:
    #         if item >= len(nums_2) + 1:
    #             nums_2.remove(item)
    #             count = count + 1
    #     print(nums_2)

    n = len(nums)
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1

    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])

    for i in range(n):
        if nums[i] > 0:
            return i + 1
    return n + 1
firstMissingPositive([1,2,3,6])
