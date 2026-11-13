#!/usr/bin/env python3
"""R686 exact V17/J(6,3) slot holonomy + typed positive-rational BRC."""
from collections import Counter, deque, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
import json

TRIADS = tuple(combinations(range(6),3))
BASE = (0,1,2)
NEIGH = {S:tuple(T for T in TRIADS if len(set(S)&set(T))==2) for S in TRIADS}
FRAMES = tuple(permutations(BASE))

def step(frame,source,target):
    assert set(frame)==set(source) and target in NEIGH[source]
    outgoing = next(iter(set(source)-set(target)))
    incoming = next(iter(set(target)-set(source)))
    return tuple(incoming if v==outgoing else v for v in frame)

def along(path,initial=BASE):
    f=initial
    for a,b in zip(path,path[1:]): f=step(f,a,b)
    return f

def local_perm(source,target):
    old=tuple(sorted(source));new=tuple(sorted(target))
    return tuple(new.index(x) for x in step(old,source,target))

def compose(left,right): return tuple(left[right[i]] for i in range(3))

def path_perm(path):
    p=BASE
    for a,b in zip(path,path[1:]):p=compose(local_perm(a,b),p)
    return p

def edge_hist(path):
    return {str(a)+":"+str(b):n for (a,b),n in sorted(Counter(zip(path,path[1:])).items())}

def join(*loops):
    p=list(loops[0])
    for loop in loops[1:]:
        assert p[-1]==loop[0]
        p.extend(loop[1:])
    return tuple(p)

def brc_step(mu,S,T):
    r=local_perm(S,T)
    out=defaultdict(Fraction)
    for g,m in mu.items(): out[compose(r,g)]+=m
    return dict(out)

def brc_along(path,mu):
    for S,T in zip(path,path[1:]):mu=brc_step(mu,S,T)
    return mu

def bfs():
    queue=deque([(BASE,BASE)])
    found={(BASE,BASE):(0,(BASE,))}
    while queue:
        S,F=queue.popleft()
        for T in NEIGH[S]:
            new=(T,step(F,S,T))
            if new not in found:
                d,path=found[(S,F)]
                found[new]=(d+1,path+(T,))
                queue.append(new)
    assert len(found)==120
    return found

def main():
    assert len(TRIADS)==20 and all(len(NEIGH[S])==9 for S in TRIADS)
    checks=0
    for S in TRIADS:
        for T in NEIGH[S]:
            assert {step(F,S,T) for F in permutations(S)}==set(permutations(T))
            for F in permutations(S):
                assert step(step(F,S,T),T,S)==F
                p=tuple(tuple(sorted(S)).index(x) for x in F)
                q=compose(local_perm(S,T),p)
                assert tuple(sorted(T)[i] for i in q)==step(F,S,T)
                checks+=1
    assert checks==1080
    L=(BASE,(0,1,3),(0,2,3),BASE)
    K=(BASE,(0,1,3),(1,2,3),BASE)
    assert along(L)==(0,2,1) and along(K)==(2,1,0)
    LK=join(L,K);KL=join(K,L)
    assert len(LK)==len(KL)==7
    assert edge_hist(LK)==edge_hist(KL)
    assert along(LK)==path_perm(LK)==(2,0,1)
    assert along(KL)==path_perm(KL)==(1,2,0)
    found=bfs()
    lens={''.join(map(str,F)):found[(BASE,F)][0] for F in FRAMES}
    assert lens=={'012':0,'021':3,'102':3,'120':4,'201':4,'210':3}
    tris=Counter(); images=set()
    for T in NEIGH[BASE]:
        for U in NEIGH[T]:
            if BASE not in NEIGH[U]:continue
            F=along((BASE,T,U,BASE));images.add(F)
            tris['identity' if F==BASE else 'transposition']+=1
            assert F in (BASE,(0,2,1),(1,0,2),(2,1,0))
    assert tris=={'identity':18,'transposition':18}
    assert images=={BASE,(0,2,1),(1,0,2),(2,1,0)}
    mu=defaultdict(Fraction)
    for path in (LK,KL):
        for g,m in brc_along(path,{BASE:Fraction(1,2)}).items():mu[g]+=m
    assert dict(mu)=={(2,0,1):Fraction(1,2),(1,2,0):Fraction(1,2)}
    assert sum(mu.values(),Fraction())==1
    even=lambda p:sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2==0
    assert all(even(g) for g in mu) and even(BASE)
    for T in NEIGH[BASE]:
        next_mu=brc_step(mu,BASE,T)
        assert len(next_mu)==2
        assert sorted(next_mu.values())==[Fraction(1,2),Fraction(1,2)]
    certificate={
      'schema':'R686_BRC_S3_COCYCLE_CERTIFICATE_V1',
      'date':'2026-11-10',
      'task':'RS-X6-NATIVE-TIME-DYNAMICS',
      'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
      'predecessor':'R685@8505a08128e307c5ffbba1dd0522f66f515a401e',
      'scope':'abstract V17 active triad transitions J(6,3), exact rational BRC, NOT native physical X6 time',
      'coverage':{'triads':20,'neighbors':9,'frames_each':6,'directed_frame_edge_checks':checks,'reachable_states':len(found),'triangles':dict(tris),'shortest_return_lengths':lens},
      'witnesses':{'L':[''.join(map(str,x)) for x in L],'K':[''.join(map(str,x)) for x in K],'L_frame':'021','K_frame':'210','LK_frame':'201','KL_frame':'120','same_directed_edge_histogram':edge_hist(LK),'event_steps':6,'exact_BRC_frame_mass':{'201':'1/2','120':'1/2'},'both_even_permutations':True},
      'theorems':{'cocycle':'p_next=r(S,T)p','holonomy':'full S3','first_nonidentity_return':3,'first_three_cycle_return':4,'abelian_quotient':'commutator subgroup A3 erased by homomorphic abelian readout'},
      'not_claimed':['V29 PASS = arbitrary V17 edge','native X6 Link/Cell','V39 j','physical duration','independent Driver approval']
    }
    Path(__file__).with_name('R686_EVIDENCE.json').write_text(json.dumps(certificate,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    print('R686_TYPED_BRC_S3_HOLONOMY_EXACT_PASS')
    print('triangles:',dict(tris),'min returns:',lens)
    print('same edge histogram LK/KL; outputs:',along(LK),along(KL))

if __name__=='__main__':main()
