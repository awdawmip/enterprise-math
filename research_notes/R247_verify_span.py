#!/usr/bin/env python3
"""Exact rational future-trace span test for unit-positive deterministic BRC.

Author-only implementation: does not import enterprise_math native source.
The 16 control states are non-spatial. Formal affine effects differ only on
native axis 1 of the six-axis maps; axes 2--6 are unchanged identity.
"""
from collections import deque
from fractions import Fraction as F
import json

N = 16
ALPHABET = ("G3", "G2")

def g3(s):
    x,a,c,r = ((s >> k)&1 for k in (3,2,1,0))
    return 8*(x ^ a ^ c)+4*a+2*c+r

def g2(s):
    x,a,c,r = ((s >> k)&1 for k in (3,2,1,0))
    return 8*(x ^ r)+4*a+2*c+r

TRANS={"G3":tuple(map(g3,range(N))),"G2":tuple(map(g2,range(N)))}

def pi(s):
    return ((s>>3)&1, ((s>>2)^(s>>1))&1, s&1)

ID=(F(1),F(0)); NUL=(F(0),F(0)); SHIFT=(F(1),F(1)); REFLECT=(F(-1),F(0))

def make_effects(masked):
    effects={g:[ID]*N for g in ALPHABET}
    for g in ALPHABET:
        for s in (2,4): effects[g][s]=NUL
    effects["G3"][10]=ID
    effects["G3"][12]=REFLECT
    effects["G2"][10]=ID if masked else SHIFT
    effects["G2"][12]=ID if masked else SHIFT
    return effects

def reachable_pairs(trans,a,b):
    root=(a,b); queue=deque([root]); seen={root:()}
    while queue:
        p=queue.popleft()
        for g in ALPHABET:
            t=(trans[g][p[0]],trans[g][p[1]])
            if t not in seen:
                seen[t]=seen[p]+(g,)
                queue.append(t)
    return seen

def affine_apply(effect, prior):
    m,b=effect; a,c=prior
    return m*a,m*c+b

def simulate(word,effects,start):
    state=start; value=ID
    for g in word:
        value=affine_apply(effects[g][state],value)
        state=TRANS[g][state]
    return state,value

def vec_step(v,pairs,pair_index,trans,effects,g):
    result=[F(0)]*len(v)
    for idx,(s,t) in enumerate(pairs):
        a,b,c,d,k=v[5*idx:5*idx+5]
        if not any((a,b,c,d,k)):continue
        m,u=effects[g][s]; n,w=effects[g][t]
        j=5*pair_index[(trans[g][s],trans[g][t])]
        result[j]+=m*a
        result[j+1]+=m*b+u*k
        result[j+2]+=n*c
        result[j+3]+=n*d+w*k
        result[j+4]+=k
    return tuple(result)

def observed_difference(v,pairs):
    a=b=c=d=F(0)
    for i in range(len(pairs)):
        x,y,z,w,_=v[5*i:5*i+5]
        a+=x; b+=y; c+=z; d+=w
    return a-c,b-d

def insert_basis(vec,basis):
    """Exact rank: increasing pivot order prevents reintroducing earlier pivots."""
    v=list(vec)
    for pivot in sorted(basis):
        row=basis[pivot]
        if v[pivot]:
            coeff=v[pivot]
            for j in range(pivot,len(v)): v[j]-=coeff*row[j]
    pivot=next((j for j,x in enumerate(v) if x),None)
    if pivot is None:return False
    coeff=v[pivot]
    basis[pivot]=tuple(x/coeff for x in v)
    return True

def trace_equivalence_exact(effects,sa=2,sb=4):
    reach=reachable_pairs(TRANS,sa,sb)
    for pair,word in reach.items():
        if pi(pair[0])!=pi(pair[1]):
            return {"equivalent":False,"witness":word,"reason":"control_readout"}
    pairs=tuple(reach); indices={p:i for i,p in enumerate(pairs)}
    dimension=5*len(pairs)
    v=[F(0)]*dimension
    v[0]=v[2]=v[4]=F(1)
    v=tuple(v)
    basis={}
    assert insert_basis(v,basis)
    pending=deque([(v,())])
    max_depth=0
    while pending:
        x,word=pending.popleft()
        max_depth=max(max_depth,len(word))
        assert observed_difference(x,pairs)==(0,0)
        for g in ALPHABET:
            y=vec_step(x,pairs,indices,TRANS,effects,g)
            witness=word+(g,)
            if observed_difference(y,pairs)!=(0,0):
                assert simulate(witness,effects,sa)[1]!=simulate(witness,effects,sb)[1]
                return {"equivalent":False,"witness":witness,"dimension":dimension,
                        "rank_before_witness":len(basis),"reachable_pairs":pairs}
            if insert_basis(y,basis):pending.append((y,witness))
    return {"equivalent":True,"dimension":dimension,"rank":len(basis),
            "max_basis_word_length":max_depth,"reachable_pairs":pairs,
            "proof":"successor-invariant rational span annihilated by exact affine-difference observer"}

def brute_min(effects,limit):
    queue=deque([()])
    while queue:
        word=queue.popleft()
        a,ea=simulate(word,effects,2)
        b,eb=simulate(word,effects,4)
        if pi(a)!=pi(b) or ea!=eb:return word
        if len(word)<limit:
            queue.extend(word+(g,) for g in ALPHABET)
    return None

def main():
    assert len({pi(s) for s in range(N)})==8
    assert all(pi(g3(s))==pi(g3(s^6)) and pi(g2(s))==pi(g2(s^6)) for s in range(N))
    delayed=trace_equivalence_exact(make_effects(False))
    masked=trace_equivalence_exact(make_effects(True))
    assert delayed["witness"]==("G3","G2","G3")
    assert masked["equivalent"] and masked["rank"]==3
    assert brute_min(make_effects(False),5)==("G3","G2","G3")
    assert brute_min(make_effects(True),10) is None
    shared={g:[NUL]*N for g in ALPHABET}
    assert trace_equivalence_exact(shared)["equivalent"]
    altered={g:[ID]*N for g in ALPHABET}
    altered["G3"][4]=REFLECT
    assert trace_equivalence_exact(altered)["witness"]==("G3",)
    print(json.dumps({"status":"PASS","arithmetic":"exact Fraction",
        "source_native_import":False,"reachable_control_pairs":len(masked["reachable_pairs"]),
        "ambient_dim":masked["dimension"],"delayed_witness":delayed["witness"],
        "delayed_rank_before_witness":delayed["rank_before_witness"],
        "masked_all_future_equivalent":masked["equivalent"],
        "masked_invariant_span_rank":masked["rank"],"masked_max_basis_word_length":masked["max_basis_word_length"],
        "positive_path_mass_only":True},indent=2))

if __name__=="__main__": main()
