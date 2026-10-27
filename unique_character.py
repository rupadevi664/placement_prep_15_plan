## 3. Coding Problem: Find the First Non-Repeating Character

### Approach

# Use a dictionary to count the frequency of each character in the given string. First, remove spaces from the string. Then, traverse the string again and find the first character whose frequency is exactly one. Preserve case sensitivity and avoid using `count()` inside a loop.

### Code


def first_non_repeating(text):
    text = text.replace(" ", "")
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    for char in text:
        if frequency[char] == 1:
            return char

    return "No non-repeating character found"


print(first_non_repeating("programming"))
print(first_non_repeating("aabbcdd"))
print(first_non_repeating("aabbcc"))

# ### Test Inputs and Outputs

# **Test Case 1: String with a non-repeating character**

# Input:
# ```python
# "programming"
# ```

# Output:
# ```text
# p
# ```

# **Test Case 2: First non-repeating character appears later**

# Input:
# ```python
# "aabbcdd"
# ```

# Output:
# ```text
# c
# ```

# **Test Case 3: All characters are repeated**

# Input:
# ```python
# "aabbcc"
# ```

# Output:
# ```text
# No non-repeating character found
# ```

# **Test Case 4: String containing spaces**

# Input:
# ```python
# "a a b b c"
# ```

# Output:
# ```text
# c
# ```

# ### Time/Space Complexity

# **Time Complexity:** O(n), because the string is traversed twice and each dictionary operation takes O(1) expected time.

# **Space Complexity:** O(k), where k is the number of distinct characters stored in the frequency dictionary. In the worst case, this is O(n).

