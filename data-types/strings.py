# string = 'hello\nworld'
# print(len(string))

string = "Hello World"
# Indexing and Slicing with Strings
string[0] # "H"
string[8] # "r"

# Reverse Indexing
string[-2] #l
string[-3] #r

# Slicing
#[start:stop:step]
string = "abcdefghijk"
string[2:] # "cdefghijk"
string[:3] # "abc"
string[3:6] # "def"
string[1:3] # "bc"
string[3:-2] # "defghi"
string[::2] # "acegik" it skips 2 
string[2:7:2] # "ceg"
string[::-1] # "kjihgfedcba" reverses a string

# Immutability
name = "Sam"
last_letters = name[1:]
# "P" + last_letters # Concat to make "Pam"

letter = "z"
letter * 10 # "zzzzzzzzzz"

x = "Hello World"
x.upper() # "HELLO WORLD"
x.lower() # "hello world"
x.split() # ["Hello", "World"]

x = "Hi this is a string"
x.split("is")
x.split("i") # ['H', ' th', 's ', 's a str', 'ng']

# Print Formatting Strings
# "This is a string {}".format("INSERTED") # "This is a string INSERTED"
# "The {2} {1} {0}".format('fox', 'brown', 'quick') # "The quick brown fox"
# "The {q} {b} {f}".format(f = 'fox', b = 'brown', q = 'quick') # "The quick brown fox"

# Float formatting follows {value:width.precision f}
result = 100/777
# print("The result was {r:1.3f}".format(r = result)) # "The result was 0.129"
# print("The result was {r:1.5f}".format(r = result)) # "The result was 0.12870"
# print(f"The result was {result:1.5f}") # "The result was 0.12870"

name = "Jose"
# print(f"Hello, his name is {name}")