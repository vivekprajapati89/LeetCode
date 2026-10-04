class Solution:
    def isPalindrome(self, x: int) -> bool:
        fX = x
        if x < 0:
            return bool(0)
        result = 0

        while x > 0:
            rem = x % 10
            result = result * 10 + rem
            x = x // 10
        
        if result == fX:
            return bool(1)

        return bool(0)

        