#!/usr/bin/env python3
"""R749SSG: exact sharp additive noise radius for cutoff-only decoding."""
from fractions import Fraction
from math import comb
from itertools import product
import json
W=(1,1,2,3,6)

def populations(n):
    c=[0]*(n+1);t=[0]*(n+1);c[0]=1
    for j,w in enumerate(W):
        for v in range(w,n+1):
            x=c[v-w];c[v]+=x;t[v]+=t[v-w]+(x if j==0 else 0)
    C=[0]*(n+2);T=[0]*(n+2)
    for v in range(n+1):
        C[v+1]=C[v]+c[v];T[v+1]=T[v]+t[v]
    return C,T

def differences(a):
    d=[]
    while a:
        d.append(a[0]);a=[a[i+1]-a[i] for i in range(len(a)-1)]
    return d

def run():
    C,T=populations(300)
    def lo(q): return Fraction(T[q]-2,C[q]+2)
    def hi(q): return Fraction(T[q]+2,C[q]-2)
    def gapnum(q): return (T[q+1]-2)*(C[q]-2)-(T[q]+2)*(C[q+1]+2)
    def sepnum(q): return 201*gapnum(q)-(C[q]-2)*(C[q+1]+2)
    assert all(sepnum(q)>0 for q in range(7,36))
    coefs={}
    for b in range(36,42):
        a=differences([sepnum(b+6*j) for j in range(12)])
        assert a[11]==0 and all(x>0 for x in a[:11]),(b,a)
        coefs[str(b)]=a[:11]
        for j in (12,17,30):
            assert sum(comb(j,i)*a[i] for i in range(11))==sepnum(b+6*j)
    def vals(q):
        return {Fraction(T[q]+e,C[q]+d) for e in range(-2,3) for d in range(-2,3)}
    a=sorted(vals(6));b=sorted(vals(7))
    closest=min((abs(x-y),str(x),str(y)) for x in a for y in b)
    assert closest==(Fraction(1,201),'4/3','89/67'),closest
    assert lo(8)-hi(6)>Fraction(1,201)
    for q in range(7,300):assert lo(q+1)-hi(q)>Fraction(1,201)
    assert C[300]>1000000
    return {
      'unit':'R749SSG','status':'PASS','review':'AUTHOR_EXACT_NOT_REVIEWED',
      'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'predecessor':'R749SSF',
      'raw_ratio_cutoff_class_minimum_interclass_distance':'1/201',
      'sharp_strict_additive_noise_radius_for_cutoff_only':'1/402',
      'attaining_values':['4/3','89/67'],
      'finite_sepnum_checked_q':[7,35],
      'positive_newton_coefficients_sepnum_bases36_to41':coefs,
      'interpolation_external_checks':[12,17,30],
      'same_cutoff_error_pair_resolution_uniform_radius':'NONE_POSITIVE',
      'reason':'X(q,e+1,d)-X(q,e,d)=1/(C_q+d) tends to zero as q increases',
      'scope':'exact rational raw ratio with real additive measurement noise; cutoff-only recovery, not error-pair recovery'
    }

if __name__=='__main__':
    o=run()
    with open('R749SSG_SHARP_CUTOFF_NOISE_RESULTS.json','w') as f:json.dump(o,f,indent=2);f.write('\n')
    print('PASS',o['raw_ratio_cutoff_class_minimum_interclass_distance'])
