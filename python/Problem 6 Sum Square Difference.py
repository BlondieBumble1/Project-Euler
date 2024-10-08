# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sum = 0
squareSum = 0
for i in range(1, 101):
    sum += i
    squareSum += i**2
print(f"Sum of squares: {squareSum}, Square of sum: {sum**2}, Difference: {sum**2 - squareSum}")
