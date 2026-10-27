def add_number(numbers):
    new_numbers = numbers.copy()
    new_numbers.append(100)
    return new_numbers


original = [10, 20, 30]

updated = add_number(original)

print("Original list:", original)
print("Updated list:", updated)