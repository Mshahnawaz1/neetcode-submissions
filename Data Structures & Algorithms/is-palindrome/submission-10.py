class Solution:
    def isPalindrome(self, s: str) -> bool:
        o = [x.lower() for x in s if x.isalnum()]
        return o == o[::-1]