"""D25 author-side exact p-adic Gauss second jet; no native authorization claimed."""
from collections import Counter


def primes(bound):
    s = bytearray(b'\x01') * (bound + 1)
    s[:2] = b'\x00\x00'
    for k in range(2, int(bound**.5) + 1):
        if s[k]:
            s[k*k:bound+1:k] = b'\x00' * ((bound-k*k)//k+1)
    return [p for p in range(5, bound+1) if s[p]]


def observers(p):
    m = p**3
    inv = [0] * p
    inv[1] = 1
    for j in range(2, p):
        inv[j] = -(m//j)*inv[m % j] % m
    step = pow(576, -1, m)
    t = 1
    f = g = fp = gp = gpp = 0
    for k in range(p):
        w = 16*k+1
        f = (f+t) % m
        g = (g+w*t) % m
        fp = (fp+9*k*t) % m
        gp = (gp+9*k*w*t) % m
        gpp = (gpp+81*k*(k-1)*w*t) % m
        if k+1 < p:
            j = k+1
            t = t*(8*k+1)*(8*k+3)*step*inv[j]*inv[j] % m
    return f,g,fp,gp,gpp


def check(bound=10000):
    counts = Counter()
    samples = []
    for p in primes(bound):
        m = p**3
        d = 3 if p % 8 in (1, 3) else 35
        f,g,fp,gp,gpp = observers(p)
        d1 = (gp - 9*pow(8,-1,m)*g + 9*pow(32,-1,m)*f) % m
        d2 = (gpp + (1701*g-2673*f)*pow(512,-1,m)) % m
        assert d1 == -9*d*pow(32,-1,m)*p*p % m, ('first jet', p)
        assert d2 == 243*d*pow(128,-1,m)*p*p % m, ('second jet', p)
        assert (d2 - 9*(4*p-3)*pow(4,-1,m)*d1) % m == 0, ('transport', p)
        counts['all_prime_jet_checks'] += 1
        if p % 8 in (5,7):
            name = 'F' if p % 24 in (13,23) else 'G'
            value, slope = (f,fp) if name == 'F' else (g,gp)
            assert value % p == 0 and slope % p != 0, ('first digit', p)
            displacement = -(value//p)*pow(slope,-1,p) % p
            assert value % (p*p) == 0 and displacement == 0, ('Hensel root', p)
            counts['root_' + name + '_mod_p2'] += 1
            if p in (13,23,29,373,2053):
                samples.append((p,name, f%(p*p),g%(p*p),slope%p, displacement, d1//(p*p), d2//(p*p)))
    print('PASS', 'bound',bound, 'counts',dict(counts), 'samples',samples)


if __name__ == '__main__':
    check()
