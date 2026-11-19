#!/usr/bin/env python3
"""R23 exact Boolean-BRC joint grant threshold verifier, Python standard library."""
import itertools, json, math
from functools import lru_cache

def successors(theta,k,q,state):
    m=len(theta)
    steps=state[:m]
    r,done=state[m],state[m+1]
    for i in range(m):
        if steps[i]<k:
            nxt=list(state)
            nxt[i]+=1
            if nxt[i]==k:
                nxt[m]=min(q,r+theta[i])
            yield i,tuple(nxt)
    if not done and r>=q:
        nxt=list(state)
        nxt[m]-=q
        nxt[m+1]=1
        yield m,tuple(nxt)

def accepts(theta,k,q,word):
    s=(0,)*len(theta)+(0,0)
    for sym in word:
        opt=dict(successors(theta,k,q,s))
        if sym not in opt:
            return False
        s=opt[sym]
    return True

def verify():
    counts={'controller_configurations':0,'initial_signature_observations':0,
            'pair_witness_checks':0,'small_domain_full_word_checks':0,
            'transition_signature_nodes':0}
    cases=[]
    for m in range(1,5):
        for k in range(1,4):
            for q in range(1,m+1):
                bits=list(itertools.product((0,1),repeat=m))
                start=(0,)*m+(0,0)
                horizon=q*k+1
                num=[0]
                @lru_cache(maxsize=None)
                def sig(theta,state,h):
                    if h==0:
                        return ()
                    num[0]+=1
                    return tuple((sym,sig(theta,nxt,h-1))
                        for sym,nxt in successors(theta,k,q,state))
                def family_class(theta):
                    return sum((1<<i) for i,b in enumerate(theta) if b) if sum(theta)>=q else -1
                for h in range(horizon+1):
                    signatures=[sig(theta,start,h) for theta in bits]
                    counts['initial_signature_observations']+=len(bits)
                    expected=1 if h<horizon else 1+sum(math.comb(m,j) for j in range(q,m+1))
                    assert len(set(signatures))==expected
                    if h==horizon:
                        for i,t in enumerate(bits):
                            for j,u in enumerate(bits):
                                assert (signatures[i]==signatures[j]) == (family_class(t)==family_class(u))
                for a,t in enumerate(bits):
                    for u in bits[a+1:]:
                        if family_class(t)==family_class(u):
                            continue
                        S={i for i,x in enumerate(t) if x}
                        T={i for i,x in enumerate(u) if x}
                        rich=S if len(S)>=q and (len(T)<q or not S.issubset(T)) else T
                        other=T if rich is S else S
                        distinct=next(iter(sorted(rich-other)))
                        indices=sorted([distinct]+sorted(rich-{distinct})[:q-1])
                        witness=tuple(i for idx in indices for i in (idx,)*k)+(m,)
                        assert len(witness)==horizon
                        assert accepts(t,k,q,witness)!=accepts(u,k,q,witness)
                        counts['pair_witness_checks']+=1
                if m<=2 and k<=2:
                    for theta in bits:
                        for h in range(horizon+1):
                            frontier={(start,())}
                            words={()}
                            for _ in range(h):
                                nxt=set()
                                for state,word in frontier:
                                    for label,new in successors(theta,k,q,state):
                                        nxt.add((new,word+(label,)))
                                        words.add(word+(label,))
                                frontier=nxt
                            for length in range(h+1):
                                for word in itertools.product(range(m+1),repeat=length):
                                    assert (word in words)==accepts(theta,k,q,word)
                                    counts['small_domain_full_word_checks']+=1
                counts['controller_configurations']+=len(bits)
                counts['transition_signature_nodes']+=num[0]
                cls=1+sum(math.comb(m,j) for j in range(q,m+1))
                cases.append({'lanes':m,'steps_per_grant':k,'required_credits':q,
                    'hidden_assignments':2**m,'first_difference_horizon':horizon,
                    'classes_before_horizon':1,'classes_at_horizon':cls,
                    'minimal_bits_at_horizon':(cls-1).bit_length()})
    return {'schema':'X6_SHARED_THRESHOLD_TRIADIC_GRANT_R23_EXACT_V1',
        'status':'PASS','observer':'Boolean successful source/signed-Port words; frame and shared credit internal',
        'counts':counts,'cases':cases}

if __name__=='__main__':
    print(json.dumps(verify(),sort_keys=True,indent=2))
