from algorithms.rsa import primetable as rsa_primetable
from algorithms.rsa import keytable as rsa_keytable
from algorithms.rsa import keygen as rsa_keygen
from algorithms.xor import keygen as xor_keygen

keys = {'RSA': {}, 'XOR': {}}

def load():
    rsa_primetable.load()
    rsa_keytable.load()
    rsa_primetable.generate(1000)
    rsa_keytable.generate(64, 10, 1000)
    rsa_keytable.generate(64, 100, 1000)
    rsa_keytable.generate(64, 500, 1000)
    rsa_primetable.save()
    rsa_keytable.save()
    keys['RSA']['small'] = rsa_keygen.create_key_pair(64, 10, 1000)
    keys['RSA']['medium'] = rsa_keygen.create_key_pair(64, 100, 1000)
    keys['RSA']['large'] = rsa_keygen.create_key_pair(64, 500, 1000)
    keys['XOR']['small'] = xor_keygen.create_key(64)
    keys['XOR']['medium'] = xor_keygen.create_key(256)
    keys['XOR']['large'] = xor_keygen.create_key(1024)
