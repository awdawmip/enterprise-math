#!/usr/bin/env python3
"""Author-side exact p-adic tests for prime-index Gauss/Clausen mirror lifting.
No native Enterprise Math execution, admission, or independent review is claimed.
"""
from itertools import accumulate


def primes(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for j in range(2, int(limit ** .5) + 1):
        if sieve[j]:
            sieve[j*j:limit+1:j] = b'\x00' * ((limit-j*j)//j+1)
    return [p for p in range(7, limit+1) if sieve[p] and p % 6 == 1]


def inv(n, q):
    return pow(n % q, -1, q)


def seq(p, power, numerator, divisor):
    q = p ** power
    acc = [1]
    for n in range(p-1):
        acc.append(acc[-1] * numerator(n) * inv(divisor(n), q) % q)
    return acc


def check_prime(p):
    m = (p-1)//6
    q = p*p
    b = seq(p, 4, lambda n:(6*n+1)*(3*n+1), lambda n:36*(n+1)**2)
    c = seq(p, 2, lambda n:(6*n+5)*(3*n+2), lambda n:36*(n+1)**2)
    a = seq(p, 5, lambda n:(2*n+1)*(3*n+1)*(3*n+2), lambda n:36*(n+1)**3)
    ga = []
    cl = []
    hga = 0
    hcl = 0
    for k in range(1,4*m+1):
        assert b[p-k] % p**2 == 0, ('G valuation',p,k)
        assert c[k] % p != 0, ('G unit',p,k)
        g = (36*k*k*c[k]*(b[p-k]//(p*p))) % q
        ga.append(g)
        assert g % p == 1, ('G modp mirror',p,k,g)
        if k>1:
            dg=(2*inv(k-1,q)-6*inv(6*k-1,q)-3*inv(3*k-1,q))%q
            hga=(hga-dg)%q
            assert g*inv(ga[0],q)%q == (1+p*hga)%q, ('G lift',p,k,g,ga[0],hga)
            lhs=ga[k-2]*inv(g,q)%q
            rhs=((1-6*p*inv(6*k-1,q))*(1-3*p*inv(3*k-1,q))*inv((1-p*inv(k-1,q))**2,q))%q
            assert lhs == rhs, ('G exact ratio',p,k)
    for k in range(1,2*m+1):
        assert a[p-k] % p**3 == 0, ('C valuation',p,k)
        assert a[k] % p != 0, ('C unit',p,k)
        v=(-18*k**3*a[k]*(a[p-k]//p**3))%q
        cl.append(v)
        assert v%p == 1, ('C modp mirror',p,k,v)
        if k>1:
            dc=(3*inv(k-1,q)-2*inv(2*k-1,q)-3*inv(3*k-1,q)-3*inv(3*k-2,q))%q
            hcl=(hcl-dc)%q
            assert v*inv(cl[0],q)%q == (1+p*hcl)%q, ('C lift',p,k,v,cl[0],hcl)
            lhs=cl[k-2]*inv(v,q)%q
            rhs=((1-2*p*inv(2*k-1,q))*(1-3*p*inv(3*k-1,q))*(1-3*p*inv(3*k-2,q))*inv((1-p*inv(k-1,q))**3,q))%q
            assert lhs == rhs, ('C exact ratio',p,k)

    # One further p-adic digit of the original weighted p^4 tail observer:
    # Q^{[2]} is a new p^5-normalized readout, not the old Q mod p.
    Q2 = 0
    baseC = 0
    corrC = 0
    hc = 0
    for k in range(1,2*m+1):
        if k>1:
            dc=(3*inv(k-1,q)-2*inv(2*k-1,q)-3*inv(3*k-1,q)-3*inv(3*k-2,q))%q
            hc=(hc-dc)%q
        Q2 += (6*(p-k)+1)*(a[p-k]//p**3)
        denom=inv(18*k**3*a[k],q)
        baseC=(baseC+(6*k-1)*denom)%q
        corrC=(corrC+((6*k-1)*hc-6)*denom)%p
    Q2%=q
    assert Q2 == cl[0]*(baseC+p*corrC)%q, ('C weighted lift',p,Q2,baseC,corrC)

    # New p^2 signed reciprocal lift: original high-index definition vs
    # complementary lower-index two-moment formula with lifted unit + harmonic port.
    if p%24 in (13,19):
        Rp2 = 0
        moment = 0
        hg = 0
        for k in range(1,m+1):
            if k>1:
                dg=(2*inv(k-1,q)-6*inv(6*k-1,q)-3*inv(3*k-1,q))%q
                hg=(hg-dg)%q
            # reverse finite convolution, still retain each original source index:
            weighted=sum(b[i]*(1+6*(i-k)) for i in range(k,m+1))%q
            Rp2 += 2*weighted*(b[p-k]//(p*p))
            moment += weighted*inv(18*k*k*c[k],q)*(1+p*hg)
        Rp2%=q
        moment=moment*ga[0]%q
        assert Rp2==moment, ('G signed lift',p,Rp2,moment)
    else: Rp2=None

    return {'p':p,'G_endpoint':ga[0],'C_endpoint':cl[0],
            'G_last':ga[-1],'C_last':cl[-1], 'R_lift':Rp2,'Q_lift':Q2,
            'G_pairs':len(ga), 'C_pairs':len(cl)}


def main():
    tested = [check_prime(p) for p in primes(3000)]
    assert len(tested)>100
    tested += [check_prime(p) for p in [373,1327] if p>3000]
    for p in [13,19,37,157,373,1327]:
        result=next(item for item in tested if item['p']==p)
        print('ANCHOR',result)
    print('SUMMARY','primes',len(tested),
          'gauss_pairs',sum(x['G_pairs'] for x in tested),
          'clausen_pairs',sum(x['C_pairs'] for x in tested),
          'target_signed_lifts',sum(x['R_lift'] is not None for x in tested))
    print('PASS_D25_SECOND_DIGIT_GAUSS_CLAUSEN_MIRROR_EXACT')

if __name__=='__main__':
    main()
