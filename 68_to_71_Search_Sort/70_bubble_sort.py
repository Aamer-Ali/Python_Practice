def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp


nums = [5, 3, 8, 6, 7, 324, 5346453, 6547, 65, 875, 9, 8, 90, 0, 976, 7542, 423, 325, 45, 6, 58, 67, 98, 0, 980, 98,
        967, 54, 5, 32, 1, 2]
sort(nums)
print(nums)
