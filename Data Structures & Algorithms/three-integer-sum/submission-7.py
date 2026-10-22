class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        print(nums)
        for i in range(len(nums)):

            if nums[i] > 0:  
                break

            if i > 0 and nums[i] != nums[i-1] or i == 0:

                left = i + 1
                right = len(nums) - 1
                target = nums[i]
                # print(target)
                while left < right:
                    # print(nums[left] + nums[right] + target)
                    if nums[left] + nums[right] + target == 0:
                        results.append([nums[i],nums[left], nums[right]])
                        # print(i,left,right)
                        left += 1
                        right -= 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1

                    elif nums[left] + nums[right] + target > 0:
                        right -= 1

                    else:
                        left += 1

        return results
