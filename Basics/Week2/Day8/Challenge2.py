#Lambda function

numbers = [2, 4, 6, 8, 10, 12, 14, 16]

tripled_list = list(map(lambda x: x * 3, numbers))
filtered_list = list(filter(lambda x: x > 10, numbers))

print("Tripled list:", tripled_list)
print("Filtered list (greater than 10):", filtered_list)