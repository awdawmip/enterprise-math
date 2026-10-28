"""GH-40: exact reverse-index Gauss reconstruction of the GH-39 high tail.

Proves nothing via numerical tests alone; the accompanying paper gives the
algebraic proof for all primes p=4d+3>=7. Tests use exact integers in F_p.
"""


def primes_below(limit):
    s = bytearray(b"\x01") * limit
    s[:2] = b"\x00\x00"
    for i in range(2, int(limit**0.5) + 1):
        if s[i]:
            s[i*i:limit:i] = b"\x00" * (1 + (limit - 1 - i*i) // i)
    return [i for i in range(limit) if s[i]]


def gauss_coefficients(p):
    d = (p - 3) // 4
    a = [1]
    for r in range(d):
        a.append(a[-1] * (8*r+1)**2 * pow(16*(4*r+3)*(r+1), -1, p) % p)
    return d, a


def check(p):
    d, a = gauss_coefficients(p)
    beta = [1]
    for r in range(d):
        beta.append(beta[-1]*16*(r+1)*(4*r+3)
                    *pow((8*r+13)**2, -1, p) % p)
    inv_ad = pow(a[d], -1, p)
    assert all(beta[r] == a[d-r]*inv_ad % p for r in range(d+1)), p

    # Reversal gives the same coefficient b_{2d-r} with ordered-pair provenance.
    inv = [sum(beta[i]*beta[r-i] for i in range(r+1)) % p for r in range(d)]
    top = [sum(a[i]*a[2*d-r-i] for i in range(max(0,d-r),d+1)
               if 0 <= 2*d-r-i <= d) % p for r in range(d)]
    assert all(top[r] == a[d]**2*inv[r] % p for r in range(d)), p

    # Polynomials in z: low reverse ranks r correspond to original high n=2d-r.
    # For p=4d+3, (8*(2d-r)+1) = -(8r+11) in F_p.
    z = 9 % p
    E_original = sum((8*(2*d-r)+1)*top[r]*pow(z,2*d-r,p)
                     for r in range(d)) % p
    w = sum((8*r+11)*inv[r]*pow(pow(z,-1,p),r,p)
            for r in range(d)) % p
    E_reverse = -a[d]**2*pow(z,2*d,p)*w % p
    assert E_original == E_reverse, (p,E_original,E_reverse)
    assert pow(z,2*d,p) == pow(z,-1,p), p  # 9 is a nonzero square, 2d=(p-3)/2.
    assert E_original == -a[d]**2*pow(z,-1,p)*w % p
    return (E_original,w,a[d])


def main():
    n=0
    saved={}
    for p in primes_below(2000):
        if p < 7 or p%4 != 3:
            continue
        got=check(p)
        n+=1
        if p in (7,11,19,43,67):saved[p]=got
    print(f"PASS_GH40_REVERSED_GAUSS_SOURCE  {n} primes p=3 mod4 <2000")
    for p, (E,W,a_d) in saved.items():
        print(f"p={p}: original high tail E={E}, reverse moment W(1/9)={W}, a_d={a_d}")


if __name__=="__main__":
    main()
