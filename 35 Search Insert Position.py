class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target < nums[0]:                                # target이 리스트 최소값 보다 작을때
            return 0

        if max(nums) < target :                           # target이 리스트 최대값 보다 클때
                return len(nums)

        if target in nums :                               # target이 리스트에 존재할 때
            return nums.index(target)

        for i in range(len(nums)) :
            if nums[i] > target :
                return i
              
              
             
# Runtime 55 ms Beats 88.20%
# Memory 14.7 MB Beats 39.65%
