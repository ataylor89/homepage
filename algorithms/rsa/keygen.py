from algorithms.rsa import primetable, keytable
import random
import argparse

def create_key_pair(keylen, tmin, tmax):
    keytable.load()
    filtered = {}
    for k,v in keytable.table.items():
        if v[1] >= tmin and v[1] <= tmax and v[2] >= tmin and v[2] <= tmax:
            filtered[k] = v
    if keylen > len(filtered):
        raise ValueError("There aren't enough keys in the key table that meet the criteria")
    nvalues = list(filtered.keys())
    nvalues = random.sample(nvalues, keylen)
    key = []
    for nvalue in nvalues:
        (n, p, q, phi, e, d) = filtered[nvalue]
        key.append((n, e, d))
    return key
