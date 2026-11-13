#!/usr/bin/env python3
"""Exact Fraction verification of the conditional BU policy-uniform quotient theorem.
Author-side check, not independent admission or proof of the all-kernel claim.
"""
from fractions import Fraction as F
from itertools import product

Q_NODES={"AU": F(1,6), "AV": F(1,3), "BU": F(1,4), "BV": F(1,4)}
RATIO={"AU":(F(9,10), F(11,10)), "AV":(F(1,4),F(1,4)),
       "BU":(F(1,5),F(9,5)), "BV":(F(2),F(2))}
SOURCE={law:{(name,j,k):Q_NODES[name]/4*(RATIO[name][j] if law=="P" else 1)
       for name in Q_NODES for j in (0,1) for k in (0,1)} for law in ("P","Q")}
assert all(len(a)==16 and sum(a.values())==1 and all(w>0 for w in a.values()) for a in SOURCE.values())

def tv(a,b):
    return sum(abs(a.get(x,0)-b.get(x,0)) for x in set(a)|set(b))/2

def add(dic,key,value): dic[key]=dic.get(key,F(0))+value

def raw(law,e):
    """Conditional BU distribution of (J,K,Z) for P or Q."""
    answer={}
    for j,k,z in product((0,1),repeat=3):
        p=SOURCE[law][("BU",j,k)]/Q_NODES["BU"]
        answer[j,k,z]=p*((1-e) if z==j else e)
    return answer

def encode(rawlaw,code):
    result={}
    for (j,k,z),p in rawlaw.items():
        add(result,(z,code[(j,k,z)]),p)
    return result

def decoded_raw_by_j(law,e):
    """Exact common reverse kernel with S=J, sampled K fair."""
    enc=encode(raw(law,e),{(j,k,z):j for j,k,z in product((0,1),repeat=3)})
    result={}
    for (z,s),p in enc.items():
        for k in (0,1):add(result,(s,k,z),p/2)
    return result

def transcript(law,e,sim=False,s23=False):
    """Two-stage causal, source-law-independent S2/S23 policy;
    S2 terminal decision uses actual K; simulation draws K once.
    """
    base=decoded_raw_by_j(law,e) if sim else raw(law,e)
    result={}
    for (j,k,z),p in base.items():
        continue_probability=(F(1,3) if j==0 else F(2,3))
        add(result,(z,'T3','Q'),p*(1-continue_probability))
        terminal_P=(F(1,4) if (j if s23 else k)==0 else F(3,4))
        add(result,(z,'T4',k,'P'),p*continue_probability*terminal_P)
        add(result,(z,'T4',k,'Q'),p*continue_probability*(1-terminal_P))
    return result

# 2^8 assignments from 4 (J,K) states for each Z (256 binary stochastic-free encoders).
# The universal theorem covers *all* stochastic encoders; this finite enumeration only checks deterministic binary cases.
for e in [F(0), F(1,4), F(1,3), F(1,2)]:
    rp,rq=raw('P',e),raw('Q',e)
    assert sum(rp.values())==sum(rq.values())==1
    full=tv(rp,rq)
    assert full==F(2,5)
    zP={z:sum(w for (j,k,z2),w in rp.items() if z2==z) for z in (0,1)}
    zQ={z:sum(w for (j,k,z2),w in rq.items() if z2==z) for z in (0,1)}
    assert tv(zP,zQ)==F(2,5)*(1-2*e)
    assert decoded_raw_by_j('P',e)==rp and decoded_raw_by_j('Q',e)==rq
    for law in ('P','Q'):
        for s23 in (False,True):
            assert transcript(law,e,False,s23)==transcript(law,e,True,s23)
    equality_count=0
    const_count=0
    for bits in product((0,1),repeat=8):
        code={x:bits[i] for i,x in enumerate(product((0,1),repeat=3))}
        cp,cq=encode(rp,code),encode(rq,code)
        equal=tv(cp,cq)==full
        # Necessary/sufficient condition for information preserving coding.
        separated=all(not ({code[(0,k,z)] for k in (0,1)} &
                           {code[(1,k,z)] for k in (0,1)}) for z in (0,1))
        if e: assert equal==separated
        else: assert equal
        equality_count+=equal
        const_count+=separated
    assert equality_count==(256 if e==0 else 4)
    assert const_count==4
    print(f'epsilon={e}: raw_TV={full}; Z_TV={tv(zP,zQ)}; '
          f'Z_loss={full-tv(zP,zQ)}; binary_exact_encoders={equality_count}/256; '
          'S=J exact P/Q and causal S2/S23 transcripts: PASS')

# Exact shortest pathwise-loss witness for S=J: fair K never predicted better than 1/2.
for u,v in [(F(0),F(1)),(F(1,4),F(3,4)),(F(1),F(1))]:
    t4p=(u+9*v)/40; t4q=(u+v)/8
    worst=max(t4p,t4q)/2
    assert t4p==sum(SOURCE['P'][('BU',j,k)]*(u if j==0 else v)
                   for j in (0,1) for k in (0,1))
    assert t4q==sum(SOURCE['Q'][('BU',j,k)]*(u if j==0 else v)
                   for j in (0,1) for k in (0,1))
    print(f'continue u={u}, v={v}: P(T4,BU)={t4p}; Q(T4,BU)={t4q}; '
          f'sharp_minimax_same_realized_K_error={worst}')
print('PASS_BRC_N4_POLICY_UNIFORM_CONDITIONAL_SUFFICIENCY_20261030')
