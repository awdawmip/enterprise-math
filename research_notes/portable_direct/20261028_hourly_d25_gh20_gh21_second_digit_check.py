#!/usr/bin/env python3
"""GH-20 / GH-21: exact modular-rational checks of two p-adic Gauss source moments.

No numpy, floats, automatic admission or native Enterprise Math experiment.
"""
from math import comb
from fractions import Fraction


def primes_below(n):
    a = bytearray(b'\x01') * n
    a[0:2] = b'\x00\x00'
    for k in range(2, int(n**0.5) + 1):
        if a[k]:
            a[k*k:n:k] = b'\x00' * ((n-1-k*k)//k + 1)
    return [i for i in range(2, n) if a[i]]


def moment_packet(p, z=9):
    assert p >= 11 and p % 8 == 3
    m = (p-3)//8
    modulus = p*p
    a = c = 1
    nu = 0
    fp = gp = fh = gh = k = kg = gprime_scaled = 0
    zpower = 1
    terms = []
    for r in range(m+1):
        weight = (16*r + 5)
        fp = (fp + a*zpower) % modulus
        gp = (gp + weight*a*zpower) % modulus
        gprime_scaled = (gprime_scaled + weight*r*a*zpower) % modulus
        fh = (fh + c*zpower) % modulus
        gh = (gh + weight*c*zpower) % modulus
        k = (k + (c%p)*nu*(zpower%p)) % p
        kg = (kg + weight*(c%p)*nu*(zpower%p)) % p
        terms.append((r,a,c,nu))
        if r < m:
            a = a*(m-r)**2*pow((2*m+2+r)*(r+1), -1, modulus) % modulus
            c = c*(8*r+3)**2*pow(16*(4*r+5)*(r+1), -1, modulus) % modulus
            nu = (nu + 2*pow(8*r+3,-1,p) + pow(4*r+5,-1,p))%p
            zpower = zpower*z%modulus
    assert (fh-p*k) % modulus == fp
    assert (gh-p*kg) % modulus == gp
    for r,a,c,nu in terms:
        assert a == (c*(1-p*nu))%modulus, (p,r,a,c,nu)
    # Independently verify the exact binomial model GH-19 and its first derivative.
    if p < 1500:
        b0 = sum(comb(3*m+1,m-r)*comb(m,r)*pow(z,r,modulus) for r in range(m+1))%modulus
        b1 = sum((16*r+5)*comb(3*m+1,m-r)*comb(m,r)*pow(z,r,modulus) for r in range(m+1))%modulus
        d = comb(3*m+1,m)
        assert d%p
        assert b0*pow(d,-1,modulus)%modulus == fp
        assert b1*pow(d,-1,modulus)%modulus == gp
    return {'p':p, 'm':m, 'F':fp, 'G':gp, 'hatF':fh, 'hatG':gh, 'K':k, 'KG':kg,
            'F_mod_p':fp%p, 'Fprime':((gp-5*fp)*pow(16*z,-1,modulus))%modulus,
            'Gprime':gprime_scaled*pow(z,-1,modulus)%modulus,
            'has_F_root':fp%p==0}


def hensel_packet(p, channel=None):
    r=moment_packet(p)
    channel = channel or ('F' if p%24==19 else 'G')
    assert channel in ('F','G')
    if r[channel]%p: return None
    hat = 'hat'+channel
    corr = 'K' if channel=='F' else 'KG'
    q=r[channel]//p
    qh=r[hat]//p
    assert (qh-r[corr])%p == q%p
    d=r[channel+'prime']%p
    assert d, (p,channel,'non-simple root')
    u=(-q*pow(d,-1,p))%p
    lift=(9+p*u)%(p*p)
    other=moment_packet(p,lift)
    assert other[channel]==0,(p,channel,r,lift,other)
    r.update(channel=channel,q=q, q_hat=qh, derivative_mod_p=d, u=u, root_mod_p2=lift)
    return r


def exact_small_p_rational_check():
    for p in (11,19,43):
        m=(p-3)//8
        def poch(q,k):
            v=Fraction(1)
            for j in range(k):v*=q+j
            return v
        for z in (9,9+p,9+2*p):
            rat=sum((poch(Fraction(-m),r)**2/poch(Fraction(2*m+2),r)/__import__('math').factorial(r))*z**r for r in range(m+1))
            assert rat.denominator%p
            mod=rat.numerator*pow(rat.denominator,-1,p*p)%(p*p)
            assert mod == moment_packet(p,z)['F']


def main():
    exact_small_p_rational_check()
    primes=[p for p in primes_below(10000) if p>=11 and p%8==3]
    root19=[p for p in primes if p%24==19]
    root11=[p for p in primes if p%24==11]
    for p in primes:
        packet=moment_packet(p)
        if p%24==19:
            assert packet['has_F_root'],p  # finite observation, NOT universal proof
            assert hensel_packet(p, 'F')
        if p%24==11:
            assert packet['G']%p == 0,p  # finite observation, NOT universal proof
            assert packet['F']%p != 0,p
            assert hensel_packet(p, 'G')
    examples=[hensel_packet(p) for p in (11,19,43,59,67,139,163,211)]
    print('PASS_GH20_TWO_CHANNEL_MOD_P2_FIRST_VARIATION',len(primes),'p=3 mod 8 primes <10000')
    print('PASS_GH21_CONDITIONAL_TWO_BRANCH_HENSEL_LIFT',len(primes),'simple-root samples with exact mod-p2 readback')
    print('OBS_F_BRANCHED_ZERO',len(root19),'p=19 mod24 samples <10000')
    print('OBS_G_BRANCHED_ZERO',len(root11),'p=11 mod24 samples <10000')
    print('OBS_NONZERO_FIRST_DIGIT_QUOTIENT',sum(x['q']%x['p']!=0 for x in (hensel_packet(p) for p in primes)), 'of',len(primes))
    for x in examples:
        print('CERT', {k:x[k] for k in ('p','m','channel','q','q_hat','K','KG','derivative_mod_p','u','root_mod_p2')})

if __name__=='__main__':main()
