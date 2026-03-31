import my_lib.my_lib as my_lib

import matplotlib.pyplot as plt
import numpy as np


#Data Types

#Variables
my_variable = 10
print(my_variable)

#operations
result = my_variable + 5
print(result)

my_variable = -10
print(my_variable)
result = abs(my_variable)
print(result)

#Data Types

#numeric data types
my_int = int(10.67)
print(my_int)
my_float = float(3.14)
print(my_float)

#Other Data Types
my_string = "Hello, World!"
print(my_string)

my_bool = True
print(my_bool)

my_array = [1, 2, 3, 4, 5]
print(my_array)
print(my_array[0])  # Accessing the first element

m_2d_array = [[1, 2], [3, 4]]
print(m_2d_array)
print(m_2d_array[1][1])  # Accessing the first element of the first row

my_3d_array = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(my_3d_array)  
print(my_3d_array[1][0][1])  # Accessing the second element of the first row of the second layer

my_dictionary = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dictionary)


#------------------------------------------------------------------------

#What is python?

#prograppming language with standard library of operations 

a = 10**2
print(a)

# you can define your own operations using functions

def my_area_local(x, y):
    area = x*y
    return area

result = my_area_local(5, 10)
print("my area is :", result, "m2")



result = my_lib.my_area(5, 10)
print("my area is :", result, "m2")

# Libraries are collections of pre-defined functions and operations that you can use in your code. They help you perform specific tasks without having to write the code from scratch.

#example of ploting a graph using matplotlib
# Prepare data
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

# Plot data
plt.style.use('ggplot')  # Set a style for the plot
plt.plot(xpoints, ypoints, marker='o', linestyle=':', color='yellow')

# Add labels and a title
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Simple Line Plot Example")

# Display the plot
plt.show()