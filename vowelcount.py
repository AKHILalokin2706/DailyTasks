def count_vowels(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

input_string = input("Enter a string: ")

vowel_count = count_vowels(input_string)

if vowel_count > 0:
    print(f"The string contains {vowel_count} vowel(s).")
else:
    print("The string does not contain any vowels.")
