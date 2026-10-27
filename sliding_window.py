#previous sum-outgoing number+incoming number =new window sum
#insted of repeating elements from begining we use the previous sum and adjust it
def max_window_sum(numbers, k):
    if k <= 0 or k > len(numbers):
        return None

    window_sum = sum(numbers[:k])
    max_sum = window_sum

    for i in range(k, len(numbers)):
        window_sum = window_sum - numbers[i-k] + numbers[i]

        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum


print(max_window_sum([2, 1, 5, 1, 3, 2], 3))
print(max_window_sum([1, 2, 3, 4, 5], 2))
print(max_window_sum([1, 2], 0))
print(max_window_sum([1, 2], 3))
