"""GH-38/GH-39: exact finite-field Picard--Fuchs and Gauss-tail checks.

All arithmetic is in F_p; no native Enterprise-Math execution is claimed.
Only the finite ranges named in main() are enumerated.
"""


def primes_below(limit):
    sieve = bytearray(b"\x01") * limit
    sieve[:2] = b"\x00\x00"
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i * i:limit:i] = b"\x00" * (((limit - 1 - i * i) // i) + 1)
    return [i for i in range(limit) if sieve[i]]


def port_coefficients(p):
    d = (p - 3) // 4
    c, a = [1], [1]
    for r in range(d):
        # c_r = (1/4)_r^3 / ((1/2)_r (3/4)_r r!)
        c.append(c[-1] * pow(4 * r + 1, 3, p)
                 * pow((4 * r + 2) * (4 * r + 3) * (4 * r + 4), -1, p) % p)
        # a_r = (1/8)_r^2 / ((3/4)_r r!)
        a.append(a[-1] * pow(8 * r + 1, 2, p)
                 * pow(16 * (4 * r + 3) * (r + 1), -1, p) % p)
    return d, c, a


def verify_picard_fuchs(p, d, c, a):
    inv4, inv8 = pow(4, -1, p), pow(8, -1, p)
    for n in range(d + 2):
        cn = c[n] if n <= d else 0
        an = a[n] if n <= d else 0
        cp = c[n - 1] if n else 0
        ap = a[n - 1] if n else 0
        third = (n * (n - pow(2, -1, p)) * (n - inv4) * cn
                 - (n - 1 + inv4) ** 3 * cp) % p
        second = (n * (n - inv4) * an - (n - 1 + inv8) ** 2 * ap) % p
        if n <= d:
            assert third == second == 0, (p, n, third, second)
        else:
            assert third == c[d] * inv8 % p, (p, n, third)
            assert second == -25 * pow(64, -1, p) * a[d] % p, (p, n, second)
    assert c[d] and a[d]


def verify_clausen_tail(p, d, c, a):
    # Full product coefficient b_n; for n<=d it must equal c_n.
    b = [sum(a[i] * a[n - i]
             for i in range(max(0, n - d), min(d, n) + 1)) % p
         for n in range(2 * d + 1)]
    assert b[:d + 1] == c, (p, b[:d + 1], c)
    # (8 theta+1) B^2 = B (B+16 theta B): coefficient at n is (8n+1)b_n.
    q = [((16 * r + 1) * a[r]) % p for r in range(d + 1)]
    for n in range(2 * d + 1):
        l = sum(a[i] * q[n - i]
                for i in range(max(0, n - d), min(d, n) + 1)) % p
        assert l == (8 * n + 1) * b[n] % p, (p, n, l, b[n])
    z = 9 % p
    t = sum((8 * r + 1) * c[r] * pow(z, r, p) for r in range(d + 1)) % p
    B = sum(a[r] * pow(z, r, p) for r in range(d + 1)) % p
    Q = sum(q[r] * pow(z, r, p) for r in range(d + 1)) % p
    tail = sum((8 * n + 1) * b[n] * pow(z, n, p)
               for n in range(d + 1, 2 * d + 1)) % p
    assert t == (B * Q - tail) % p
    derivative = sum(r * (8 * r + 1) * c[r] * pow(z, r - 1, p)
                     for r in range(1, d + 1)) % p
    return t, derivative, B, Q, tail


def main():
    thorough, observation = 0, 0
    sample = {}
    for p in primes_below(5000):
        if p < 7 or p % 4 != 3:
            continue
        d, c, a = port_coefficients(p)
        # Direct single-sum root/derivative observation over the wider finite range.
        t = sum((8 * r + 1) * c[r] * pow(9, r, p) for r in range(d + 1)) % p
        dt = sum(r * (8 * r + 1) * c[r] * pow(9, r - 1, p)
                 for r in range(1, d + 1)) % p
        assert t == 0, ("finite sample T", p, t)
        assert dt != 0, ("finite sample derivative", p, dt)
        observation += 1
        if p < 2000:
            verify_picard_fuchs(p, d, c, a)
            got = verify_clausen_tail(p, d, c, a)
            assert got[0] == t and got[1] == dt
            thorough += 1
            if p in (7, 11, 19, 43, 67):
                sample[p] = got
    assert sample[19][:1] == (0,)
    print(f"PASS_GH38_PICARD_FUCHS_RESONANCE {thorough} prime cases")
    print(f"PASS_GH39_GAUSS_CLAUSEN_TAIL {thorough} prime cases")
    print(f"OBSERVED_NOT_PROVED_T_9_SIMPLE_ROOT {observation} prime cases")
    for p, vals in sample.items():
        print(f"p={p}: T, Tprime, B, Q, high_tail = {vals}")


if __name__ == "__main__":
    main()
