# Comparison Operators in Python
2 == 2 # True
2 == 1 # False
"hello" == "bye" # False
"Bye" == "bye" # False
"bye" == "bye" # True
"2" == 2 # False
2.0 == 2 # True
3 != 3 # False
4 != 5 # True
2 > 1 # True
1 > 2 # False
2 >= 2 # True
4 <= 1 # False

# Chaining Comparison Operators in Python with Logical Operators
1 < 2 and 2 < 3 # False
1 < 2 and 2 < 3 # True
"h" == "h" and 2 == 2 # True

1 == 1 or 2 == 2 # True
100 == 1 or 2 == 2 # True
100 == 1 or 2 == 200 # True

not 1 == 1 # False - returns the opposite boolean
not 400 > 5000 # True