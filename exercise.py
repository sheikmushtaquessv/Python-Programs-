# # # EXERCISE--1

# # def print_shape(length, width):
# #     if length == width:
# #         print("It's a square.")
# #     elif length != width:
# #         print("It's a rectangle.")
# # length = float(input("Enter the length: "))
# # width = float(input("Enter the width: "))
# # print_shape(length, width)


# # Exercise--2

# def triangle_type(length, breadth, height):
#         if length == breadth == height:
#             return "Equilateral"
#         elif length == height :
#             return "Isosceles"
#         else:
#             return "Scalene"
   
# length = float(input("Enter the length of the triangle: "))
# breadth = float(input("Enter the breadth of the triangle: "))
# height = float(input("Enter the height of the triangle: "))

# triangle = triangle_type(length, breadth, height)
# print("The triangle is:", triangle)


# # EXERCISE--3

# import random

# options=("rock","paper","scissors")

# player='User'
# computer=random.choice(options)

# while player not in options:
#   player=input("Enter a choice(rock,paper,scissors):")

# print(player)
# print(computer)

# # print(f"player:{player}")
# # print(f"computer:{computer}")

# if player==computer:
#   print("It's a tie!")
# elif player=="rock" and computer=="scissors":
#     print("You win!")
# elif player=="paper" and computer=="rock":
#     print("You win!")
# elif player=="scissors" and computer=="paper":
#     print("You win!")
# else:
#     print("You lose!")



# # EXERCISE--4

# # Print a list of all matches:

# import random
# import string

# def generate_deck():
#  deck = []
# letters = string.ascii_letters
# numbers = string.digits
# while len(deck)<52:
#     card = ""
#     for i in range(6):
#         alpha_char = random.choice(letters+numbers)
#         # print(alpha_char)
#         card = card + alpha_char
#         # print(card)

#     if card in deck:
#         continue
#     else:
#         deck.append(card)

# # print(deck)


# def replace_card_name(deck, old_card_name, new_card_name, num_replacements):
#     for _ in range(num_replacements):
#         # Select a random index in the deck
#         random_index = random.randint(0, len(deck) - 1)

#         # Replace the old card name with the new card name at the selected index
#         deck[random_index] = new_card_name

#     return deck

# deck = generate_deck()
# print("Original Deck:")
# print(deck)

# old_card_name = input("Enter the name of the card to replace: ")
# new_card_name = input("Enter the new name of the card: ")

# deck_with_replacements = replace_card_name(deck, old_card_name, new_card_name, 6)
# print("\nDeck with Card Name '{}' replaced in 6 places with '{}'".format(old_card_name, new_card_name))
# print(deck_with_replacements)


# # # EXERCISE--5

# it is a sequence of characters that forms a search pattern.
# re module offers a set of functions that allows us to search a string for a match:
# import re

# def validate_phone(phone):
#     # Phone number pattern: ###-###-####
#     # #  r'^\d{10}$' :##########
#     # pattern = r'^\d{10}$'
#     # pattern = r'^\d{+91}$'
#     #  pattern = r"^[6-9]\d{9}$" 
#     #  pattern = r'^\d{3}-\d{3}-\d{4}$' 
#     #  pattern =r"^((0091)|(\+91)|0?)[6-9]\d{9}$"
#     pattern = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"

#     # pattern = r'^\d{10}$'
#     # Starts with 3 digits*
#    # Followed by a dash,# Followed by 4 digits,# Followed by 0 or more characters that aren't newlines**
#    # Followed by the end of the string.
#     return re.match(pattern, phone) is not None
#     # A return statement is used to end the execution of the function call

# def validate_password(password):
#     # Password pattern: At least 1 uppercase, 1 lowercase, 1 digit, 1 symbol, alphanumeric, min length 8
#     pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
#     return re.match(pattern, password) is not None

# def main():
#     # Getting user input for phone number and password
#     phone = input("Enter your phone number:")
#     password = input("Enter your password: ")

#     # Validating phone number and password
#     if validate_phone(phone):
#         print("Phone number is valid.")
#     else:
#         print("Invalid phone number format. Please enter in the format ###-###-####.")

#     if validate_password(password):
#         print("Password is valid.")
#     else:
#         print("Invalid password. Password must contain at least 1 uppercase, 1 lowercase, 1 digit, 1 symbol, alphanumeric, and be at least 8 characters long.")

# main()


# =========
# import re

# def validate_phone(phone):
#     # Phone number pattern: ###-###-####
#     #  r'^\d{10}$'
#     pattern = r'^\d{3}-\d{3}-\d{4}$' 
# # Starts with 3 digits*
# # Followed by a dash
# # Followed by 4 digits
# # Followed by 0 or more characters that aren't newlines**
# # Followed by the end of the string.
#     return re.match(pattern, phone) is not None

# def validate_password(password):
#     # Password pattern: At least 1 uppercase, 1 lowercase, 1 digit, 1 symbol, alphanumeric, min length 8
#     if len(password) < 8:
#         return False
    
#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_symbol = False
    
#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#         else:
#             has_symbol = True
    
#     return has_upper and has_lower and has_digit and has_symbol

# def main():
#     # Getting user input for phone number and password
#     phone = input("Enter your phone number (in the format ###-###-####): ")
#     password = input("Enter your password: ")

#     # Validating phone number and password
#     if validate_phone(phone):
#         print("Phone number is valid.")
#     else:
#         print("Invalid phone number format. Please enter in the format ###-###-####.")

#     if validate_password(password):
#         print("Password is valid.")
#     else:
#         print("Invalid password. Password must contain at least 1 uppercase, 1 lowercase, 1 digit, 1 symbol, alphanumeric, and be at least 8 characters long.")

#
#     main()


# -=======
# # def triangle_type(length, breadth, height):
# #     if length + breadth > height and length + height > breadth and breadth + height > length:
# #         if length == breadth == height:
# #             return "Equilateral"
# #         elif length == breadth or length == height or breadth == height:
# #             return "Isosceles"
# #         else:
# #             return "Scalene"
# #     else:
# #         return "Not a triangle"
# # length = float(input("Enter the length of the triangle: "))
# # breadth = float(input("Enter the breadth of the triangle: "))
# # height = float(input("Enter the height of the triangle: "))

# # triangle = triangle_type(length, breadth, height)
# # print("The triangle is:", triangle)




# # if player==computer:
# #   print("It's a tie!")
# # elif player=="rock" and computer=="scissors":
# #     print("You win!")
# # elif player=="paper" and computer=="rock":
# #     print("You win!")
# # elif player=="scissors" and computer=="paper":
# #     print("You win!")
# # else:
# #     print("You lose!")


# ============

# import random
# import string

# def generate_deck():
#  deck = []
# letters = string.ascii_letters
# numbers = string.digits
# while len(deck)<52:
#     card = ""
#     for i in range(6):
#         alpha_char = random.choice(letters+numbers)
#         # print(alpha_char)
#         card = card + alpha_char
#         # print(card)

#     if card in deck:
#         continue
#     else:
#         deck.append(card)

# # print(deck)


# def replace_card_name(deck, old_card_name, new_card_name, num_replacements):
#     for _ in range(num_replacements):
#         # Select a random index in the deck
#         random_index = random.randint(0, len(deck) - 1)

#         # Replace the old card name with the new card name at the selected index
#         deck[random_index] = new_card_name

#     return deck

# deck = generate_deck()
# print("Original Deck:")
# print(deck)

# old_card_name = input("Enter the name of the card to replace: ")
# new_card_name = input("Enter the new name of the card: ")

# deck_with_replacements = replace_card_name(deck, old_card_name, new_card_name, 6)
# print("\nDeck with Card Name '{}' replaced in 6 places with '{}'".format(old_card_name, new_card_name))
# print(deck_with_replacements)



# ===========
# import random
# import string

# def generate_deck():
#     deck = []
#     letters = string.ascii_letters
#     numbers = string.digits

#     while len(deck) < 52:
#         card = ""
#         for i in range(6):
#             alpha_char = random.choice(letters + numbers)
#             card += alpha_char
#         deck.append(card)

#     return deck

# def replace_card_name(deck, old_card_name, new_card_name, num_replacements):
#     for _ in range(num_replacements):
#         # Select a random index in the deck
#         random_index = random.randint(0, len(deck) - 1)

#         # Replace the old card name with the new card name at the selected index
#         deck[random_index] = new_card_name
# return deck

# deck = generate_deck()
# print("Original Deck:")
# print(deck)

# old_card_name = input("Enter the name of the card to replace: ")
# new_card_name = input("Enter the new name of the card: ")

# deck_with_replacements = replace_card_name(deck, old_card_name, new_card_name, 6)
# print("\nDeck with Card Name '{}' replaced in 6 places with '{}'".format(old_card_name, new_card_name))
# print(deck_with_replacements)


# def calculate_probability(num_replacements, total_cards):
#     probability = 1
#     for i in range(num_replacements):
#         probability *= (total_cards - i) / total_cards
#     return probability

# num_replacements = 6
# total_cards = 52

# probability = calculate_probability(num_replacements, total_cards)
# print("Probability of having 52 unique cards after replacing one card in 6 different places:", probability)


