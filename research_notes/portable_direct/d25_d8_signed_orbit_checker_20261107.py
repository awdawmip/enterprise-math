"""D25 author-side finite-field D8 signed-orbit certificate.

All operations are in F_p. This does not execute the native p=373
H0/B0 divided-power/Frobenius benchmark.
"""
from collections import Counter
from math import comb


def primes_up_to(limit):
    sieve = bytearray(b'\1') * (limit + 1)
    sieve[:2] = b'\0\0'
    for d in range(2, int(limit ** .5) + 1):
        if sieve[d]:
            sieve[d*d:limit+1:d] = b'\0' * ((limit - d*d)//d + 1)
    return [i for i in range(limit+1) if sieve[i]]


def check_prime(p):
    assert p % 24 in (13, 19)
    m = (p-1)//6
    i2 = pow(2, -1, p)
    c = pow(2, -m, p)
    assert pow(c, 3, p) == p-1
    roots = [u for u in range(1, p) if pow(u, 6, p) == 1]
    assert len(roots) == 6
    local = {((u + c * pow(u, -1, p)) % p) for u in roots}
    nonzero = local - {0}
    assert len(nonzero) == 2
    t = min(nonzero)
    assert nonzero == {t, (-t)%p}
    X = set(range(p)) - {0, 1, p-1}

    def sv(y):
        # y=2x+1, original f(x)=x^5(x+1)^2(2x+1)
        x = (y-1)*i2 % p
        return pow((pow(x, 5, p)*pow(x+1, 2, p)*y) % p, m, p)

    def leg(z):
        return pow(z % p, (p-1)//2, p)

    def T(y):
        return (y-1)*pow(y+1, -1, p) % p

    def s(y):
        return -y % p

    def q(y):
        return pow(y, -1, p)

    seen=set()
    orbit_count=0
    hist=Counter()
    survivors=0
    for first in sorted(X):
        if first in seen:
            continue
        O={first}; stack=[first]
        while stack:
            y=stack.pop()
            for image in (s(y), T(y)):
                assert image in X
                if image not in O:
                    O.add(image)
                    stack.append(image)
        assert not (O & seen)
        seen.update(O)
        orbit_count+=1
        O_sum=sum(sv(y) for y in O)%p
        reps=[y for y in O if leg(y)==1 and leg(y*y-1)==1]
        if p%24==13 and len(O)==2:
            assert not reps and O_sum==0
        else:
            assert len(O)==8
            if p%24==13:
                assert len(reps) in (0, 8)
                if reps:
                    survivors+=1
                    y=min(reps)
                    z=T(y)
                    assert z in reps
                    v,w=sv(y),sv(z)
                    expected=(4*(v+w))%p
                    assert v*w%p==c
                else:
                    expected=0
            else:
                assert len(reps)==2
                y=min(reps)
                z=q(T(y))
                assert z in reps and z!=y
                v,w=sv(y),sv(z)
                expected=(2*(v+w))%p
                assert v*w%p==c
            assert expected == O_sum
        if O_sum:
            d=4 if p%24==13 else 2
            assert O_sum in {(d*t)%p, (-d*t)%p}
            hist['+'] += O_sum == d*t%p
            hist['-'] += O_sum == -d*t%p
        else:
            hist['0'] += 1
    assert len(seen)==p-3
    expected_orbits = (p-5)//8 + 1 if p%24==13 else (p-3)//8
    assert orbit_count == expected_orbits
    assert sum(hist.values())==orbit_count
    S=sum(comb(m,k)*comb(2*m+k,k) for k in range(m+1))%p
    direct=sum(sv(y) for y in X)%p
    assert S==(-direct)%p
    d=4 if p%24==13 else 2
    assert S == (-d*t*(hist['+']-hist['-']))%p
    assert (S==0)==(hist['+']==hist['-'])
    assert S==0  # finite observation only
    return dict(p=p, m=m, c=c, t=t, plus=hist['+'], minus=hist['-'], zero=hist['0'], orbits=orbit_count, survivor_d8=survivors, S=S)


if __name__ == '__main__':
    ps=[p for p in primes_up_to(10000) if p%24 in (13,19)]
    results=[check_prime(p) for p in ps]
    assert len(results)==312
    for p in (13,19,43,61,67,373):
        print(next(r for r in results if r['p']==p))
    print('checked',len(results),'target primes <=10000; branch sizes:',
          Counter(r['p']%24 for r in results), '; failures=0')
    print('nonzero global D8 orbits:',sum(r['plus']+r['minus'] for r in results))
