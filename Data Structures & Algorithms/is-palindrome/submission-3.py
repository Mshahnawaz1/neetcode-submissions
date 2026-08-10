class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        s = [x for x in s if x.isalpha() or x.isdigit()]
        return s == s[::-1]