def capitalize_words(input_string):
    return input_string.title()


input_string = input("Enter a string in lowercase: ")

length_of_string = len(input_string)

capitalized_string = capitalize_words(input_string)

sliced_string = input_string[1:5]  
negative_indexing_example = input_string[-3:] 


print("Length of the string:", length_of_string)
print("Capitalized string:", capitalized_string)
print("Sliced string:", sliced_string)
print("Last 3 characters using negative indexing:", negative_indexing_example)
