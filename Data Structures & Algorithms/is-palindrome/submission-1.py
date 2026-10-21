class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cs = ''.join([char for char in s if char.isalnum()])
        cs = cs.lower()
        
        left,right = 0, len(cs) - 1

        while left < right:
            if cs[left] != cs[right]:
                return False

            left += 1
            right -= 1

        return True
        