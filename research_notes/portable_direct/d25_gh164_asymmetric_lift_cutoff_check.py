#!/usr/bin/env python3
"""Author-side exact p-adic cutoff regression for the frozen D25 scalar interface."""


def target_primes(limit):
    sieve = bytearray(b'\x01') * limit
    sieve[:2] = b'\x00\x00'
    for n in range(2, int((limit - 1) ** 0.5) + 1):
        if sieve[n]:
            sieve[n * n:limit:n] = b'\x00' * len(sieve[n * n:limit:n])
    return [p for p in range(11, limit) if sieve[p] and p % 24 in (13, 19)]


def exact_full(p):
    modulus = p ** 3
    term = 1
    g = h = tail_g = tail_h = 0
    m = (p - 1) // 6
    for k in range(p):
        g = (g + term) % modulus
        h = (h + (12 * k + 1) * term) % modulus
        if k > 2 * m:
            tail_g = (tail_g + term) % modulus
            tail_h = (tail_h + (12 * k + 1) * term) % modulus
        if k + 1 < p:
            term = term * (6 * k + 1) * (3 * k + 1) * pow(36 * (k + 1) ** 2, -1, modulus) % modulus
    assert g % p == 0
    G = g // p
    assert (G * h - 1) % p == 0
    return (G * h - 1) // p % p, g, h, tail_g, tail_h


def independently_reduced(p):
    """Only prefix high precision; post-cutoff tail is computed in F_p."""
    m = (p - 1) // 6
    k0 = 2 * m + 1
    q = p ** 3
    B = 1
    g0 = h0 = 0
    for k in range(k0):
        g0 = (g0 + B) % q
        h0 = (h0 + (12 * k + 1) * B) % (p ** 2)
        if k < k0 - 1:
            B = B * (6 * k + 1) * (3 * k + 1) * pow(36 * (k + 1) ** 2, -1, q) % q
    assert g0 % p == 0
    G0 = g0 // p
    assert (G0 * h0 - 1) % p == 0

    # B_(2m+1)/p^2, with the two distinct p-factors removed
    numerator = 1
    for j in range(k0):
        if j != m:
            numerator = numerator * (6 * j + 1) % p
        if j != 2 * m:
            numerator = numerator * (3 * j + 1) % p
    factorial = 1
    for j in range(1, k0 + 1):
        factorial = factorial * j % p
    c = numerator * pow(36, -k0, p) * pow(factorial, -2, p) % p
    tail = 0
    for k in range(k0, p):
        tail = (tail + c) % p
        if k < p - 1:
            c = c * (6 * k + 1) * (3 * k + 1) * pow(36 * (k + 1) ** 2, -1, p) % p

    delta_truncated = ((G0 * h0 - 1) // p) % p
    return ((delta_truncated + (h0 % p) * tail) % p, delta_truncated,
            tail, h0 % p)



def valuation_staircase(p):
    """Three valuation blocks: precisions p^3, p^2, p, respectively."""
    m = (p - 1) // 6
    mod3, mod2 = p ** 3, p ** 2
    a = 1
    g_unit = h_unit = 0
    for k in range(m + 1):
        g_unit = (g_unit + a) % mod3
        h_unit = (h_unit + (12*k + 1)*a) % mod2
        if k < m:
            a = a*(6*k+1)*(3*k+1)*pow(36*(k+1)**2, -1, mod3) % mod3
    # 6m+1=p; b is B_(m+1)/p modulo p^2.
    b = a*(3*m+1)*pow(36*(m+1)**2, -1, mod2) % mod2
    g_mid = h_mid = 0
    for k in range(m+1, 2*m+1):
        g_mid = (g_mid + b) % mod2
        h_mid = (h_mid + (12*k+1)*b) % p
        if k < 2*m:
            b = b*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,mod2)%mod2
    # 3(2m)+1=p; c is B_(2m+1)/p^2 modulo p.
    c = b*(6*(2*m)+1)*pow(36*(2*m+1)**2,-1,p)%p
    g_tail = 0
    for k in range(2*m+1,p):
        g_tail = (g_tail + c)%p
        if k+1<p:
            c=c*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,p)%p
    g = (g_unit+p*g_mid+p*p*g_tail)%mod3
    h = (h_unit+p*h_mid)%mod2
    assert g%p==0
    G=g//p
    assert (G*h-1)%p==0
    return ((G*h-1)//p)%p,g_tail


def hypergeometric_tail(p):
    """Independent finite-field 3F2-type shifted expression for tail T_p."""
    m=(p-1)//6
    k0=2*m+1
    numer=1
    for j in range(k0):
        if j!=m: numer=numer*(6*j+1)%p
        if j!=2*m: numer=numer*(3*j+1)%p
    denom=1
    for j in range(1,k0+1):denom=denom*j%p
    c0=numer*pow(36,-k0,p)*pow(denom,-2,p)%p
    c=1;total=0
    for r in range(4*m):
        total=(total+c)%p
        if r<4*m-1:
            # ((r+5/6)*(r+1))/(2*(r+5/3)^2)
            c=c*(6*r+5)*(r+1)*3*3*pow(2*6*(3*r+5)**2,-1,p)%p
    return c0*total%p


def exploratory_weighted_w(p):
    q = p ** 3
    term = 1
    total = 0
    for k in range(p):
        total = (total + (6 * k + 1) * term) % q
        if k < p - 1:
            term = term * (2*k + 1) * (3*k + 1) * (3*k + 2) * pow(36*(k + 1)**3, -1, q) % q
    return total


def main():
    candidates = target_primes(5000)
    examples = {}
    nonzero = 0
    w3_matches = 0
    bad = []
    for p in candidates:
        delta, g, h, gt, ht = exact_full(p)
        reduced, truncated, tail, h_bar = independently_reduced(p)
        assert gt % (p*p) == ht % (p*p) == 0
        assert tail == (gt // (p*p)) % p, ('tail', p)
        assert delta == reduced, ('delta', p, delta, reduced)
        dd,tt = valuation_staircase(p)
        assert delta==dd and tt==tail, ('staircase',p,delta,dd,tt,tail)
        assert hypergeometric_tail(p)==tail, ('hypergeom',p)
        assert (delta - truncated) % p == (tail*h_bar)%p
        nonzero += tail != 0
        w = exploratory_weighted_w(p)
        w3_matches += w == p
        if w != p:
            bad.append((p,w))
        if p in (13,19,37,157,109,3347):
            examples[p] = dict(delta=delta, truncated=truncated, tail=tail,
                               h_bar=h_bar, omitted_delta=(delta-truncated)%p,
                               Wmodp3=w)
    assert len(candidates) == 166, len(candidates)
    print('EXAMPLES', examples)
    print('SUMMARY target_primes_lt5000',len(candidates),'tail_nonzero',nonzero,
          'tail_zero',len(candidates)-nonzero, 'W_p_equals_p_mod_p3',w3_matches)
    print('WEIGHTED_W_EXCEPTIONS',bad[:10])
    print('PASS_GH164_ASYMMETRIC_SECOND_DIGIT_CUTOFF_EXACT')


if __name__ == '__main__':
    main()
