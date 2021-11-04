def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    result = 0
    for i in range(0,len(height)):
        for j in range(i,len(height)):
            if min(height[i],height[j])*(j-i) > result:
                result = min(height[i],height[j])*(j-i)
    print(result)

