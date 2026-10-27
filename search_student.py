## 4. Coding Problem: Fix the Student Search Program

### Approach

#Use a `for` loop to check each student ID in the list. If the current ID matches the search ID, print `"Student found"` and stop the loop using `break`. Use a `for-else` structure to print `"Student not found"` only when the loop completes without finding the ID.

### Code

student_ids = [101, 102, 103, 104]
search_id = 103

for student_id in student_ids:
    if student_id == search_id:
        print("Student found")
        break
else:
     print("Student not found")
# ```

# ### Test Inputs and Outputs

# **Test Case 1: Student ID exists**

# Input:
# ```python
# student_ids = [101, 102, 103, 104]
# search_id = 103
# ```

# Output:
# ```text
# Student found
# ```

# **Test Case 2: Student ID does not exist**

# Input:
# ```python
# student_ids = [101, 102, 103, 104]
# search_id = 105
# ```

# Output:
# ```text
# Student not found
# ```

# **Test Case 3: Empty list**

# Input:
# ```python
# student_ids = []
# search_id = 103
# ```

# Output:
# ```text
# Student not found
# ```

# ### Time/Space Complexity

# **Time Complexity:** O(n) in the worst case, because the loop may need to check every student ID.

# **Space Complexity:** O(1), because the program uses a fixed amount of additional space, regardless of the number of student IDs.

