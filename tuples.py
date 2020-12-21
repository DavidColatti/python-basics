t = (1,2,3) # tuples are similar to lists however are immutable
mylist = [1,2,3] # list

t = ('one', 2)
t[0] # 'one'
t[-1] # 2

t = ('a', 'a', 'b')
# print(t.count('a')) # 2
# print(t.index('a')) # 0 - first index that 'a' appears
# print(t.index('b')) # 2

mylist[0] = "New"
# print(mylist) # ['New', 2, 3]

t[0] = "New" # Can't reassign a value inside a tuple
# print(t) # TypeError: 'tuple' object does not support item assignment

