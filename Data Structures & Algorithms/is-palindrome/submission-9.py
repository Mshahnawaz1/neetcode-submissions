class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Method 1
        # L, R = 0, len(s)-1
        # while (L <= R):
        #     if not s[L].isalnum():
        #         L += 1
        #         continue
        #     if not s[R].isalnum(): 
        #         R -= 1
        #         continue
            
        #     if s[L].lower() != s[R].lower():
        #         return False
        #     L += 1
        #     R-= 1
        # return True

        #Method 2
        tmp = [x.lower() for x in s if x.isalnum()]
        return tmp == tmp[::-1]
