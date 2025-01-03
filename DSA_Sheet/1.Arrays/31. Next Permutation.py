class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l<= 2:
            return nums.reverse()
        pointer = l - 2
        while pointer >= 0 and nums[pointer] >= nums[pointer+1]:
            pointer -= 1
        if pointer == -1:
            return nums.reverse()
        for i in range(l - 1,pointer,-1):
            if nums[pointer]<nums[i]:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                break
        nums[pointer+1:]= reversed(nums[pointer+1:])
solution = Solution()

nums = [1, 2, 3]
solution.nextPermutation(nums)
print(nums)