# def maxProfit(prices):
#     """
#     :type prices: List[int]
#     :rtype: int
#     """
#     prices.append(0)
#     buy = []
#     sale = []
#     all = []
#     stack = []
#     Max = 0
#     for i in range(0, len(prices)):
#         if stack == []:
#             stack.append(prices[i])
#             continue
#
#         if prices[i] < stack[-1]:
#             if len(stack) == 1:
#                 stack.pop()
#             else:
#                 Max = Max + (stack[-1] - stack[0])
#                 buy.append(stack[0])
#                 sale.append(stack[-1])
#                 all.append(stack[0])
#                 all.append(stack[-1])
#                 stack.clear()
#         stack.append(prices[i])
#     print(Max)
#     print(buy)
#     print(sale)
#     print(all)
#     if len(sale) > 2:
#         Max = 0
#         for i in range(len(sale) - 1):
#             for j in range(i, len(buy)):
#                 temp = 0
#                 temp = temp + (sale[j] - buy[i])
#                 temp = temp + maxProfit2(all[2*j+2::])
#                 if temp >= Max:
#                     Max = temp
#     print(Max)
#     return Max
#
# def maxProfit2(prices):
#     """
#     :type prices: List[int]
#     :rtype: int
#     """
#     if prices == []:
#         return 0
#     stack = [prices[0]]
#     Max = 0
#     for i in range(1, len(prices)):
#         if prices[i] < stack[-1]:
#             stack.pop()
#             stack.append(prices[i])
#         else:
#             if prices[i] - stack[0] > Max:
#                 Max = prices[i] - stack[0]
#     return Max
def maxProfit(prices):
    n = len(prices)
    buy1 = buy2 = -prices[0]
    sell1 = sell2 = 0
    print(buy1)
    for i in range(1, n):
        buy1 = max(buy1, -prices[i])
        sell1 = max(sell1, buy1 + prices[i])
        buy2 = max(buy2, sell1 - prices[i])
        sell2 = max(sell2, buy2 + prices[i])
    return sell2

maxProfit([3,3,5,0,0,3,1,4])