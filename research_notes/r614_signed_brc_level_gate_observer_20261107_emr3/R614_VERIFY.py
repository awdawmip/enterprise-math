#!/usr/bin/env python3
"""R614: exact signed K/J->B->D level-gate mixed response verifier.
R462 frozen science @18783e01e3646c72b7aab3b16d3f565e83e6446f, theta=0.
All computations use Python arbitrary-precision integers. These gates label
recurrence levels, NOT P000 physical heartbeat times.
"""
from math import comb
from itertools import product
from pathlib import Path
from hashlib import sha256
import json

N=8
def C(n,k): return comb(n,k) if 0<=k<=n else 0

def add(p,q):
    z=[0]*max(len(p),len(q))
    for j,v in enumerate(p): z[j]+=v
    for j,v in enumerate(q): z[j]+=v
    return tuple(z)

def mul(p,q):
    z=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        if a:
            for j,b in enumerate(q):
                if b: z[i+j]+=a*b
    return tuple(z)

def coeff(p,j): return p[j] if 0<=j<len(p) else 0
def scale(p,c): return tuple(c*x for x in p)
def mono(n,c,shift):
    return tuple([0]*shift+[c*C(n,j) for j in range(n+1)]) if n>=0 else (0,)

def K(i):
    ds=(-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
    z=(0,)
    for j,a in enumerate(ds,1):
        if a: z=add(z,mono(i+1-j,-a,i-1))
    return z

def J(s):
    z=(0,)
    for a,n in ((-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2)):
        if a: z=add(z,mono(n,a,s))
    return z

KERNELS={i:K(i) for i in range(1,13)}

def gated_state(n,G=None,forced=True):
    G={} if G is None else G
    B=[(1,1)]
    for s in range(1,n+1):
        b=J(s) if forced else (0,)
        for i in range(1,min(s,12)+1):
            if G.get((s,i),1): b=add(b,mul(KERNELS[i],B[s-i]))
        B.append(b)
    return B

def D(B,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*coeff(B[q+w],q)
               for w in range(k+1))

def histories(s,G):
    if s==0: return [((),"B0",(1,1))]
    out=[((),f"J{s}",J(s))]
    for i in range(1,min(s,12)+1):
        if G.get((s,i),1):
            for e,terminal,p in histories(s-i,G):
                out.append((((s,i),)+e,terminal,mul(KERNELS[i],p)))
    return out

def delta_poly(s,E):
    a=(0,)
    for bits in product((0,1),repeat=len(E)):
        G=dict(zip(E,bits))
        z=gated_state(s,G)[s]
        a=add(a,scale(z,(-1)**(len(E)-sum(bits))))
    return a

def delta_D(q,k,E):
    a=0
    for bits in product((0,1),repeat=len(E)):
        G=dict(zip(E,bits))
        a+=(-1)**(len(E)-sum(bits))*D(gated_state(q+k,G),q,k)
    return a

def same_poly(p,q):
    return all(coeff(p,j)==coeff(q,j) for j in range(max(len(p),len(q))))

def main():
    assert KERNELS[1]==(2,3)
    assert KERNELS[2]==(0,-1,4,4)
    assert coeff(KERNELS[3],2)==-8
    B=gated_state(N)
    assert [2**q*coeff(B[q],q) for q in range(3)]==[1,6,32]
    assert D(B,2,1)==60
    edges=[(s,i) for s in range(1,4) for i in range(1,s+1)]
    assert len(edges)==6
    assignments=0
    for bits in product((0,1),repeat=len(edges)):
        G=dict(zip(edges,bits))
        current=gated_state(3,G)
        for s in range(4):
            sum_of_histories=(0,)
            for _,_,p in histories(s,G):
                sum_of_histories=add(sum_of_histories,p)
            assert same_poly(sum_of_histories,current[s])
        assignments+=1
    assert assignments==64
    R=[(1,)]
    for n in range(1,N+1):
        z=(0,)
        for i in range(1,min(n,12)+1):
            z=add(z,mul(KERNELS[i],R[n-i]))
        R.append(z)
    first_response_cases=0
    for s in range(1,6):
        for i in range(1,s+1):
            drop=mul(KERNELS[i],B[s-i])
            for n in range(s,N+1):
                switched=gated_state(n,{(s,i):0})
                actual=add(B[n],scale(switched[n],-1))
                predicted=mul(R[n-s],drop)
                assert same_poly(actual,predicted),(s,i,n)
                first_response_cases+=1
    E12=((3,1),(2,2))
    E21=((3,2),(1,1))
    Ex=((3,1),(3,2))
    P=mul(mul(KERNELS[1],KERNELS[2]),(1,1))
    assert P==(0,-2,3,25,32,12)
    assert same_poly(delta_poly(3,E12),P)
    assert same_poly(delta_poly(3,E21),P)
    assert delta_D(2,1,E12)==6
    assert delta_D(2,1,E21)==6
    assert all(x==0 for x in delta_poly(3,Ex))
    assert delta_D(2,1,Ex)==0
    history_terms=0
    for s in range(8):
        seen=set()
        for edges_of_history,terminal,_ in histories(s,{}):
            key=(edges_of_history,terminal)
            assert key not in seen
            seen.add(key)
            assert len(set(edges_of_history))==len(edges_of_history)
            assert all(edges_of_history[j][0]>edges_of_history[j+1][0]
                       for j in range(len(edges_of_history)-1))
            history_terms+=1
    rec={
      "schema":"R614_SIGNED_BRC_LEVEL_GATE_OBSERVER_V1",
      "scientific_pin":"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f",
      "source":"research_notes/r388_signed_k3_corank16_20261029_emr3/r388_exact.py",
      "arithmetic_semantics":"Python arbitrary precision integers",
      "domain":"exact signed twelve K/J->B->D at theta=0, counterfactual level-indexed Boolean gates",
      "K1":list(KERNELS[1]),"K2":list(KERNELS[2]),
      "P":list(P),"baseline_D21":D(B,2,1),
      "E12":[list(x) for x in E12],"E21":[list(x) for x in E21],
      "mixed_D21_E12":delta_D(2,1,E12),
      "mixed_D21_E21":delta_D(2,1,E21),
      "mixed_D21_mutually_exclusive":delta_D(2,1,Ex),
      "mask_assignments_checked":assignments,
      "first_response_cases_checked":first_response_cases,
      "history_terms_checked":history_terms,
      "formal_gate_scope":"recurrence-level masks of native signed auxiliary K/J branches; no asserted physical X6 intervention",
      "terminal_marker":"R614_CAUSAL_BRANCH_PROBE_ALL_EXACT_PASS"
    }
    content=json.dumps(rec,sort_keys=True,ensure_ascii=False,indent=2)+"\n"
    Path(__file__).with_name("R614_EVIDENCE.json").write_text(content,encoding="utf-8")
    print(rec["terminal_marker"])
    print("mask_assignments",assignments,"first_response_triplets",first_response_cases,"history_terms",history_terms)
    print("evidence_sha256",sha256(content.encode()).hexdigest())
    print("baseline D21",rec["baseline_D21"],"mixed",rec["mixed_D21_E12"],rec["mixed_D21_E21"])

if __name__=="__main__": main()
