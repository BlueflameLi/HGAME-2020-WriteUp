import gmpy2

p = gmpy2.mpz(681782737450022065655472455411)
q = gmpy2.mpz(675274897132088253519831953441)
e = gmpy2.mpz(13)
phi_n = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi_n)
print ("private key:")
print (d)

c = gmpy2.mpz(275698465082361070145173688411496311542172902608559859019841)
print ("plaintext:")
print (pow(c,d,p*q))