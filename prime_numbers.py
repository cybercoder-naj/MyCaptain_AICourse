n = int(input())
primes = [1] * (n + 1)
primes[0] = 0
primes[1] = 0
number = 2
while number * number <= n:
    if primes[number] == 1:
        for multiples in range(number * number, n + 1, number):
            primes[multiples] = 0
    number += 1
print('the prime numbers are\n', [x for x in range(len(primes)) if primes[x] == 1])
