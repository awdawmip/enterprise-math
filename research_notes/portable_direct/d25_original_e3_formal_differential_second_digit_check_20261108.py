#!/usr/bin/env python3
"""Author-side exact original E3 formal-differential vs cubic Hasse coefficient.

All arithmetic is in (Z/p^3)[T]/(T^2-2); numbers are exact integers.
The finite-sum route and formal differential recurrence are independent.
"""
import json
from math import comb


def run_prime(p):
    modulus = p**3
    def plus(x,y): return ((x[0]+y[0])%modulus,(x[1]+y[1])%modulus)
    def neg(x): return ((-x[0])%modulus,(-x[1])%modulus)
    def sub(x,y): return plus(x,neg(y))
    def mul(x,y): return ((x[0]*y[0]+2*x[1]*y[1])%modulus,
                          (x[0]*y[1]+x[1]*y[0])%modulus)
    def scale(x,k): return ((k*x[0])%modulus,(k*x[1])%modulus)
    inv108=pow(108,-1,modulus)
    c=(2*inv108%modulus,-inv108%modulus)
    one=(1,0)

    # Original Tate uniformizer: t=-x/y; invariant differential f(t)dt
    # 2n f_n = 2(2n-1) f_{n-1} - (2n-2) f_{n-2} + 4c(2n-3) f_{n-3}.
    f=[one]
    for n in range(1,p):
        a=scale(f[n-1],2*(2*n-1))
        b=scale(f[n-2],-(2*n-2)) if n>=2 else (0,0)
        d=mul(scale(c,4*(2*n-3)),f[n-3]) if n>=3 else (0,0)
        f.append(scale(plus(plus(a,b),d),pow(2*n,-1,modulus)))
    b_formal=f[p-1]

    n=(p-1)//2
    m=(p-1)//3
    power=one
    b_sum=(0,0)
    h_sum=(0,0)
    a_sum=(0,0)
    harmonic_sum=(0,0)
    for k in range(m+1):
        a=comb(3*k,k)*comb(2*k,k)
        b_factor=comb(2*k,k)*comb(p-1-k,2*k)
        h_factor=comb(n,k)*comb(p-1-2*k,k)*4**k
        b_sum=plus(b_sum,scale(power,b_factor))
        h_sum=plus(h_sum,scale(power,h_factor))
        a_sum=plus(a_sum,scale(power,a))
        harmonic=sum(pow(j,-1,modulus) for j in range(1,k+1))%modulus
        harmonic_sum=plus(harmonic_sum,scale(power,a*harmonic))
        power=mul(power,c)
    assert b_formal==b_sum,(p,b_formal,b_sum)
    difference=sub(h_sum,b_formal)
    expected=scale(harmonic_sum,-p*pow(2,-1,modulus))
    assert tuple(x%(p*p) for x in difference)==tuple(x%(p*p) for x in expected),p
    assert all(v%p==0 for v in b_formal+h_sum) if p%24 in (13,19) else True
    t_diff=tuple((v//p)%p for v in difference) if all(x%p==0 for x in difference) else None
    out={
        'p':p,'modulus_p3':modulus,'c':c,
        'formal_differential_b_p_minus_1_mod_p3':b_formal,
        'cubic_Hasse_H_p_mod_p3':h_sum,
        'Hesse_A_p_mod_p3':a_sum,
        'formal_quotient_mod_p2':tuple((v//p)%(p*p) for v in b_formal) if all(v%p==0 for v in b_formal) else None,
        'Hasse_quotient_mod_p2':tuple((v//p)%(p*p) for v in h_sum) if all(v%p==0 for v in h_sum) else None,
        'H_minus_formal_over_p_mod_p':t_diff,
        'harmonic_sum_Hk_mod_p':tuple(v%p for v in harmonic_sum),
        'verified': True,
    }
    assert t_diff==tuple((-pow(2,-1,p)*v)%p for v in out['harmonic_sum_Hk_mod_p'])
    return out

if __name__=='__main__':
    results=[run_prime(p) for p in (13,19,37,43,61,67,211,373)]
    print(json.dumps(results,indent=2,ensure_ascii=False))
