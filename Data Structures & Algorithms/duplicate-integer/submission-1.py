class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for num in nums:
            if num in hashmap:   
                hashmap[num]+=1
            else:
                hashmap[num]=1
        for value in hashmap.values():
            if value>1:
                return True
        return False
            