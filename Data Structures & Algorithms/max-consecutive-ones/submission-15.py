class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count = 0 
        max_count = 0

        for value in nums:             
             if value == 1:             
                current_count +=1
    
             else:
                if max_count < current_count:
                    max_count = current_count 
                current_count = 0

        if max_count < current_count:
            max_count = current_count

        return (max_count)