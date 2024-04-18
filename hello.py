# print("Hello World")

# # Variables and DataTypes

# a=30
# b='Mushtaque'
# c=71.22
# print(a,type(a))
# print(b,type(b))
# print(c,type(c))

# # input() function

# a=input("Enter name")
# print(a)

# # string

# name='Harry'
# sl=name[0:3]
# sl=name[1:3]
# print(sl)

# # Negative Indices

# name='Harry'
# sl=name[-4:-2]
# print(sl)

# # Slicing with skip value
# word='amazing'
# sl=word[1:6:2]
# sl1=word[:7]
# sl2=word[0:7]
# sl3=word[0:]

# print(sl3)

# String functions

# name='Harry'
# length=len(name)
# print(length)
# print(len(name))

# name='Harry'
# endswith=endswith('ry')
# print(endswith)


# Strings='khhdasahsuihefuuefiuiwui'
# Integers=123456 #positive or negative
# Decimal=0.12 #positive or negative
# Boolean=True #True or False

# lists=["abc", 34,-55,40.0,-44.7,True, "male"]#Mutable
# Dictionaries={'unique':["abc","male", 34,-55,40.0,-44.7,True,False],'unique2':["abc","male", 34,-55,40.0,-44.7,True,False]}
# tuple=("abc", 34,-55,40.0,-44.7,True, "male") #Immutable
# sets={"abc", 34,-55,40.0,-44.7,True, "male"}#Duplicates Not Allowed.




# def calculate_triangle_area(base, height):
#     area = 0.5 * base * height
#     return area

# # Taking user input for base and height
# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))

# # Calculating the area of the triangle
# area = calculate_triangle_area(base, height)
# print("The area of the triangle is:", area)


# import math

# def calculate_triangle_area(base, height):
#     area = 0.5 * base * height
#     return area

# shape_list = ['circle', 'triangle', 'square']
# selected_shape = input("Please select a shape from the list {}:".format(shape_list))

# if selected_shape.lower() == 'triangle':
#     base = float(input("Enter the base of the triangle: "))
#     height = float(input("Enter the height of the triangle: "))
#     area = calculate_triangle_area(base, height)
#     print("The area of the triangle is:", area)
# else:
#     print("You selected a shape other than triangle. Please run the program again and select 'triangle'.")

# if selected_shape.lower() == 'circle':
#     base = float(input("Enter the base of the circle: "))
#     height = float(input("Enter the height of the circle: "))
#     area = calculate_triangle_area(base, height)
#     print("The area of the circle is:", area)
# else:
#     print("You selected a shape other than circle. Please run the program again and select 'circle'.")

# if selected_shape.lower() == 'square':
#     base = float(input("Enter the base of the square: "))
#     height = float(input("Enter the height of the square: "))
#     area = calculate_triangle_area(base, height)
#     print("The area of the square is:", area)
# else:
#     print("You selected a shape other than square. Please run the program again and select 'square'.")

# import random
# import string

# def generate_alphanumeric_code(length):
#     # Generate a random alphanumeric code of the specified length
#     characters = string.ascii_letters + string.digits
#     code = ''.join(random.choice(characters) for _ in range(length))
#     return code

# def generate_list_of_codes(num_codes, code_length):
#     # Generate a list of alphanumeric codes
#     code_list = [generate_alphanumeric_code(code_length) for _ in range(num_codes)]
#     return code_list

# # Generate a list of 100 alphanumeric codes with length 6
# result_list = generate_list_of_codes(num_codes=100, code_length=6)

# # Return the result list
# result_list


