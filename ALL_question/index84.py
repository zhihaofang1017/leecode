def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    if min(heights) != 0:
        maxArea = len(heights)*min(heights)
    else:
        maxArea = max(heights)

    print(maxArea)
    while len(heights) > 1:
        short = min(heights)
        index = heights.index(short)
        print(heights[0:index])
        print(heights[index+1::])
        if solution(heights[0:index]) > solution(heights[index+1::]):
            if maxArea <= solution(heights[0:index]):
                maxArea = solution(heights[0:index])
            heights = heights[0:index]
        else:
            if maxArea <= solution(heights[index+1::]):
                maxArea = solution(heights[index+1::])
            heights = heights[index + 1::]
    print(maxArea)


def solution(heights):
    if heights == []:
        return 0
    height = min(heights)
    return height*len(heights)

largestRectangleArea([0,1,0,2,1,0,1,3,2,1,2,1])