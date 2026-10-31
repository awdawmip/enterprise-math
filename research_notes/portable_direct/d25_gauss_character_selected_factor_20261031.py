#!/usr/bin/env python3
"""Exact finite evidence for character-selected p^2 vanishing of β Gauss factors.

No infinite-prime theorem or native H0/B0 computation is claimed.
"""
from math import comb, factorial


def primes_upto(n):
    is_prime = bytearray(b'\x01') * (n + 1)
    is_prime[:2] = b'\x00\x00'
    for k in range(2, int(n ** 0.5) + 1):
        if is_prime[k]:
            is_prime[k*k:n+1:k] = b'\x00' * ((n-k*k)//k + 1)
    return [p for p in range(5,n+1) if is_prime[p]]


def beta_coefficients(p, power=2):
    q = p**power
    b=[1]
    for k in range(p-1):
        b.append(b[-1]*(8*k+1)*(8*k+3)*pow(576*(k+1)**2, -1, q) % q)
    return b


def one_prime(p):
    assert p%8 in (5,7)
    q=p*p
    b=beta_coefficients(p)
    g=sum(b)%q
    h=sum((16*k+1)*b[k] for k in range(p))%q
    character_3=1 if pow(3,(p-1)//2,p)==1 else -1
    assert p%24 in (5,7,13,23)
    selected=g if character_3==1 else h
    complement=h if character_3==1 else g
    # The selected factor satisfies a new finite experimental conjecture.
    assert selected == 0,(p,g,h)
    assert complement % p != 0,(p,g,h)
    # External theorem: B_p = p chi_{-3} mod p^3, and beta Clausen split.
    # This particular modular product zero is checked independently here.
    assert g*h % q == 0
    if p in (5,7,13,23,29,31,37,373):
        # Numerator/denominator product independent of ratio recurrence.
        for k in (0,1,p//2,p-1):
            numerator=1
            for j in range(k):
                numerator *= (8*j+1)*(8*j+3)
            denominator=576**k * factorial(k)**2
            assert b[k]==(numerator*pow(denominator,-1,q))%q
    result=dict(p=p,character_3=character_3,g_mod_p2=g,h_mod_p2=h,
                p2_zero_factor='g' if character_3==1 else 'h',
                complementary_unit=complement%p)
    if p in (5,7,13,23,29,31,37,373):
        higher=beta_coefficients(p,3)
        g3=sum(higher)%(p**3)
        h3=sum((16*k+1)*higher[k] for k in range(p))%(p**3)
        result['selected_div_p2_mod_p'] = ((g3 if character_3==1 else h3)//q)%p
    return result


def main():
    rows=[one_prime(p) for p in primes_upto(1200) if p%8 in (5,7)]
    assert len(rows)==100
    print('PASS p<=1200 all',len(rows),'primes p mod8 in {5,7}')
    print('Character +1 selected g:',sum(r['character_3']==1 for r in rows))
    print('Character -1 selected h:',sum(r['character_3']==-1 for r in rows))
    for r in rows:
        if r['p'] in (5,7,13,23,29,31,37,61,71,79,109,373):
            print(r)


if __name__=='__main__':main()
