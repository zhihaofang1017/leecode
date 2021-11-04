# def candy(ratings):
#     result = [1]
#     for i in range(1,len(ratings)):
#         result.append(1)
#         if ratings[i - 1] > ratings[i]:
#             if result[i - 1] <= result[i]:
#                 result[i - 1] = result[i - 1] + 1
#         elif ratings[i - 1] < ratings[i]:
#             result[i] = result[i-1] + 1
#     a = 0
#     for item in result:
#         a = a +item
#     print(a)
#     print(result)
# def candy(ratings):
#     result = 1
#     for i in range(1,len(ratings)):
#         if ratings[i - 1] == ratings[i]:
#             result = result + 1
#         else:
#             result = result + 2
#     print(result)
# def candy(ratings):
#     temp = [ratings[0],ratings[1]]
#     judge = 0
#     result = [1]
#     for i in range(1,len(ratings)):
#         print(result)
#         temp.append(ratings[i])
#         if judge == 0:
#             if temp[-1] > temp[-2]:
#                 judge = 1
#             elif temp[-1] < temp[-2]:
#                 judge = 2
#             else:
#                 temp = temp[-1]
#         elif judge == 1:
#             if temp[-1] < temp[-2]:
#                 temp = [temp[-2],temp[-1]]
#                 judge = 0
#         elif judge == 2:
#             if temp[-1] > temp[-2]:
#                 temp = [temp[-2],temp[-1]]
#                 judge = 0
#
#         if ratings[i - 1] < ratings[i]:
#             if ratings[i] == temp[-1] and judge == 1:
#                 result.append(len(temp))
#             else:
#                 temp = [ratings[i - 1], ratings[i]]
#                 judge = 0
#                 result.append(1)
#         elif ratings[i - 1] > ratings[i]:
#             if ratings[i] == temp[-1] and judge == 2:
#                 result = result + len(temp)
#             else:
#                 temp = [ratings[i - 1], ratings[i]]
#                 result = result + 1
#         else:
#             result = result + 1
#             judge = 0
#             temp = [ratings[i]]
#     print(result)



def candy(ratings):
    result = 1
    temp1 = 1
    temp1_max = 3
    temp2 = 1
    temp = 1
    for i in range(1,len(ratings)):
        print(result)
        if ratings[i - 1] == ratings[i]:
            result = result + 1
            temp = 1
            temp1 = 2
            temp2 = 2
        elif ratings[i - 1] < ratings[i]:
            temp2 = 1
            temp1 = temp1 + 1
            result = result + temp1
            temp = temp + 1
            if temp1 >= temp1_max:
                temp1_max = temp1
        else:
            temp1 = 1
            print(str(temp) + "aaa")
            if temp == 1:
                result = result + temp2
                temp2 = temp2 + 1
                if temp2 > temp1_max:
                    result = result + 1
            else:
                temp2 = temp2 + 1
                result = result + 1
            temp = 1
            print(str(temp2)+"n")
    print(result)
candy([1,2,87,87,87,2,1])
# candy([1,0,2])
candy([1,2,3,5,4,3,2,1])