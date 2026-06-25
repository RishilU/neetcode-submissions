from typing import List # this is used to add type hints for List type

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
  for num in elements:
    my_list.append(num)
  return my_list
  #this lets us add list 1 by 1 
  
  
  
  #my_list.append(elements)
  #return(my_list)
# thi solution adds the entire nested list at once,  including []


# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))
