#!/usr/bin/env python3
"""R762GW exact BRC checks for the free eight-letter signed STAR candidate."""
from collections import defaultdict
from math import comb, pi
import json

def central(n):
    return comb(2*n,n)*sum(
        comb(n,j)**2 * comb(2*j,j) * comb(2*(n-j),n-j)
        for j in range(n+1)
    )

def support(m):
    return ((m+1)**2*(m*m+2*m+3))//3

def check_dp(max_m=8):
    zero=(0,0,0,0)
    states={zero:1}
    out=[]
    for m in range(max_m+1):
        zcount=states.get(zero,0)
        assert zcount == (central(m//2) if m%2==0 else 0)
        assert sum(states.values())==8**m
        assert len(states)==support(m)
        if m%2==0 and m>0:
            assert all(k==zero or n<zcount for k,n in states.items())
        out.append({"m":m,"words":8**m,"readouts":len(states),"zero_count":zcount})
        if m==max_m: break
        next_states=defaultdict(int)
        for z,n in states.items():
            for v in range(4):
                for sign in (-1,1):
                    a=list(z)
                    a[v]+=sign
                    next_states[tuple(a)]+=n
        states=dict(next_states)
    return out

def main():
    samples=[{"n":n,"m":2*n,"zero_count":central(n),"all_words":8**(2*n)}
             for n in range(13)]
    assert [samples[j]["zero_count"] for j in range(7)] == [
        1,8,168,5120,190120,7939008,357713664]
    dp=check_dp()
    diagnostics=[]
    for n in (12,24,48,64,128):
        p=central(n)/8**(2*n)
        r=p/(2/(pi*pi*n*n))
        diagnostics.append({"n":n,"p_float":p,"ratio_to_leading_float":r,
                            "n_times_relative_deviation_float":n*(r-1)})
    return {"result":"PASS","source_population":"free eight-letter signed STAR candidate",
            "exact_formula":"binom(2n,n)*sum_j binom(n,j)^2 binom(2j,j) binom(2n-2j,n-j)",
            "analytic_theorem":"P_2n=2/(pi^2*n^2)*(1-1/(2n)+O(n^-2))",
            "limitation":"asymptotic proved separately; finite numbers are not a proof; no native Port/Link/time admission",
            "samples":samples,"independent_integer_dp":dp,
            "float_diagnostics_not_proof":diagnostics}

if __name__=="__main__":
    print(json.dumps(main(),ensure_ascii=False,indent=2))
