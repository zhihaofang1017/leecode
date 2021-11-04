def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    stack = [prices[0]]
    Max = 0
    for i in range(1, len(prices)):
        if prices[i] < stack[-1]:
            stack.pop()
            stack.append(prices[i])
        else:
            if prices[i] - stack[0] > Max:
                Max = prices[i] - stack[0]
    print(Max)
maxProfit([7,1,5,3,6,4])