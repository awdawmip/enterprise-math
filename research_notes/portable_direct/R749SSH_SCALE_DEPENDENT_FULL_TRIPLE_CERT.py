#!/usr/bin/env python3
"""R749SSH sharp full-triple noise margin for q>=28, exact rational arithmetic."""
from fractions import Fraction
from itertools import product
from math import comb
import json

WEIGHTS=(1,1,2,3,6)

def counts(limit):
    a=[0]*(limit+1);b=[0]*(limit+1);a[0]=1
    for j,w in enumerate(WEIGHTS):
        for v in range(w,limit+1):
            x=a[v-w];a[v]+=x;b[v]+=b[v-w]+(x if j==0 else 0)
    C=[0]*(limit+2);T=[0]*(limit+2)
    for v in range(limit+1):C[v+1]=C[v]+a[v];T[v+1]=T[v]+b[v]
    return C,T,a,b

def run():
    C,T,a,b=counts(500)
    def values(q):return sorted((Fraction(T[q]+e,C[q]+d),e,d) for e in range(-2,3) for d in range(-2,3))
    details=[];last_exception=None
    for q in range(6,501):
        arr=values(q)
        gap,i=min((arr[j+1][0]-arr[j][0],j) for j in range(24))
        wanted=Fraction(1,C[q]+2)
        if q<28:
            details.append({'q':q,'min_gap':str(gap),'candidate':str(wanted),'left':[arr[i][1],arr[i][2]],'right':[arr[i+1][1],arr[i+1][2]]})
            if gap!=wanted:last_exception=q
        else:
            assert gap==wanted,(q,gap,wanted)
            assert T[q]>=5*C[q]+10,(q,T[q]-5*C[q])
    assert last_exception==27
    assert T[28]-5*C[28]==726
    assert T[47]-5*C[47]>10
    # At shell weight m, five nonnegative n_j with sum L have average n1=L/5.
    # For every residue t_j in 0..6/w_j-1, weighted B<=17. Thus for m>=47,
    # L=(m-B)/6>=5 whenever integral, mean source1 count 6*L/5+t1>=6.
    # Consequently T_{m+1}-5*C_{m+1} increases from cutoff m=47 onward.
    for q in range(47,500):
        assert b[q]>=5*a[q],q
        assert T[q+1]-5*C[q+1]>=T[q]-5*C[q]
    # At any q>=28, different d yields |crossproduct|>=T-4C-8>=C+2.
    # Its denominator (C+d)(C+d') is strictly less than (C+2)^2.
    # Equal denominator with delta e=1 and d=2 yields exactly 1/(C+2).
    return {
        'unit':'R749SSH','status':'PASS','review':'AUTHOR_EXACT_NOT_REVIEWED',
        'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'exact_minimum_same_cutoff_ratio_separation_for_all_integer_q_ge':28,
        'formula':'1/(C_q+2)',
        'sharp_strict_noise_radius_for_full_triple_conditional_on_true_q_ge_28':'1/(2*(C_q+2))',
        'sharp_transition_q':28,'last_counterexample_cutoff':last_exception,
        'C27':C[27],'T27':T[27], 'C28':C[28],'T28':T[28],
        'q28_T_minus_5C':T[28]-5*C[28],
        'finite_monotonic_base_q':[28,47],
        'shell_monotonic_from_exact_weight_q':47,
        'finite_exact_minimum_distances_q6_to27':details,
        'same_cutoff_exact_enumeration_q':[6,500],
        'source_count_and_marked_count_independent_direct_dp':True,
        'other_cutoff_separation':'at least 1/201 for all q>=6 by R749SSG',
        'scope':'raw ratio with integer errors +/-2; exact all q>=28 proof; local q-dependent robust recovery of cutoff and two errors; not native X6 or smooth-subtracted Y'
    }

if __name__=='__main__':
    o=run()
    with open('R749SSH_SCALE_DEPENDENT_FULL_TRIPLE_RESULTS.json','w') as f:json.dump(o,f,indent=2);f.write('\n')
    print(o['status'],o['C27'],o['T27'],o['C28'],o['T28'])
