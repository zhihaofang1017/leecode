def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    result = []
    count = 0
    count2 = 0
    for i in range(0,len(nums)):
        if nums[i] == 2:
            result.append(nums[i])
            count2 = count2 + 1
        elif nums[i] == 0:
            result.insert(0, nums[i])
            count = count + 1
            count2 = count2 + 1
    for i in range(0, len(nums)-count2):
        result.insert(count, 1)
    nums = result
    print(nums)
sortColors([2,0,2,1,1,0])