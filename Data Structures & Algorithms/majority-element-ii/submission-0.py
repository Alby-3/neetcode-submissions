class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size=len(nums)/3
        s=[]
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        for key in hashmap:
            if hashmap[key]>size:
                s.append(key)
        return s
        
        

        
