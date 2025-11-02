from algorithms.rsa import keytable
import random

def create_key_pair(keylen, tmin, tmax):
    filtered = keytable.filter(tmin, tmax)
    if keylen > len(filtered):
        raise ValueError("There aren't enough keys in the key table that meet the criteria")
    nvalues = list(filtered.keys())
    nvalues = random.sample(nvalues, keylen)
    key = []
    for nvalue in nvalues:
        (n, p, q, phi, e, d) = filtered[nvalue]
        key.append((n, e, d))
    return key
