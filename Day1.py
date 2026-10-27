#Scenario 1: Detect duplicate student IDs
#Question: You receive thousands of student IDs and must detect duplicates. Which data structure will you use?

#Answer: I will use a set to store IDs that have already appeared. If an ID appears again, I will identify it as a duplicate.
ids = [101, 102, 103, 101, 104, 102]
def find_duplicates(ids):
    seen = set()
    duplicates = set()

    for student_id in ids:
        if student_id in seen:
            duplicates.add(student_id)
        else:
            seen.add(student_id)

    return duplicates


print(find_duplicates(ids))

# Test Inputs and Outputs

# Test Case 1: Duplicate IDs exist

# Input:

# student_ids = [101, 102, 103, 101, 104, 102]

# Output:

# Duplicate student IDs: [101, 102]

# Test Case 2: No duplicate IDs

# Input:

# student_ids = [101, 102, 103, 104]

# Output:

# No duplicate student IDs found

# Test Case 3: All IDs are the same

# Input:

# student_ids = [101, 101, 101]

# Output:

# Duplicate student IDs: [101]

# Test Case 4: Empty list

# Input:

# student_ids = []

# Output:

# No duplicate student IDs found

# Time/Space Complexity

# Time Complexity: O(n) expected, because each student ID is processed once and set operations take O(1) expected time.

# Space Complexity: O(n), because the seen and duplicates sets may store up to n elements in total order of growth.