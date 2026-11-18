#!/usr/bin/env python3
"""EC49BE endpoint saturation: exact rational evidence, standard library only.
The all-real upper bound and strictness for eta<1/2 are proved analytically
in PROOF_EC49BE.md; finite checks here corroborate the explicit witnesses.
"""
from fractions import Fraction as Q
from itertools import combinations, product
import json

COST = (1, 1, 2, 2, 0)
C1 = Q(43,48)
C2 = Q(13,16)
LAMBDA = Q(27,172)
HSTAR = Q(351,2752)


def first_strategy(t):
    return ((Q(11,16)-t/2, Q(0), t/4, Q(0), Q(5,16)+t/4),
            (Q(0), Q(1), Q(0), Q(0), Q(0)),
            (Q(1), Q(0), Q(0), Q(0), Q(0)))


def observation(w,u,eta):
    return Q(1,2)+(2*u-1)*(1-w)*eta


def fibers(x,eta):
    out=[]
    for c in range(4):
        for u in range(2):
            q=tuple(x[z][c]*observation(z,u,eta)/3 for z in range(3))
            T=sum(q)
            V=sum(max(Q(0),43*z-16*T) for z in q)/172
            out.append((c,u,q,T,V))
    return out


def purchase(t):
    return {(c,u): (Q(7)-4*t)/(11-8*t) if (c,u)==(0,1) else Q(1)
            for c in range(4) for u in range(2)}


def witness_check(t):
    x=first_strategy(t)
    assert all(sum(row)==1 and all(v>=0 for v in row) for row in x)
    assert sum(COST[c]*x[w][c] for w in range(3) for c in range(5))/3==C1
    p=purchase(t)
    assert all(0<=v<=1 for v in p.values())
    fs=fibers(x,Q(1,2))
    assert sum(p[(c,u)]*T for c,u,q,T,V in fs)==C2
    assert all(sum(v>0 for v in q)<=1 for c,u,q,T,V in fs)
    assert all(V==LAMBDA*T for c,u,q,T,V in fs)
    H=sum(p[(c,u)]*V for c,u,q,T,V in fs)
    assert H==HSTAR
    return {"t":str(t),"partial_purchase":str(p[(0,1)]),"paid_mass":str(C2),"H":str(H)}


def vertex_enumeration():
    vertices=set()
    for r in range(3):
        rem=tuple(w for w in range(3) if w!=r)
        for a,b in combinations(range(5),2):
            for k,l in product(range(5),repeat=2):
                acts=[0]*3
                acts[rem[0]]=k;acts[rem[1]]=l;acts[r]=a
                A=tuple(tuple(Q(int(c==acts[w])) for c in range(5)) for w in range(3))
                acts[r]=b
                B=tuple(tuple(Q(int(c==acts[w])) for c in range(5)) for w in range(3))
                ca=sum(COST[c]*A[w][c] for w in range(3) for c in range(5))
                cb=sum(COST[c]*B[w][c] for w in range(3) for c in range(5))
                target=3*C1
                if (ca-target)*(cb-target)>=0:
                    continue
                s=(target-ca)/(cb-ca)
                v=tuple(tuple((1-s)*A[w][c]+s*B[w][c] for c in range(5)) for w in range(3))
                vertices.add(v)
    return vertices


def tight_ambiguity_sample():
    q=(Q(1,2), Q(1,2), Q(0))
    T=sum(q)
    V=sum(max(Q(0),43*z-16*T) for z in q)/172
    ambiguity=T-max(q)
    assert (LAMBDA*T-V)/ambiguity==Q(32,172)
    return {"q": [str(z) for z in q],"V":str(V),"ambiguity":str(ambiguity),
            "deficit_coefficient":str(Q(32,172))}


def main():
    witnesses=[witness_check(t) for t in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))]
    vs=vertex_enumeration()
    assert len(vs)==168
    for x in vs:
        fs=fibers(x,Q(1,2))
        assert sum(max(Q(0),V-LAMBDA*T) for c,u,q,T,V in fs)==0
    assert LAMBDA*C2==HSTAR
    print(json.dumps({"status":"PASS_AUTHOR_EXACT_WITNESS_AND_VERTEX_CHECK",
        "mathematical_scope":"auxiliary positive probability BRC; eta=1/2 endpoint",
        "proof_scope":"analytic all-policy inequality and eta<1/2 strictness in PROOF_EC49BE.md",
        "tight_dual_lambda":str(LAMBDA),"exact_optimum":str(HSTAR),
        "checked_first_stage_vertices":len(vs),"sampled_witness_family":witnesses,
        "sharp_ambiguity_lemma_sample":tight_ambiguity_sample(),
        "not_claimed":"independent mathematical review, native signed/phase BRC or X6 transfer"},
        ensure_ascii=False,sort_keys=True,indent=2))


if __name__=='__main__':main()
