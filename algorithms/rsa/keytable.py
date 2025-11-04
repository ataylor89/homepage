from algorithms.rsa import primetable, util
import math
import pickle
import sys
import os
import random
import time

table = {}
test_message = "hello world! my name is andrew"

def filter(tmin, tmax):
    return {
        key: value for key, value in table.items() if value[1] >= tmin and value[1] <= tmax and value[2] >= tmin and value[2] <= tmax
    }

def generate(numkeys, tmin, tmax):
    if len(filter(tmin, tmax)) >= numkeys:
        return

    count = 0
    startindex = -1
    endindex = -1

    for i in range(0, primetable.size()):
        if startindex < 0 and primetable.get(i) >= tmin:
            startindex = i
        if endindex < 0 and primetable.get(i) == tmax:
            endindex = i
        if endindex < 0 and primetable.get(i) > tmax:
            endindex = i - 1
        if startindex > 0 and endindex > 0:
            break

    if startindex == -1:
        raise ValueError("tmin is too high")

    if endindex == -1:
        endindex = primetable.size() - 1

    while count < numkeys:
        i = random.randint(startindex, endindex)
        j = random.randint(startindex, endindex)

        if i == j:
            continue

        p = primetable.get(i)
        q = primetable.get(j)
        n = p * q

        # print("n = %d, p = %d, q = %d" %(n, p, q))

        if n in table:
            continue

        phi = math.lcm(p-1, q-1)

        # print("phi = %d" %phi)

        e = 0
        for e in range(2, phi):
            if math.gcd(e, phi) == 1:
                break

        # print("e = %d" %e)

        d = 0
        for d in range(2, phi):
            if (d * e) % phi == 1:
                break

        # print("d = %d" %d)

        if test(n, e, d):
            # print("Adding key (n=%d, p=%d, q=%d, phi=%d, e=%d, d=%d)" %(n, p, q, phi, e, d))
            table[n] = (n, p, q, phi, e, d)
            count += 1

def test(n, e, d):
    codes = list(map(lambda x: ord(x), test_message))

    encrypted = []
    for i in range(0, len(codes)):
        encrypted.append(util.power_mod_n(codes[i], e, n))

    decrypted = []
    for i in range(0, len(codes)):
        decrypted.append(util.power_mod_n(encrypted[i], d, n))

    return codes == decrypted

def load(path='keytable.pickle'):
    if os.path.exists(path):
        with open(path, "rb") as file:
            table.clear()
            table.update(pickle.load(file))

def save(path='keytable.pickle'):
    if len(table) > 0:
        with open(path, "wb") as file:
            pickle.dump(table, file)
