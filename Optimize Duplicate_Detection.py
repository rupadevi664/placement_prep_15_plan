## 6. Coding Problem: Optimize Duplicate Detection

# Approach

# Use a set to keep track of numbers that have already been visited. Traverse the list using a `for` loop. If a number is already present in the set, a duplicate exists, so set the Boolean variable to `True` and stop the loop using `break`. Otherwise, add the number to the set.

### Code

numbers = [10, 20, 30, 20, 40]

seen = set()
has_duplicates = False

for number in numbers:
    if number in seen:
        has_duplicates = True
        break

    seen.add(number)

if has_duplicates:
    print("Duplicates exist")
else:
    print("No duplicates found")


### Test Inputs and Outputs

# **Test Case 1: Duplicate numbers exist**

# Input:
# ```python
# numbers = [10, 20, 30, 20, 40]
# ```

# Output:
# ```text
# Duplicates exist
# ```

# **Test Case 2: No duplicate numbers**

# Input:
# ```python
# numbers = [10, 20, 30, 40]
# ```

# Output:
# ```text
# No duplicates found
# ```

# **Test Case 3: All numbers are identical**

# Input:
# ```python
# numbers = [5, 5, 5]
# ```

# Output:
# ```text
# Duplicates exist
# ```

# **Test Case 4: Empty list**

# Input:
# ```python
# numbers = []
# ```

# Output:
# ```text
# No duplicates found
# ```

# ### Time/Space Complexity

# **Time Complexity:** O(n) expected in the worst case, because each number is checked once and set operations take O(1) expected time.

# **Space Complexity:** O(n), because the `seen` set may store all elements when there are no duplicates.

