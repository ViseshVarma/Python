# # Program to find the highest score without using the max() function

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}")

# '''
# adding number from 1 to 100 
# '''

# total = 0
# for number in range(1, 101):
#   total += number
# print(total)

# '''
# Sum of even  numbers from 1 to 100
# '''

# sum = 0
# for number in range(2, 101, 2):
#   sum += number
# print(sum)


##########################################################################

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_of_letters= int(input("How many letters would you like in your password?\n")) 
num_of_symbols = int(input(f"How many symbols would you like?\n"))
num_of_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for char in range(1, num_of_letters + 1):
    password += random.choice(letters)

for char in range(1, num_of_symbols + 1):
    password += random.choice(symbols)

for char in range(1, num_of_numbers + 1):
    password += random.choice(numbers)

print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

