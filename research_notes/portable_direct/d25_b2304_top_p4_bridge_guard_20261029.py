#!/usr/bin/env python3
"""Author-only exact B2304 p^4 top-tier and 216/2304 signed-bridge source checker.

For p>=5 every denominator here is a p-adic unit. This is a scalar
finite calculation, not the native H0/B0 divided-power experiment.
"""
from math import comb, factorial


def primes_below(bound):
    mask = bytearray(b'\x01') * bound
    mask[:2] = b'\x00\x00'
    for d in range(2, int(bound**0.5) + 1):
        if mask[d]:
            for j in range(d * d, bound, d):
                mask[j] = 0
    return [p for p in range(5, bound) if mask[p]]


def weighted_streams(p):
    mod = p**4
    a = b = 1
    sa = sb = ata = btb = 0
    a_cut = (2*p + 2)//3  # ceil(2p/3)
    b_cut = (3*p + 3)//4  # ceil(3p/4)
    for n in range(p):
        wa, wb = (6*n + 1)*a % mod, (8*n + 1)*b % mod
        sa, sb = (sa+wa)%mod, (sb+wb)%mod
        if n >= a_cut:
            assert wa%p**3 == 0
            ata=(ata+wa)%mod
        if n >= b_cut:
            assert wb%p**3 == 0
            btb=(btb+wb)%mod
        k=n+1
        if k < p:
            a=a*(2*k-1)*(3*k-2)*(3*k-1)*pow(36*k**3,-1,mod)%mod
            b=b*(2*k-1)*(4*k-3)*(4*k-1)*pow(288*k**3,-1,mod)%mod
    return sa, sb, ata, btb


def reflected_top(p):
    # Independent small factorials; every displayed denominator < p.
    ra = sum(
        2*(6*r+5)*pow(216,r,p)*pow(factorial(r),5,p)
        *pow(factorial(2*r+1)*factorial(3*r+2),-1,p)
        for r in range((p-3)//3+1))%p
    rb = sum(
        6*(8*r+7)*pow(2304,r,p)*pow(factorial(r),4,p)
        *pow(factorial(4*r+3),-1,p)
        for r in range((p-4)//4+1))%p
    return ra,rb


def raw_binomial(p):
    mod=p**4
    ia,ib=pow(216,-1,mod),pow(2304,-1,mod)
    powa=powb=1
    sa=sb=ata=btb=0
    for n in range(p):
        wa=(6*n+1)*comb(2*n,n)**2*comb(3*n,n)*powa %mod
        wb=(8*n+1)*comb(2*n,n)**2*comb(4*n,2*n)*powb %mod
        sa=(sa+wa)%mod;sb=(sb+wb)%mod
        if n >= (2*p+2)//3: ata=(ata+wa)%mod
        if n >= (3*p+3)//4: btb=(btb+wb)%mod
        powa=powa*ia%mod;powb=powb*ib%mod
    return sa,sb,ata,btb


def verify(bound=1500):
    ps=primes_below(bound)
    assert len(ps)==237
    nonzero=0
    for p in ps:
        a,b,at,bt=weighted_streams(p)
        ar,br=reflected_top(p)
        assert (at//p**3,bt//p**3)==(ar,br), (p,'reflected top')
        chi=1 if p%3==1 else -1
        gap=(ar-2*br)%p
        if gap: nonzero+=1
        full=(a-2*b+p*chi)%p**4
        low=(a-at-2*(b-bt)+p*chi)%p**4
        assert (full-low)%p**4==(at-2*bt)%p**4
        if full==0:
            assert low==(-p**3*gap)%p**4
    fixtures={
        13:(5,6,6),19:(4,16,10),373:(278,119,40)
    }
    for p,(ar,br,gap) in fixtures.items():
        assert weighted_streams(p)==raw_binomial(p)
        aa,bb,at,bt=weighted_streams(p)
        assert reflected_top(p)==(ar,br)
        assert (ar-2*br)%p==gap
        chi=1 if p%3==1 else -1
        assert (aa-2*bb+p*chi)%p**4==0
        low=(aa-at-2*(bb-bt)+p*chi)%p**4
        print(f'p={p} A_top_over_p3={ar} B_top_over_p3={br} '
              f'Aminus2B_top_over_p3={gap} low_bridge_over_p3={low//p**3}')
    print('PASS_D25_B2304_P4_REFLECTED_TOP',len(ps),'primes <',bound,
          'nonzero_signed_top_gap',nonzero)
    print('PASS_RAW_ORIGINAL_BINOMIAL',tuple(fixtures))


if __name__=='__main__':
    verify()
