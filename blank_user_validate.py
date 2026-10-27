## 5. Coding Problem: Validate Blank User Input

### Approach

Use the `input()` function to accept a name from the user. Apply the `strip()` method to remove leading and trailing whitespace. If the resulting string is empty, display an error message. Otherwise, display a welcome message with the user's name.

### Code

```python
user_input = input("Enter your name: ")

if user_input.strip() == "":
    print("Name cannot be empty")
else:
    print("Welcome,", user_input.strip())
```

### Test Inputs and Outputs

**Test Case 1: User enters a valid name**

Input:
```text
Enter your name: Ravi
```

Output:
```text
Welcome, Ravi
```

**Test Case 2: User enters only spaces**

Input:
```text
Enter your name:    
```

Output:
```text
Name cannot be empty
```

**Test Case 3: User enters an empty string**

Input:
```text
Enter your name:
```

Output:
```text
Name cannot be empty
```

### Time/Space Complexity

**Time Complexity:** O(n), where n is the length of the input string, because `strip()` may need to examine the input characters.

**Space Complexity:** O(n) in the worst case, because processing the input string may require additional space for the stripped string.

