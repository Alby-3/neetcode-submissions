class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        s=[]
        hashmap=defaultdict(int)
        for i in nums:
            hashmap[i]+=1
        for key in hashmap:
            if hashmap[key]>len(nums)/3:
                s.append(key)
        return s
        
        

        
