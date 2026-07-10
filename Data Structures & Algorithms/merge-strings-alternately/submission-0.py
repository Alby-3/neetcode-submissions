class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=len(word1)
        b=len(word2)
        l1,l2=0,0
        s=""
        while l1<a and l2<b:
            s+=word1[l1]
            l1+=1
            s+=(word2[l2])
            l2+=1
        while l1<a:
            s+=word1[l1]
            l1+=1
        while  l2<b:
            s+=word2[l2]
            l2+=1
            
        return s




        

        
        