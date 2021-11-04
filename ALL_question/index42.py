def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    temp = 0
    total = 0
    for i in range(len(height)):
        if height[i] > temp:
            temp = height[i]
        else:
            total = total + (temp - height[i])
    if height[-1] == temp:
        return total
    else:
        high = height.index(temp)
        temp2 = height[-1]
        total = total - (temp - temp2)
        for i in range(len(height)-2,high,-1):
            if height[i] >= temp2:
                temp2 = height[i]
                total = total - (temp - temp2)
            else:
                total = total - (temp - temp2)
    print(total)

trap([0,1,0,2,1,0,1,3,2,1,2,1])