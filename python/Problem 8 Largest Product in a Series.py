# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
from math import prod
with open('Problem 8 Largest Product in a Series.txt') as f:
    number = f.read().replace('\n', '')
    max_product = 0
    for i in range(len(number) - 13):
        numbers = []
        for j in range(13):
            numbers.append(int(number[i + j]))
        product = prod(numbers)
        if product > max_product:
            max_product = product
    print(max_product)
f.close()