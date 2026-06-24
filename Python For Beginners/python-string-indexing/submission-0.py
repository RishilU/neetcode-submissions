def print_first_char(word: str) -> None:
    print(word[0])

def print_second_char(word: str) -> None:
    print(word[1])

def print_last_char(word: str) -> None:
    print (word[len(word)-1])

   # //Way that works is [len(word)-1 gets us the specific INDEX (character) of what we need, but that's still a #]
   # //to get it into specific letter, we use the outside word 


# do not modify below this line
print_first_char("hello")
print_second_char("hello")
print_last_char("hello")

print_first_char("yay")
print_second_char("yay")
print_last_char("yay")
