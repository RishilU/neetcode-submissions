class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
          currentStreak, longestStreak = 0,0;
          
          for i in range(len(nums)):
                if nums[i] == 1:
                    currentStreak+=1;
                else:  # Hit a 0
                     if currentStreak > longestStreak: 
                          longestStreak = currentStreak
                     currentStreak = 0

          if currentStreak > longestStreak:
               longestStreak = currentStreak

          return longestStreak         


                
               
                   



        