PLACEHOLDER = "[name]"

with open("invited_names.txt") as my_file:
    names = my_file.readlines()

with open("starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output_letters/Letter_For_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)




