class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        listt = []
        summ = 0
        for i in range(len(nums)):
            if nums[i] in listt:
                summ -= nums[i]
            else:
                summ += nums[i]
                listt.append(nums[i])
        return summ