class Solution(object):
    def search(self, nums, target):

        left, right = 0, len(nums) - 1
        mid = 0

        while (left <= right):

            mid = left + ((right - left) // 2)

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1






