class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)

        # From back to front, find the first number < nums[i + 1].
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1

        # From back to front, find the first number > nums[i], swap it with nums[i].
        if i >= 0:
            for j in range(n - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        return nums
Sol=Solution()
print(Sol.nextPermutation([1,8,5,6]))