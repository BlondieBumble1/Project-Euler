# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
with open('Problem 13.txt') as file:
    totals = []
    for j in range(100):
        total = 0
        number = file.readline().strip()
        total += int(number)
        totals.append(total)
    total = sum(totals)
    print(str(total)[:10])