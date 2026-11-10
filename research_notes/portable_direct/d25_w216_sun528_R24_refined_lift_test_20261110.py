#!/usr/bin/env python3
"""Exact check of Sun 5.28 CM binomial input in the new Sun 5.29 lift bridge.
Conjectural input is checked only on the stated finite set, never accepted.
"""
from math import comb
from d25_w216_sun529_fermat_terminal_bridge_20261110 import TARGET_PRIMES,target_check

def check_R24(p):
    assert p%24 in (13,19)
    a=(p-1)//2
    R=comb(a,p//24)*comb(a,(5*p)//24)%p
    assert R!=0
    p_,alpha,epsilon,q,u,lift=target_check(p)
    predicted_alpha=((-7)*pow(5*R,-1,p))%p if p%24==13 else pow(11*R,-1,p)
    predicted_epsilon=(q-3*predicted_alpha)%p
    assert alpha==predicted_alpha,(p,'Sun528-F0',alpha,predicted_alpha)
    assert epsilon==predicted_epsilon,(p,'refined-Sun529',epsilon,predicted_epsilon)
    return (p,p%24,R,alpha,epsilon,q,predicted_epsilon)

if __name__=='__main__':
    for p in TARGET_PRIMES:
        print(check_R24(p))
    print('PASS: 13 target-class finite R24 witnesses; source conjecture remains open.')
