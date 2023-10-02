keys = input("Enter keys separated by space: ").split()
values = input("Enter values separated by space: ").split()

mapped_dict = dict(zip(keys, values))

print(mapped_dict)
