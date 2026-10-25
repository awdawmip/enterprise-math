#!/usr/bin/env python3
"""Independent C307 finite test suite and sharpness counterexample witnesses.

Bounded tests are not a universal proof. The general proof lives in
C307_AUTHOR_THEOREM_AND_PROOF_20261026.md.
"""
import random, json
from math import gcd, factorial
from C307_HETEROGENEOUS_NEWTON_CONTENT import adaptive_moduli,content_gcd_from_sample_residues

def eval_poly(coeffs, t):
    return sum(a*t**i for i,a in enumerate(coeffs))

def shifted_node_isolator(j,d,T):
    q=[1]
    for i in range(d+1):
        if i==j:continue
        a=T+i
        next_coeff=[0]*(len(q)+1)
        for k,x in enumerate(q):
            next_coeff[k]-=a*x
            next_coeff[k+1]+=x
        q=next_coeff
    assert q[-1]==1
    return q

def main():
    rng=random.Random(30720261026)
    cases=0; witnesses=0; saved_nodes=0
    for d in range(10):
        for s in range(1,122):
            M,h,moduli=adaptive_moduli(s,d)
            assert all(M%n==0 for n in moduli)
            assert all(moduli[j]==moduli[d-j] for j in range(d+1))
            for v in range(3):
                T=rng.randint(-9,9)
                coeffs=[rng.randint(-1000,1000) for _ in range(d+1)]
                if v==0: coeffs=[0]*(d+1)
                residues=[eval_poly(coeffs,T+j)%moduli[j] for j in range(d+1)]
                actual=content_gcd_from_sample_residues(s,d,residues)
                expected=s
                for a in coeffs: expected=gcd(expected,a)
                assert actual==expected,(d,s,T,coeffs,actual,expected)
                cases+=1
            if s>1:
                for j,n in enumerate(moduli):
                    # All relevant factors of n divide s <=121. Exact trial divisions
                    # suffice for this small independent test (not production code).
                    factors=[];r=n;p=2
                    while p*p<=r and p<=3000:
                        if r%p==0:
                            factors.append(p)
                            while r%p==0:r//=p
                        p+=1
                    if r>1:factors.append(r)
                    q=shifted_node_isolator(j,d,1)
                    value=eval_poly(q,1+j)
                    assert abs(value)==factorial(j)*factorial(d-j)
                    for p in [p for p in factors if s%p==0]:
                        lower=n//p
                        c=lower//gcd(lower,abs(value))
                        assert (c*value)%lower==0
                        assert gcd(s,c)!=s
                        witnesses+=1
                    if n<M:saved_nodes+=1
    report={"seed":30720261026,"exact_polynomials":cases,
        "individual_missing_prime_power_witnesses":witnesses,
        "nodes_strictly_smaller":saved_nodes,"max_test_degree":9,
        "s_range":[1,121]}
    print("C307_INDEPENDENT_SYNTHETIC_PASS",json.dumps(report,sort_keys=True))
if __name__=="__main__":main()
