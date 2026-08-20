class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_map = {} 
        
               
        for word in strs:
            # Sort the word to get the key
            sorted_word = ''.join(sorted(word))
            
            # Check if key exists, if not create empty list
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []
            
            # Add the word to the list
            anagram_map[sorted_word].append(word)
        
        # Return just the values (the lists of anagrams)
        return list(anagram_map.values())