def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    
    freq1, freq2 = {}, {}
    
    for char in str1:
        freq1[char] = freq1.get(char, 0) + 1
    
    for char in str2:
        freq2[char] = freq2.get(char, 0) + 1
    
    for char, count in freq1.items():
        if char not in freq2 or freq2[char] != count:
            return False
    
    return True

input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")

if are_anagrams(input_str1, input_str2):
    print(f"{input_str1} and {input_str2} are anagrams.")
else:
    print(f"{input_str1} and {input_str2} are not anagrams.")
