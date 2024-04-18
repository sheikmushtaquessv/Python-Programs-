# # x=3
# # y=4
# # print(x+y)

# # # Lists

# # grocery_list = ['choclates','fruits','vegetables','choclates','choclates']
# # # quantity_list = [1,3,4,5]
# # # price_list = [0.5,6.3,7.2]

# # # print entire list
# # print(grocery_list)

# # # # print 1st two items
# # # print(grocery_list[:2])

# # # # print 3rd item
# # # print(grocery_list[2])

# # # grocery_list[2] = 'Carrots'

# # # # print entire list
# # # print(grocery_list)

# # # # print length of list
# # # print(len(grocery_list))

# # # #remove last item and assign to new variable
# # # last_item = grocery_list.pop()

# # # print(gro
# # # print(grocery_list,last_item)
# # # # insert an item at any given place
# # # grocery_list.insert(2,'pens')
# # # print(grocery_list)

# # #add new item at end
# # grocery_list.append('water bottle')
# # # remove a specific item
# # grocery_list.remove('choclates')
# # print(grocery_list)
# # print(grocery_list.count('choclates'))




# import math

# def calculate_triangle_area(base, height):
#     area = 0.5 * base * height
#     return area
# def calculate_square_area(side):
#     side=side**2
#     return side

# shape_list = ['circle', 'triangle', 'square']
# selected_shape = input("Please select a shape from the list {}:".format(shape_list))

# if selected_shape.lower() == 'triangle':
#     base = float(input("Enter the base of the triangle: "))
#     height = float(input("Enter the height of the triangle: "))
#     area = calculate_triangle_area(base, height)
#     print("The area of the triangle is:", area)
# else:
#     print("You selected a shape other than triangle. Please run the program again and select 'triangle'.")

# if selected_shape.lower() == 'square':
#     base = float(input("Enter the base of the square: "))
#     height = float(input("Enter the height of the square: "))
#     side = calculate_square_area(side)
#     print("The area of the square is:", side)
# else:
#     print("You selected a shape other than triangle. Please run the program again and select 'square'.")


# import math

# def calculate_triangle_area(base, height):
#     return 0.5 * base * height

# def calculate_circle_area(radius):
#     return math.pi * radius**2

# def calculate_square_area(side):
#     return side**2


"""I have a list of  [circle , triangle,square ] I will pick traingle and have to calculate are of triangle 
   user input needs base and height output should be area of triangle in python and also i want to select alternative shapes also"""

import math

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return math.pi * radius**2

def calculate_square_area(side):
    return side**2


def calculate_area(shape, *args):
    if shape.lower() == 'triangle':
        return calculate_triangle_area(*args)
    elif shape.lower() == 'circle':
        return calculate_circle_area(*args)
    elif shape.lower() == 'square':
        return calculate_square_area(*args)
    else:
        return "Invalid shape."

shape_list = ['circle', 'triangle', 'square']
selected_shape = input("Please select a shape from the list {}:".format(shape_list))

if selected_shape.lower() in shape_list:
    if selected_shape.lower() == 'triangle':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_area(selected_shape, base, height)
    elif selected_shape.lower() == 'circle':
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_area(selected_shape, radius)
    elif selected_shape.lower() == 'square':
        side = float(input("Enter the length of a side of the square: "))
        area = calculate_area(selected_shape, side)
    print("The area of the {} is: {:.2f}".format(selected_shape, area))  
    # {:.2f}--This is a placeholder for the area value. It will be replaced by the value of area. The :.2f format specifier means that the area will be formatted as a floating-point number with two decimal places."
else:
    print("Invalid shape selection.")

