# Python program to Print all Prime numbers in an Interval
# using simple optimized Sieve of Eratosthenes
# to reduce size of prime array to half and
# reducing iterations.

def bitwiseSieve(srt, n):

    # prime[i] is going to store
    # true if if i*2 + 1 is composite.
    prime = [0 if i % 2 == 0 else 1 for i in range(n+1)]
    prime[1] = 0
    prime[2] = 1
    # 2 is the only even prime so
    # we can ignore that. Loop
    # starts from 3.
    i = 3
    while (i * i <= n):
        # If i is prime, mark all its
        # multiples as composite
        if (prime[(i)] == 1):
            j = i * i
            while (j <= n):
                prime[j] = 0
                j += 2*i
        i += 2
    # writing 2 separately
    # Printing other primes
    i = srt
    while (i <= n):
        if (prime[i] == 1):
            print(i, end=" ")
        i += 1


# Driver code
if __name__ == '__main__':
    srt = 3
    end = 100
    bitwiseSieve(srt, end)

# update and run in any interval if srt is change
# previously it always start from 2

# This code is contributed by Susobhan Akhuli
