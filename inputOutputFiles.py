# myfile = open('myfile.txt')
# print(myfile.read()) # `Hello this is a text file \nthis is the second line \nthis is the third line`

# To call .read() method twice, you need to reset the cursor back to the beginning of the txt file:
# myfile.read()
# myfile.seek(0)
# myfile.read()

# myfile.readlines() # ['Hello this is a text file\n', 'this is the second line\n', 'this is the third line']

# myfile.close() # need to manually close this file to open another one

# Read files from another directory in your computer
# with open('/Users/davidcolatti/Desktop/TxtFile.txt') as my_new_file:
#     content = my_new_file.read()
    # print(content) # Hey from desktop

# mode is a permission: 
# w = write a file
# a = append to a file
# r = read a file
# r+ = read and writing
# w+ writing and reading (overwrites existing files or creates a new file)
# with open('myfile.txt', mode='r') as myfile:
#     content = myfile.read()
    # print(content) # 'Hello this is a text file \nthis is the second line \nthis is the third line'

# Read
# with open('my_new_file.txt', mode='r') as f:
#     f.read()

# Add a new line
# with open('my_new_file.txt', mode='a') as f:
#     f.write("\nFour on fourth")

# with open('my_new_file.txt', mode='r') as f:
#     print(f.read()) # 'One of first \nTwo on second \nThree on third \nFour on fourth'

# overrides an existing file or creates a new one
# with open('asdjldasljasd.txt', mode='w') as f:
#     f.write("I Created this file!")