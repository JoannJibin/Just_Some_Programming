def sieve(n):
    # Create a boolean list to track prime status of numbers
    prime = [True] * (n + 1)
    p = 2

    # Sieve of Eratosthenes algorithm
    while p**2 <= n:
        if prime[p]:
            # Mark all multiples of p as non-prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Collect all prime numbers
    r = []
    for p in range(2, n + 1):
        if prime[p]:
            r.append(p)

    return r


n = int(input("Enter the number till which we need to find all prime numbers: "))
result = sieve(n)
for i in result:
    print(i, end=' ')