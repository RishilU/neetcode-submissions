def first_n_characters(s: str, n: int) -> str:
  return(s[:n])

  #word let's say is frog, n=2
  # whole string (s) - n = first n characters 

def last_n_characters(s: str, n: int) -> str:
  return(s[-n:])

# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))
