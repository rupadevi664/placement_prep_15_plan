# ## 7. Coding Problem: Remove Duplicates While Preserving Order

# # Approach

# Use a list named `unique_numbers` to store the unique elements in their original order and a set named `seen` to track elements that have already appeared. Traverse the original list using a `for` loop. If a number is not present in `seen`, add it to both `unique_numbers` and `seen`. This removes duplicates while preserving the order of first occurrence.

# # Code

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = []
seen = set()

for number in numbers:
    if number not in seen:
        unique_numbers.append(number)
        seen.add(number)

print("Original list:", numbers)
print("List after removing duplicates:", unique_numbers)


### Test Inputs and Outputs

# **Test Case 1: List containing duplicate numbers**

# Input:
# ```python
# numbers = [10, 20, 10, 30, 20, 40, 30]
# ```

# Output:
# ```text
# Original list: [10, 20, 10, 30, 20, 40, 30]
# List after removing duplicates: [10, 20, 30, 40]
# ```

# **Test Case 2: List without duplicates**

# Input:
# ```python
# numbers = [1, 2, 3, 4]
# ```

# Output:
# ```text
# Original list: [1, 2, 3, 4]
# List after removing duplicates: [1, 2, 3, 4]
# ```

# **Test Case 3: All elements are identical**

# Input:
# ```python
# numbers = [5, 5, 5, 5]
# ```

# Output:
# ```text
# Original list: [5, 5, 5, 5]
# List after removing duplicates: [5]
# ```

# **Test Case 4: Empty list**

# Input:
# ```python
# numbers = []
# ```

# Output:
# ```text
# Original list: []
# List after removing duplicates: []
# ```

# ### Time/Space Complexity

# **Time Complexity:** O(n) expected, because each element is processed once and set membership checks take O(1) expected time.

# **Space Complexity:** O(n), because the `seen` set and `unique_numbers` list may each store up to n elements.

