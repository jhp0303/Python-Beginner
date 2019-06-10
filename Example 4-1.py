list_a = [52, 273, 103, 32, 57]

min_value = list_a[0]
for element in list_a:
    if element < min_value:
        min_value = element
    
max_value = list_a[0]
for element in list_a:
    if element > max_value:
        max_value = element

print("최소값:", min_value)
print("최대값:", max_value)