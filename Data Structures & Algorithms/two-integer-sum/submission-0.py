class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i,num in enumerate(nums):
            if target - num in track:
                return [track[target - num], i]

            if num not in track:
                track[num] = i

        return [-1,-1]

            