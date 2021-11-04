def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    position = 0
    while position != len(nums) - 1:
        if nums[position] != 0:
            position = position + 1
        else:
            judge = 0
            for i in range(0, position):
                if i + nums[i] > position :
                    position = position + 1
                    judge = judge + 1
                    break
            if judge == 0:
                print("1")
                return False
    return True
canJump([2,0,0])