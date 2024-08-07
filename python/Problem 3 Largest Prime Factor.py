#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

import math

num = 600851475143
factors = []
primeFactors = []

for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        factors.append(i)

for j in factors:
    is_prime = True
    for k in range(2, int(math.sqrt(j)) + 1):
        if j % k == 0:
            is_prime = False
            break
    if is_prime:
        primeFactors.append(j)
        
print(max(primeFactors))