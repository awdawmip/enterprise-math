"""Exact p^2 binomial/harmonic decomposition for D25 Cauchy endpoint H=K0+6 theta K0.

All arithmetic is integer modular arithmetic. The decomposition is proved independently
by shifting three Pochhammer parameters and one B-s factor at p=6r+1.
Not a proof of the character conjecture.
"""
from math import isqrt


def primes_upto(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[0:2]=b'\x00\x00'
    for i in range(2,isqrt(n)+1):
        if sieve[i]:
            sieve[i*i::i]=b'\x00'*((n-i*i)//i+1)
    return [p for p in range(7,n+1) if sieve[p] and p%6==1]


def check(p):
    assert p>=7 and p%6==1
    r=(p-1)//6
    mod=p*p
    ip=lambda n:pow(n%p,-1,p)
    im=lambda n:pow(n%mod,-1,mod)
    half=im(2)
    third=ip(3)
    twothirds=2*third%p
    # Original rational hypergeometric and reflection coefficients, reduced mod p^2.
    a=b=zpow=1
    U=H_original=0
    # Binomial approximants, and cumulative harmonic correction kernels.
    B3=B2=B4=1
    tpow=1
    two_pow=1
    V=E=H_binomial=H_harmonic=0
    h3=h2=h4=0
    core_modp=0
    for m in range(1,2*r+1):
        a=a*(2*m-1)*(3*m-2)*(3*m-1)*im(18*m**3)%mod
        b=b*(2*m-1)*im(4*m)%mod
        U=(U-im(4*m*b))%mod
        zpow=zpow*half%mod
        H_original=(H_original+(6*m+1)*a*U*zpow)%mod
        B3=B3*(3*r-m+1)*im(m)%mod
        B2=B2*(2*r-m+1)*im(m)%mod
        B4=B4*(4*r-m+1)*im(m)%mod
        tpow=tpow*(-half)%mod
        two_pow=two_pow*2%mod
        t_m=tpow*B3*B2*B4%mod
        # v_m = - (-1)^m 2^m / (4m C(3r,m)).
        v_m=((-1)**(m+1))*two_pow*im(4*m*B3)%mod
        V=(V+v_m)%mod
        h3=(h3+ip(3*r-m+1))%p
        h2=(h2+ip(2*r-m+1))%p
        h4=(h4+ip(4*r-m+1))%p
        beta=h3*ip(2)%p
        alpha=(h3*ip(2)+h2*third+h4*twothirds)%p
        E=(E+v_m*beta)%p
        base=(6*m+1)*t_m%mod
        H_binomial=(H_binomial+base*V)%mod
        H_harmonic=(H_harmonic+base*(E-alpha*(V%p)))%p
        core_modp=(core_modp+base*(V%p))%p
        # Strong pointwise tests of p-adic source decomposition.
        assert a==((-1)**m)*B3*B2*B4*(1-p*alpha)%mod, ('a',p,m)
        assert (-im(4*m*b))%mod==v_m*(1+p*beta)%mod, ('u',p,m)
    assert H_original==(H_binomial+p*H_harmonic)%mod, ('lift',p)
    character=1 if p%8 in (1,7) else -1
    candidate_delta=(core_modp-3*(character-1))%p
    return {'p':p,'r':r,'core_mod_p':core_modp,'character':character,
            'character_residue':candidate_delta,'H_mod_p2':H_original,
            'H_binomial_mod_p2':H_binomial,'harmonic_correction_mod_p':H_harmonic,
            'second_digit':((H_original-3*(character-1))%mod)//p}


if __name__=='__main__':
    ps=primes_upto(10000)
    good=0
    samples=[]
    for p in ps:
        out=check(p)
        good+=out['character_residue']==0
        if p in (7,13,19,31,37,43,61,73,373,1171):samples.append(out)
    print('EXACT-LIFT PASS %d/%d primes p<=10000, p=1 mod 6'% (len(ps),len(ps)))
    print('CHARACTER CONJECTURE FINITE CHECK (not general proof): %d/%d'% (good,len(ps)))
    for v in samples:print(v)
