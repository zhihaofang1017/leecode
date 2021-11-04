def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    i1 = 0
    i2 = 0
    judge = 0
    if (len(nums1)+len(nums2))%2 == 0:
        middle_index = (len(nums1)+len(nums2))/2
    else:
        middle_index = (len(nums1)+len(nums2)+1)/2
    temp = 0
    while temp < middle_index:
        num1 = getNum(nums1, i1)
        num2 = getNum(nums2, i2)
        if num1 >= num2:
            print("a")
            if i1 == 0:
                temp = temp + len(nums1) - getIndex(nums1, i1)
            else:
                temp = temp + getIndex(nums1, i1-1) - getIndex(nums1, i1)
            i1 += 1
            judge = 1
        else:
            print("b")
            if i2 ==0:
                temp = temp + len(nums2) - getIndex(nums2, i2)
            else:
                temp = temp + getIndex(nums2, i2-1) - getIndex(nums2, i2)
            i2 += 1
            judge = 0
        print(temp)
    print(i1)
    if judge == 1:
        print(getIndex(nums1, i1))
    print(temp)



def getNum(nums, i):
    if i == 0:
        return nums[-1]
    else:
        return nums[int(len(nums)/(2**i))]

def getIndex(nums, i):
    if i == 0:
        return len(nums) - 1
    else:
        return int(len(nums)/(2**i))

findMedianSortedArrays([1, 3, 5, 7, 9, 11, 13], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])