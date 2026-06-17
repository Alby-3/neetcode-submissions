class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}
        if len(s)!=len(t):
            return False
        else:
            for c in s :
                if c in hashmap:
                     hashmap[c]+=1
                else:
                    hashmap[c]=1
            for k in t:
                if k in hashmap:
                    hashmap[k]-=1
                else:
                    return False
            for value in hashmap.values():
                if value>0:
                    return False
           
            return True
        