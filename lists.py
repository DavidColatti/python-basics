my_list = [1,2,3]
my_list = ["STRING", 100, 23.2]
len(my_list) # 3
my_list = ['one', 'two', 'three']

my_list[0] # 'one'
my_list[1:] # ['two', 'three']

another_list = ['four', 'five']
my_list + another_list # ['one', 'two', 'three', 'four', 'fiver']

new_list = my_list + another_list
new_list[0] = new_list[0].upper()
# print(new_list) # ['ONE', 'two', 'three', 'four', 'five']

new_list.append('six') # ADDS another element to the end of the list
# print(new_list) # ['ONE', 'two', 'three', 'four', 'five', 'six']

new_list.pop() # Removed item from end of the list
# print(new_list) # ['ONE', 'two', 'three', 'four', 'five']

popped_item = new_list.pop() # assigns the popped item to a variable
# print(popped_item) # 'five'

new_list.pop(0) # pass index position inside pop to specify the element
# print(new_list) # ['two', 'three', 'four']

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [3, 4, 1, 8, 2]

new_list.sort() # does not return anything, it modifies the existing list
num_list.sort()
my_sorted_list = new_list
my_sorted_num_list = num_list
# print(my_sorted_list) # ['a', 'b', 'c', 'e', 'x']
# print(my_sorted_num_list) # [1, 2, 3, 4, 8]

new_list.reverse()
num_list.reverse()
my_reversed_list = new_list
my_reversed_num_list = num_list
# print(my_reversed_list) # ['x', 'e', 'c', 'b', 'a']
# print(my_reversed_num_list) # [8, 4, 3, 2, 1]