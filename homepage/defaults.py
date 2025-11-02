from algorithms.rsa import primetable as rsa_primetable
from algorithms.rsa import keytable as rsa_keytable
from algorithms.rsa import keygen as rsa_keygen
from algorithms.xor import keygen as xor_keygen

rsa_primetable.generate(1000)
rsa_keytable.generate(256, 10, 1000)
rsa_key = rsa_keygen.create_key_pair(64, 10, 1000)
xor_key = xor_keygen.create_key(64)
