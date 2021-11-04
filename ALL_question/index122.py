def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    prices.append(0)
    stack = []
    Max = 0
    for i in range(0, len(prices)):
        if stack == []:
            stack.append(prices[i])
            continue

        if prices[i] < stack[-1]:
            if len(stack) == 1:
                stack.pop()
            else:
                Max = Max + (stack[-1] - stack[0])
                stack.clear()
        stack.append(prices[i])
    print(Max)
maxProfit([7,6,4,3,1])