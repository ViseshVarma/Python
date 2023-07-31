# # File not Found
#
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"Key": "value"}
#     print(a_dictionary["sfasdfs"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} doesnt exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that i made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
