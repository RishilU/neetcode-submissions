def remove_fourth_character(word: str) -> str:
    return word[:3] + word[4:]
  

#word[:3] = characters at indices 0, 1, 2 (first 3 characters)
#word[4:] = characters from index 4 onward (everything after the 4th character)
#Concatenate them to skip index 3 (the 4th character)#


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
