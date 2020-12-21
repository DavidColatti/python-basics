# Sets are unordered collections of unique elements
myset = set()
myset.add(1)
# print(myset) # {1}
myset.add(2)
# print(myset) # {1, 2}

myset.add(2) # Adding an element that currently exists
# print(myset) # {1, 2} - It won't repeat element values

mylist = [1,1,1,1,1,2,2,2,2,3,3,3]
# print(set(mylist)) # {1, 2, 3}