#!/usr/bin/env python3
"""R132: exact one-integer difference-word feasibility, A=B,d=E=1,x=0."""
from fractions import Fraction
from itertools import product
import json
import random
from time import perf_counter_ns
from statistics import median

def direct_word(t,B,m):
    assert B>=2 and m>=1 and 0<t<1
    def frac(x):return x - (x.numerator//x.denominator)
    return tuple(int(frac((B+i)*t)<t) for i in range(m))

def ceildiv(a,b):
    assert b>0
    return -((-a)//b)

def solve(B,w):
    """Return exact witness theta or None for arbitrary target bits."""
    assert B>=2 and w and all(bit in (0,1) for bit in w)
    m=len(w)
    s=[0]
    for bit in w:s.append(s[-1]+bit)
    # Index a=-1..m-1; g[a]=sum_{i=0}^a w_i with g[-1]=0.
    ix=list(range(-1,m))
    def g(a):return s[a+1]
    lo=0
    hi=B-2
    for a in ix:
        for b in ix:
            if a==b:continue
            c=b-a
            rhs=(B+a)*(g(b)+1)-(B+b)*g(a)
            if c>0:
                hi=min(hi,ceildiv(rhs,c)-1)
            else:
                lo=max(lo,rhs//c+1)
    if lo>hi:return None
    q=lo
    l=max([Fraction(0)]+[Fraction(q+g(a),B+a) for a in ix])
    u=min([Fraction(1)]+[Fraction(q+g(a)+1,B+a) for a in ix])
    assert l<u,(B,w,q,l,u)
    t=(l+u)/2
    assert direct_word(t,B,m)==tuple(w),(B,w,q,t,direct_word(t,B,m))
    return t

def direct_atoms(B,m):
    cuts=set()
    for i in range(m):
        for den in (B+i,B+i-1):
            cuts.update(Fraction(k,den) for k in range(1,den))
    cuts=sorted(cuts)
    pp=[Fraction(0),*cuts,Fraction(1)]
    for j in range(len(pp)-1):
        yield direct_word((pp[j]+pp[j+1])/2,B,m)
        if j<len(cuts):yield direct_word(cuts[j],B,m)

def exhaustive():
    instances=0
    tested_patterns=0
    atom_positions=0
    possible_patterns=0
    for B in range(2,19):
        for m in range(1,9):
            atoms=list(direct_atoms(B,m))
            observed=set(atoms)
            atom_positions+=len(atoms)
            for w in product((0,1),repeat=m):
                t=solve(B,w)
                assert (t is not None)==(w in observed),(B,m,w,t)
                tested_patterns+=1
                possible_patterns+=t is not None
            instances+=1
    return {"B_range":"2..18","m_range":"1..8","instances":instances,
            "independent_exact_atoms":atom_positions,"all_binary_patterns_tested":tested_patterns,
            "attainable_patterns":possible_patterns}

def random_checks():
    rng=random.Random(132)
    n=0;yes=0
    for _ in range(5000):
        B=rng.randrange(2,10**6)
        m=rng.randrange(1,41)
        w=tuple(rng.randrange(2) for _ in range(m))
        t=solve(B,w)
        if t is not None:
            assert direct_word(t,B,m)==w
            yes+=1
        n+=1
    return {"count":n,"with_exact_witness":yes}

def huge():
    B=10**150+123
    m=64
    vals={}
    for name,w in (("all_zero",(0,)*m),("all_one",(1,)*m),("onehot_0",(1,)+(0,)*(m-1)),("onehot_last",(0,)*(m-1)+(1,))):
        t=solve(B,w)
        assert t is not None
        vals[name]={"numerator_digits":len(str(t.numerator)),"denominator_digits":len(str(t.denominator))}
    return {"B_digits":len(str(B)),"m":m,"valid_witnesses":vals}

def compare_runtime():
    rows=[]
    for B in (64,256,1024,4096):
        m=12
        w=(0,)*(m-1)+(1,)
        qtimes=[]; ttimes=[]
        for _ in range(3):
            st=perf_counter_ns();t=solve(B,w);qtimes.append((perf_counter_ns()-st)/1e6)
            assert t is not None
            st=perf_counter_ns();v=set(direct_atoms(B,m));ttimes.append((perf_counter_ns()-st)/1e6)
            assert w in v
        rows.append({"B":B,"m":m,"decision_median_ms":median(qtimes),"all_trace_enum_median_ms":median(ttimes),"candidate_count":len(v)})
    return rows

if __name__=='__main__':
    result={"schema":"EM_R132_DIFFERENCE_WORD_CHECK_V1","exact_exhaustive":exhaustive(),
            "random":random_checks(),"huge":huge(),"timing":compare_runtime(),
            "result":"R132_ONEINTEGER_FEASIBILITY_PASS","arithmetic":"all comparisons exact Fraction; in-process benchmark medians of 3"}
    print(json.dumps(result,ensure_ascii=False,indent=2))
