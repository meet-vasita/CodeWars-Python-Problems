# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9

def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i**2
    return sum
        

print(square_sum([1,2,2]))

#Much Better Code
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)