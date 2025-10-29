import pickle
import os
import time
import argparse

table = []

def generate(n):
    size = 10 * n
    s = sieve(n, size)
    while s.count('P') < n:
        size *= 10
        s = sieve(n, size)
    table.clear()
    table.extend([i for i, j in enumerate(s) if j == 'P'][0:n])

def sieve(n, size):
    arr = ['P'] * size
    arr[0] = 'N'
    arr[1] = 'N'
    for i in range(2, size):
        if arr[i] == 'P':
            j = 2
            while i * j < size:
                arr[i * j] = 'C'
                j += 1
    return arr

def get(n):
    return table[n]

def size():
    return len(table)

def load(path='primetable.pickle'):
    if os.path.exists(path):
        with open(path, "rb") as file:
            table.clear()
            table.extend(pickle.load(file))

def save(path='primetable.pickle'):
    if len(table) > 0:
        with open(path, "wb") as file:
            pickle.dump(table, file)

def main():
    parser = argparse.ArgumentParser(prog="primetable.py", description="Generate a prime table")
    parser.add_argument("-n", "--numberofprimes", type=float, default=1e4)
    args = parser.parse_args()
    try:
        n = int(args.numberofprimes)
        assert n > 0
    except:
        print("Unable to parse the command-line argument as a positive integer")
        return
    load()
    if len(table) >= n:
        print("The existing table is sufficient")
        return
    st = time.time()
    generate(n)
    te = time.time() - st
    save()
    print("Created a prime table with %d primes in %s seconds" %(n, te))

if __name__ == "__main__":
    main()
