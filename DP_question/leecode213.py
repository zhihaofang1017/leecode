def rob(nums):
    if len(nums) <= 3:
        return max(nums)
    nums1 = nums[0:-1]
    nums2 = nums[1:]

    temp1 = nums1[0]
    temp2 = nums1[1]

    for i in range(3, len(nums1)):
        if i % 2 == 1:
            temp1 = temp1 + nums1[i]
        else:
            temp2 = temp2 + nums1[i]

    temp3 = nums2[0]
    temp4 = nums2[1]
    for i in range(3, len(nums2)):
        if i % 2 == 1:
            temp3 = temp3 + nums2[i]
        else:
            temp4 = temp4 + nums2[i]

    temp5 = nums1[0]
    temp6 = nums1[1]

    for i in range(2, len(nums1)):
        if i % 2 == 0:
            temp5 = temp5 + nums1[i]
        else:
            temp6 = temp6 + nums1[i]

    temp7 = nums2[0]
    temp8 = nums2[1]
    for i in range(2, len(nums2)):
        if i % 2 == 0:
            temp7 = temp7 + nums2[i]
        else:
            temp8 = temp8 + nums2[i]
    print(temp1)
    print(temp2)
    print(temp3)
    print(temp4)
    print(temp5)
    print(temp6)
    print(temp7)
    print(temp8)
    ans = max(temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8)
    return ans


# rob([1, 2, 3, 1])
rob([6, 3, 10, 8, 2, 10, 3, 5, 10, 5, 3])
# rob([1, 3, 1, 3, 100])
