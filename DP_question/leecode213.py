# def rob(nums):
#     if len(nums)==1:
#         return nums[0]
#     if len(nums)==2:
#         return max(nums[0],nums[1])
#     nums1 = nums[0:-1]
#     nums2 = nums[1:]
#
#     temp1 = nums1[0]
#     temp2 = nums1[1]
#     temp5 = 0
#
#     for i in range(2,len(nums1)):
#
#         if i%2 == 0:
#             temp = max(temp5,temp1)
#             temp5 = temp1
#             temp1 = temp + nums1[i]
#         else:
#             temp = max(temp5, temp2)
#             temp5 = temp2
#             temp2 = temp + nums1[i]
#
#     temp3 = nums2[0]
#     temp4 = nums2[1]
#     temp6 = 0
#     for i in range(2,len(nums2)):
#         if i%2 == 0:
#             temp = max(temp6, temp3)
#             temp6 = temp3
#             temp3 = temp + nums2[i]
#
#         else:
#             temp = max(temp6, temp4)
#             temp6 = temp4
#             temp4 = temp + nums2[i]
#
#     print(temp1)
#     print(temp2)
#     print(temp3)
#     print(temp4)
#     ans = max(temp1,temp2,temp3,temp4)
#     print(ans)
#     return ans
#
# rob([6,6,4,8,4,3,3,10])
# rob([1,3,1,3,100])



# hash

# class Solution(object):
#     def rob(self,nums):
#         if len(nums)==1:
#             return nums[0]
#         if len(nums)==2:
#             return max(nums[0],nums[1])
#         nums1 = nums[0:-1]
#         nums2 = nums[1:]
#
#         temp1 = nums1[0]
#         temp2 = nums1[1]
#         temp5 = nums1[1]
#         hashtable1 = dict()
#         hashtable1[nums1[0]] = 0
#
#         for i in range(2,len(nums1)):
#             if i%2 == 0:
#                 temp1 = max(max(hashtable1),temp1)
#                 temp1 = temp1 + nums1[i]
#                 hashtable1[temp5] = i-1
#                 temp5 = temp1
#             else:
#                 temp2 = max(max(hashtable1), temp2)
#                 temp2 = temp2 + nums1[i]
#                 hashtable1[temp5] = i-1
#                 temp5 = temp2
#
#         temp3 = nums2[0]
#         temp4 = nums2[1]
#         hashtable2 = dict()
#         hashtable2[nums2[0]] = 0
#         temp6 = nums2[1]
#         for i in range(2,len(nums2)):
#             if i%2 == 0:
#                 temp3 = max(max(hashtable2), temp3)
#                 temp3 = temp3 + nums2[i]
#                 hashtable2[temp6] = i-1
#                 temp6 = temp3
#             else:
#                 temp4 = max(max(hashtable2), temp4)
#                 temp4 = temp4 + nums2[i]
#                 hashtable2[temp6] = i - 1
#                 temp6 = temp4
#         # print(temp1)
#         # print(temp2)
#         # print(temp3)
#         # print(temp4)
#         ans = max(temp1,temp2,temp3,temp4)
#         return ans

def rob(nums):
    if len(nums)==1:
        return nums[0]
    if len(nums)==2:
        return max(nums[0],nums[1])
    nums2 = nums[0:-1]
    nums1 = nums[1:]

    temp1 = nums1[0]
    temp2 = nums1[1]
    temp3 = nums1[2] + nums1[0]
    print(nums1)

    for i in range(3,len(nums1)):
        temp = max(temp1, temp2)
        temp1 = temp2
        temp2 = temp3
        temp3 = nums1[i] + temp

    temp4 = nums2[0]
    temp5 = nums2[1]
    temp6 = nums2[2] + nums2[0]
    for i in range(3,len(nums2)):
        temp = max(temp4, temp5)
        temp4 = temp5
        temp5 = temp6
        temp6 = nums2[i] + temp

    ans = max(temp1,temp2,temp3,temp4,temp5,temp6)
    print(ans)
    return ans

rob([6,6,4,8,4,3,3,10])
rob([1,3,1,3,100])




# def rob(nums):
#     if len(nums) == 1:
#         return nums[0]
#     if len(nums) == 2:
#         return max(nums[0], nums[1])
#     nums1 = nums[0:-1]
#     nums2 = nums[1:]
#
#     temp1 = nums1[0]
#     temp2 = nums1[1]
#     for i in range(2, len(nums1)):
#         if i % 2 == 0:
#             temp1 = temp1 + nums1[i]
#         else:
#             temp2 = temp2 + nums1[i]
#
#     temp3 = nums2[0]
#     temp4 = nums2[1]
#     for i in range(2, len(nums2)):
#         if i % 2 == 0:
#             temp3 = temp3 + nums2[i]
#         else:
#             temp4 = temp4 + nums2[i]
#     # print(temp1)
#     # print(temp2)
#     # print(temp3)
#     # print(temp4)
#     ans = max(temp1, temp2, temp3, temp4)
#     return ans