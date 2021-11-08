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
        for i in range(len(height) - 2, high, -1):
            if height[i] >= temp2:
                temp2 = height[i]
                total = total - (temp - temp2)
            else:
                total = total - (temp - temp2)
    return total



# 双指针
def trap2(height):
    left_pointer = 0
    right_pointer = len(height) - 1
    left_max = height[0]
    right_max = height[-1]
    score = 0
    while left_pointer < right_pointer:
        if height[left_pointer] < height[right_pointer]:
            left_pointer = left_pointer + 1
            if height[left_pointer] >= left_max:
                left_max = height[left_pointer]
            else:
                score = score + (left_max - height[left_pointer])
        else:
            right_pointer = right_pointer - 1
            if height[right_pointer] >= right_max:
                right_max = height[right_pointer]
            else:
                score = score + (right_max - height[right_pointer])
        print(score)





def trap1(height):
    dp = [0, height[0], 0]
    for i in range(1, len(height)-1):
        print(i)
        if height[i] >= dp[1]:
            dp[0] = i
            dp[1] = height[i]
            continue
        else:
            dp[2] = dp[2] + (dp[1] - height[i])

    max_temp = dp[0]
    print(max_temp)
    print(dp[1])
    for i in range(len(height)-1,max_temp,-1):
        print(i)




trap2([4,2,0,3,2,5])
