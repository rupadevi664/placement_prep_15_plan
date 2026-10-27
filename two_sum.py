#finding two numbers in a list whose sum equals to target
def two_sum(numbers,target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j]==target:
                return numbers[i],numbers[j]
    return None
print(two_sum([2,7,11,15],9))