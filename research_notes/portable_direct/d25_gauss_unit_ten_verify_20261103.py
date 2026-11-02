#!/usr/bin/env python3
"""Exact modular witness for the p-uniform Gauss far-edge unit and Clausen defect.

No external libraries, floating point, native task execution, or unproved theorem assumptions.
All operations are in Z/p^3Z or F_p; no division of a nonunit is performed.
"""
from __future__ import annotations
import json
from pathlib import Path


def primes(n: int):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * (((n - i*i)//i) + 1)
    return [i for i in range(7, n + 1) if sieve[i] and i % 6 == 1]


def verify(p: int):
    r = (p - 1)//6
    mod = p**3
    inv2 = pow(2, -1, mod)
    g_coeff = f_coeff = zpower = 1
    g_value = dg_value = w_value = 0
    for n in range(p):
        v = g_coeff*zpower % mod
        g_value = (g_value+v) % mod
        dg_value = (dg_value+n*v) % mod
        w_value = (w_value+(6*n+1)*f_coeff*zpower) % mod
        if n < p-1:
            np1 = n+1
            g_coeff = (g_coeff*(6*n+1)*(3*n+1)*pow(18*np1*np1, -1, mod))%mod
            f_coeff = (f_coeff*(2*n+1)*(3*n+1)*(3*n+2)*pow(18*np1**3, -1, mod))%mod
            zpower = zpower*inv2%mod
    assert g_coeff % (p*p) == 0, ('boundary valuation', p)
    u_direct = g_coeff // (p*p)
    u_closed = pow(10,-1,p)
    assert u_direct == u_closed, ('unit',p,u_direct,u_closed)
    defect_numerator=(w_value-g_value*g_value-12*g_value*dg_value)%mod
    assert defect_numerator % (p*p) == 0, ('Clausen valuation',p)
    e_direct=defect_numerator//(p*p)

    # Independently reconstruct the defect using only F_p moments and the 1/10 unit.
    ak=two_s=lk=inv2k=1
    lam=gam=total=0
    inv2p=pow(2,-1,p)
    for k in range(1,r+1):
        s=k-1
        lam=(lam+two_s*ak)%p
        gam=(gam+s*two_s*ak)%p
        two_s=two_s*2%p
        ak=ak*18*(s+1)**2*pow((6*s+11)*(3*s+5),-1,p)%p
        lk=lk*(r-k+1)*(2*r-k+1)*pow(k*k,-1,p)%p
        inv2k=inv2k*inv2p%p
        total=(total+lk*inv2k*((6*k-5)*lam-6*gam))%p
    e_closed=(-pow(5,-1,p)*total)%p
    assert e_direct == e_closed, ('defect',p,e_direct,e_closed)
    return {'p':p,'r':r,'U':u_direct,'E':e_direct,'sum_kernel':total,'Lambda_r':lam,'Gamma_r':gam}


def main():
    pts=primes(10000)
    examples={7,13,19,37,373,1171,9973}
    result={'scope':'all primes p<=10000, p=1 (mod 6), p>=7',
            'status':'author-side finite-exact computational validation; not universal proof or native experiment',
            'tested_count':0,'violations':0,'examples':[]}
    for p in pts:
        record=verify(p)
        result['tested_count']+=1
        if p in examples:result['examples'].append(record)
    p374=next((x for x in result['examples'] if x['p']==373),None)
    assert p374 is not None and p374['U']==112 and p374['E']==177
    out=Path('/mnt/data/d25_gauss_unit_ten_results_20261103.json')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == '__main__':main()
