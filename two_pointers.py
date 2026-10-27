# usally one pointer moves from begining,another moves from endining and move forward at diiferent sppeds
# two pointers are left pointer and right pointer 
# in each iteration we compare left and right pointers and move them forward or backward based on the problem statement

def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [numbers[left], numbers[right]]

        elif total < target:
            left += 1

        else:
            right -= 1

    return None


print(two_sum([1, 2, 3, 7, 8], 9))
