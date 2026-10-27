## 2. Coding Problem: Store a Student Profile

### Approach

# Use a Python dictionary to store student details as key-value pairs. Each key represents a student's attribute, such as name, age, course, or marks. Access the values using their corresponding keys and display them.

### Code

student = {
    "name": "Ravi",
    "age": 21,
    "course": "Python",
    "marks": 85
}

print("Student Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])


# ### Test Inputs and Outputs

# **Test Case 1: Display student details**

# Input:
# ```python
# student = {
#     "name": "Ravi",
#     "age": 21,
#     "course": "Python",
#     "marks": 85
# }
# ```

# Output:
# ```text
# Student Name: Ravi
# Age: 21
# Course: Python
# Marks: 85
# ```

# **Test Case 2: Student with different details**

# Input:
# ```python
# student = {
#     "name": "Priya",
#     "age": 22,
#     "course": "Java",
#     "marks": 92
# }
# ```

# Output:
# ```text
# Student Name: Priya
# Age: 22
# Course: Java
# Marks: 92
# ```

# ### Time/Space Complexity

# **Time Complexity:** O(1) average for each dictionary lookup, because values are accessed directly using their keys.

# **Space Complexity:** O(1) for this example, because the dictionary stores a fixed number of fields. In general, storing n key-value pairs requires O(n) space.

