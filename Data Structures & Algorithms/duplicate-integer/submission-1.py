class Solution:
    def hasDuplicate(self, input_array: List[int]) -> bool:
       
        numbers_i_have_seen = set()

        for current_number in input_array: # ← current_number = 1 (first element)
            if current_number in numbers_i_have_seen: # Is 1 in {}? NO
                return True;
            numbers_i_have_seen.add(current_number)  # ← ADD 1 to set
        
        return False;    


        