def binary_search(nums, target):
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
b = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]


binary_search(d,10) 