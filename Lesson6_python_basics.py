# review lesson 4:
#   - variables
#   - print statement


##################### Part One: Print ####################################

# more sofisticated print statement

#print always uses strings

print("Hello World")

#Multiple Strings
print("a","b","c")
print("a","b","c", sep='-')

#print with formating
var = 10.2233434223
print(f"My Floating point variable:{var:.2f}")
var = 100 
print(f"My Integer variable:{var}")
var = 100000000000
print(f"My Integer variable:{var:,}")

#print nice an array
arr = [0,1,2,3,4]
print(*arr, sep=", ")

##################### Part Two: Control Flow ####################################

################# IF statement

x = 0

#basic IF
if x >= 0:
    print("Positive, incluive 0")
    #line 2
    #line 3
else:
    print("Negative")
    #line 2
    #line

#if with atlernative statement
if x > 0:
    print("Positive")
elif x == 0: # your aternative statement
    print("Zero")
else:
    print("Negative")


str = "Test"
if str == "Test": # your aternative statement
    print("Test")
elif str == "Test2": # your aternative statement
    print("Test2")
else:
    print("Garbage Text")

#Operators:
# == --> 2 values are identical (numbers or strings)
# != --> 2 values are not dentical (numbers or strings)
# > --> left value is greater than right (numbers)
# >= --> left value is greater or equal than right (numbers)
# < --> left value is smaller than right (numbers)
# <= --> left value is smaller or equal than right (numbers)

# Nested IF statement

# execute somethig depending on a variabel (between 15-19)
a = 10
if a < 20:
    if a < 15:
        print("Too Small")
    else:
        print("Just Right")
else:
    print("Too Big")

################# FOR Loop statement

#simple for loop
for i in range(5):
    print(i)

print("---------")

#loop over elements of an array
arr = [5,4,3,2,1,0]
for i in arr:
    print(i)

print("---------")

#loop over elements of an 2D array
arr = [[5,4,3,2,1,0],
       [0,1,2,3,4,5]
      ]
for x in arr:
    for y in x:
        print(y)
    print("--")

################# WHILE Loop statement
index = 0
Max_Limit = 100

while index < Max_Limit:
    print(f"Index is at: {index}")
    #index++
    index = index + 10