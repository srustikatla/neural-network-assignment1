input_string = input("Enter a string: ")
if len(input_string) < 2:
    print("Input string must have at least 2 characters.")
else:
    modified_string = input_string[2:]

    reversed_string = modified_string[::-1]

    print("Reversed string:", reversed_string)