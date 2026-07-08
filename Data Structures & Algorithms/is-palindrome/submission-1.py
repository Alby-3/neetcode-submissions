class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        a=s.lower()
        while left<right:
            if not a[left].isalnum():
                left+=1
                continue 
            if not a[right].isalnum():
                right-=1
                continue
            if a[left]==a[right]:
                left+=1
                right-=1
            else:
                return False
        return True