class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create empty HashMap to store number → index pairs
        num_map = {}

        # Loop through each element in the array
        # i = index (0, 1, 2, ...)
        for i in range(len(nums)):
            
            # Calculate the "complement" - the number we NEED to find
            # Example: if target=9 and current number=2, we need 7
            complement = target - nums[i]
        
            # Check: "Have I seen the complement before?"
            if complement in num_map:
                # YES! We found a pair!
                # num_map[complement] = the index of the complement
                # i = the index of current number
                # Return both indices as [smaller_index, larger_index]
                return [num_map[complement], i]
        
            # NO, we haven't seen the complement yet
            # So remember THIS number and its index for later
            # nums[i] = the current number
            # i = its index
            # Store as: number → index
            num_map[nums[i]] = i