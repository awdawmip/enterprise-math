#!/usr/bin/env python3
"""Author-side exact native-comparison falsifier; NOT the fixed H0/B0 benchmark.

For inert primes, no scalar sigma-semilinear rank-one module over
R_2=(Z/p^2)[T]/(T^2-2) can have square +p or -p modulo p^2.
Exhaustive p=13,19 integral coefficient check plus p=373 Hesse candidate.
"""

def prime_case(p):
    assert p in (13, 19, 373) and pow(2, (p-1)//2, p) == p-1
    m = p*p
    if p in (13,19):
        visited = unit = zero = odd_valuation = 0
        for a in range(m):
            for b in range(m):
                N = (a*a-2*b*b) % m
                assert (N % p != 0) or N == 0
                assert N not in (p,m-p)
                visited += 1
                if N==0: zero+=1
                else: unit+=1
        assert visited == m*m and zero == p*p
        return {'p':p,'all_ring_elements':visited,'unit_norm_count':unit,
                'zero_norm_mod_p2_count':zero,'norm_eq_plusminus_p':0}
    # p373: recompute Hesse candidate coefficient, without accepting it as native
    mod=p**3
    iv4=pow(4,-1,mod)
    u=(2*iv4%mod,-iv4%mod)
    def multiply(x,y):
        return ((x[0]*y[0]+2*x[1]*y[1])%mod,(x[0]*y[1]+x[1]*y[0])%mod)
    s=(0,0); power=(1,0); coef=1
    for k in range((p-1)//3+1):
        s=((s[0]+coef*power[0])%mod,(s[1]+coef*power[1])%mod)
        if k < (p-1)//3:
            coef=coef*(3*k+1)*(3*k+2)*(3*k+3)*pow(27*(k+1)**3,-1,mod)%mod
            power=multiply(power,u)
    assert all(x%p==0 for x in s)
    alpha=(s[0]//p,s[1]//p)
    N=(alpha[0]*alpha[0]-2*alpha[1]*alpha[1])%(p*p)
    assert N==122102 and N%p==131
    # Source-completed original E3 point count, consumed, not a new count
    assert 138384 == (p-1)**2
    return {'p':p,'hesse_alpha':alpha,'hesse_norm_mod_p2':N,
            'hesse_norm_mod_p':N%p,'original_geometric_p2_frobenius':'+p',
            'direct_rankone_identification':'EXCLUDED'}

if __name__=='__main__':
    for p in (13,19,373): print(prime_case(p))
