def odd_index_elements(input_list):
    return [input_list[i] for i in range(1, len(input_list), 2)]

input_list = input("Enter elements of the list separated by space: ").split()

result = odd_index_elements(input_list)

print("Elements at odd indices:", result)