# 0, 1 and 2 are Red, White, Blue respectively


def sortColors(self, nums: list[int]) -> None:
    """
    Modify nums in-place instead.
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):

            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums
