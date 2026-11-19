#!/usr/bin/env python3
"""PREFIX-924: exact marginal-fiber collision mass and all weak strict-19-bit cases.

Pure Python 3, no dependencies, exact integer arithmetic. Does NOT enumerate
the actual 2^32-state XOR trace population. The proof gives the exact minimum
of a *necessary mass lower bound*, not the actual collision mass.
"""
import json
from collections import Counter

P=32
N=1 << P
T=P+1
LO=(1 << 18)+1
HI=(1 << 19)-1

def balanced_pairs(degree, bins):
    """Minimum sum binom(c_j,2) over nonnegative c_j summing to degree."""
    q,r=divmod(degree,bins)
    return bins*q*(q-1)//2+r*q

def marginal_bounds(a,b,p=P):
    n=1 << p
    t=p+1
    qa,ra=divmod(n,a)
    qb,rb=divmod(n,b)
    start=ra*balanced_pairs(t*(qa+1),b)+(a-ra)*balanced_pairs(t*qa,b)
    end=rb*balanced_pairs(t*(qb+1),a)+(b-rb)*balanced_pairs(t*qb,a)
    return start,end,max(start,end)

def all_small_candidates():
    """Completeness: 0 < max(start,end) <= 3 forces a positive side <= 3.
    For odd a|N? impossible as N is a power of two. On the positive
    start side, r=N mod a > 0. If b<t*floor(N/a) then mass >= 33*r > 3.
    Otherwise mass = r*(t*ceil(N/a)-b), so r<=3 and delta<=3//r.
    Repeat with a/b exchanged to cover the end-positive side.
    """
    small_remainders=[]
    proposed=set()
    for a in range(LO,HI+1,2):
        q,r=divmod(N,a)
        if 1 <= r <= 3:
            small_remainders.append((a,q,r))
            for delta in range(1,3//r+1):
                b=T*(q+1)-delta
                if LO <= b <= HI and b%2 == 1:
                    proposed.add((a,b))
                    proposed.add((b,a))
    evaluated=[(a,b,*marginal_bounds(a,b)) for a,b in sorted(proposed)]
    minimizers=[list(z) for z in evaluated if 0<z[4]<=3]
    assert small_remainders==[(327685,13107,1),(464773,9241,3)]
    assert minimizers==[[304985,464773,0,3,3],
                        [464773,304985,3,0,3]]
    assert all(z[4] >= 3 for z in evaluated if z[4]>0)
    return small_remainders,evaluated,minimizers

def brute_small_check():
    cases=0
    for p in range(1,6):
        n=1 << p
        traces=[(x,x,None) for x in range(n)]
        traces += [(x,x^(1 << i),i) for x in range(n) for i in range(p)]
        for a in range(1,n+4,2):
            for b in range(1,n+4,2):
                seen=Counter((x%a,y%b) for x,y,_ in traces)
                actual=sum(v*(v-1)//2 for v in seen.values())
                left,right,lower=marginal_bounds(a,b,p)
                assert actual >= lower >= left and lower >= right
                cases+=1
    return cases

def direct_witness():
    a,b,k,i=464773,304985,8131,7
    A=a*k
    H=1 << i
    left=(0,H)
    right=(A,A)
    assert A < N and (A-H) == 12391*b
    assert left != right
    assert (left[0]%a,left[1]%b)==(right[0]%a,right[1]%b)
    assert marginal_bounds(a,b)==(3,0,3)
    return {"a":a,"b":b,"source_bit":i,"zero_trace":[A,A],
            "flip_trace":[0,H],"start_gap":A,"end_gap":A-H,
            "a_multiplier":k,"b_multiplier":12391}

def main():
    remainders,candidates,minimizers=all_small_candidates()
    checks=brute_small_check()
    out={"schema":"PREFIX924_FIBER_MASS_EXACT_V1",
         "science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
         "model":{"p":P,"N":N,"source_count":T,
                  "odd_modulus_low":LO,"odd_modulus_high":HI,
                  "modulus_count":len(range(LO,HI+1,2))},
         "small_remainders":remainders,
         "weak_candidates":candidates,
         "min_positive_dual_mass":3,
         "ordered_minimizers":minimizers,
         "small_observer_full_enumeration_cases":checks,
         "direct_named_witness":direct_witness(),
         "claim":"minimum of the forced marginal lower bound, not actual collision count"}
    print(json.dumps(out,sort_keys=True,indent=2))

if __name__ == "__main__":
    main()
