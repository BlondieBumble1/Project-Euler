#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

for i in range(20, 999999999, 20):
    if (i % 19 == 0) and (i % 18 == 0) and (i % 17 == 0) and i % 16 == 0 and i % 15 == 0 and i % 14 == 0 and i % 13 == 0 and i % 12 == 0 and i % 11 == 0:
        print(i)
        quit()