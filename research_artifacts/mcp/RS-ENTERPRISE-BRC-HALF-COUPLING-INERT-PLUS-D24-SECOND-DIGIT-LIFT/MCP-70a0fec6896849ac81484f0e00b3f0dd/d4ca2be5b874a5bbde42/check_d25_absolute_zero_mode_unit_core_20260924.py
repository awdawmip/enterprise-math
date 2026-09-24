from math import isqrt

def inv(a, m):
    return pow(a % m, -1, m)

def primes(n):
    out = []
    for x in range(2, n):
        if all(x % d for d in range(2, isqrt(x) + 1)):
            out.append(x)
    return out

def Bseq(p):
    M = p**3
    B = [1]
    cur = 1
    for k in range(p - 1):
        cur = cur * ((6*k+1)*(3*k+1) % M) * inv(36*(k+1)*(k+1), M) % M
        B.append(cur)
    return B

def Rm(p):
    m = (p - 1)//6
    t = [1]
    w = [1]
    cur = 1
    for h in range(m):
        cur = cur * ((2*h+1)*(3*h+1)*(3*h+2) % p) * inv(36*(h+1)**3, p) % p
        t.append(cur)
        w.append((6*(h+1)+1)*cur % p)
    P = 0
    d = 1
    R = 0
    for s in range(1, m+1):
        P = (P + w[s-1]) % p
        h = s - 1
        d = d * ((6*h+1)*(h+1) % p) * inv((2*h+1)*(3*h+2), p) % p
        c = d * inv(6*s*s, p) % p
        R = (R + c*P) % p
    return R

def check(p):
    m = (p - 1)//6
    M = p**3
    B = Bseq(p)

    g = sum(B) % M
    h = sum((12*k+1)*B[k] for k in range(p)) % M
    assert g % p == 0

    G = (g//p) % (p*p)
    prod = (G*(h % (p*p)) - 1) % (p*p)
    assert prod % p == 0
    Delta = (prod//p) % p

    S = sum(B[:2*m+1]) % M
    assert S % p == 0
    GT = (S//p) % (p*p)

    H0 = sum((12*k+1)*B[k] for k in range(m+1)) % (p*p)

    A = 0
    for r in range(1, m+1):
        assert B[m+r] % p == 0
        x = (B[m+r]//p) % p
        A = (A + (12*r-1)*x) % p

    Y = 0
    for k in range(2*m+1, p):
        assert B[k] % (p*p) == 0
        Y = (Y + B[k]//(p*p)) % p

    assert G == (GT + p*Y) % (p*p)
    assert h % (p*p) == (H0 + p*A) % (p*p)

    znum = (GT*H0 - 1) % (p*p)
    assert znum % p == 0
    ZT = (znum//p) % p

    assert Delta == (ZT + (G % p)*A + (h % p)*Y) % p
    assert Delta == Rm(p)   # regression only, not proof
    return ZT, A, Y, Delta

def main():
    T = [p for p in primes(5000) if p % 24 in (13, 19)]
    assert len(T) == 166
    assert sum(p % 24 == 13 for p in T) == 83
    assert sum(p % 24 == 19 for p in T) == 83
    for p in T:
        check(p)
    print("targets", len(T), "failures", 0)

if __name__ == "__main__":
    main()
