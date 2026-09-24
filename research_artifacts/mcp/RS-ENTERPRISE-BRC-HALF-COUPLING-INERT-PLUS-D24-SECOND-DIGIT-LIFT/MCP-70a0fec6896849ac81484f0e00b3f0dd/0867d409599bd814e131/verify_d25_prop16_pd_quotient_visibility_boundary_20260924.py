def inv_mod(a, m):
    return pow(a % m, -1, m)

# Regression only. The accompanying note carries the proof.
def check_prime(p):
    U = 3 % p
    W = 5 % p
    V = ((-1 - p * U * U) * inv_mod(W, p**3)) % (p**3)
    ea = 7 % p
    eb = 11 % p
    A = ((1 + p*ea) * inv_mod(W, p**3)) % (p**3)
    B = ((1 + p*eb) * inv_mod(V, p**3)) % (p**3)
    a = (p*A) % (p**3)
    b = B % (p**3)

    lhs = (a*b) % (p**3)
    rhs = (-p + p*p*((U*U - ea - eb) % p)) % (p**3)
    assert lhs == rhs, (p, lhs, rhs)

    # H_DR(...,(p)) gauge witness: the primitive xi^p coefficient A
    # changes by a p-multiple, so the published quotient cannot see it.
    t = 13 % p
    A2 = (A + p*inv_mod(W, p**3)*t) % (p**3)
    a2 = (p*A2) % (p**3)
    assert (A2 - A) % p == 0
    assert (W*A2 - W*A) % p == 0

    ea_old = ((W*A - 1) % (p*p)) // p
    ea_new = ((W*A2 - 1) % (p*p)) // p
    assert (ea_new - ea_old) % p == t

    k_old = ((lhs + p) % (p**3)) // (p*p)
    lhs2 = (a2*b) % (p**3)
    k_new = ((lhs2 + p) % (p**3)) // (p*p)
    assert (k_new - k_old) % p == (-t) % p

for p in [13, 19, 37, 43, 61, 67, 109, 139, 157, 163]:
    check_prime(p)

print('PASS: product-second-digit formula and H_DR(p) gauge witness')
