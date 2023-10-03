class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c.lower() for c in s if c.isalnum()])
        print(s)

        return s == s[::-1]
        