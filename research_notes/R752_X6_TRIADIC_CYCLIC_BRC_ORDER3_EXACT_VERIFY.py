#!/usr/bin/env python3
"""R752: exact signed-X6 unmarked cyclic triad BRC word-moment check.
Standard library only. All coefficients are integers, complete finite enumeration.
"""
from collections import defaultdict
from itertools import combinations, permutations, product
import json

D=6

def make_state(ax,sig,ori):
    p=[(int(a),int(s)) for a,s in zip(ax,sig)]
    return (p[0],p[1],p[2]) if ori==1 else (p[0],p[2],p[1])

def words(cycle):
    for shift in range(3):
        a,b,c=(cycle[(shift+t)%3] for t in range(3))
        yield [a,b,c,(a[0],-a[1]),(b[0],-b[1]),(c[0],-c[1])]

def moment2(word):
    M=defaultdict(int)
    for i in range(len(word)):
        for j in range(i+1,len(word)):
            a,sa=word[i];b,sb=word[j]
            M[(a,b)]+=sa*sb
    return M

def moment3(word):
    M=defaultdict(int)
    for i in range(len(word)):
        for j in range(i+1,len(word)):
            for k in range(j+1,len(word)):
                a,sa=word[i];b,sb=word[j];c,sc=word[k]
                M[(a,b,c)]+=sa*sb*sc
    return M

def canonical(M):
    return tuple(sorted((k,v) for k,v in M.items() if v))

def compute(cycle):
    M2=defaultdict(int);M3=defaultdict(int)
    for w in words(cycle):
        for k,v in moment2(w).items():M2[k]+=v
        for k,v in moment3(w).items():M3[k]+=v
    return M2,M3

def verify():
    C2=defaultdict(list);C23=defaultdict(list)
    states=[]; witnesses=0
    for ax in combinations(range(D),3):
        for sig in product((-1,1),repeat=3):
            for ori in (-1,1):
                c=make_state(ax,sig,ori)
                ws=list(words(c));witnesses+=len(ws)
                for w in ws:
                    assert len(w)==6 and len({a for a,_ in w})==3
                    assert all(sum(sign for aa,sign in w if aa==i)==0 for i in ax)
                    assert all(w[t]!=(w[t+1][0],-w[t+1][1]) for t in range(5))
                m2,m3=compute(c)
                i,j,k=ax
                assert m3[(i,j,i)] == -ori*sig[1]
                assert m3[(j,i,j)] == +ori*sig[0]
                assert m3[(i,k,i)] == +ori*sig[2]
                assert m2[(i,j)]-m2[(j,i)]==2*ori*sig[0]*sig[1]
                assert m2[(j,k)]-m2[(k,j)]==2*ori*sig[1]*sig[2]
                assert m2[(i,k)]-m2[(k,i)]==-2*ori*sig[0]*sig[2]
                key=(ax,sig,ori)
                C2[canonical(m2)].append(key)
                C23[(canonical(m2),canonical(m3))].append(key)
                states.append((key,c,m2,m3))
    assert len(states)==320 and witnesses==960
    assert len(C2)==160 and set(map(len,C2.values()))=={2}
    assert len(C23)==320 and set(map(len,C23.values()))=={1}
    for fiber in C2.values():
        assert fiber[0][0]==fiber[1][0] and fiber[0][2]==fiber[1][2]
        assert fiber[1][1]==tuple(-x for x in fiber[0][1])
    checked=0
    for perm in permutations(range(D)):
        for _,c,m2,m3 in states:
            gc=tuple((perm[a],s) for a,s in c)
            gm2,gm3=compute(gc)
            assert canonical(gm2)==canonical({(perm[a],perm[b]):v for (a,b),v in m2.items()})
            assert canonical(gm3)==canonical({(perm[a],perm[b],perm[d]):v for (a,b,d),v in m3.items()})
            checked+=1
    assert checked==230400
    report={'status':'R752_X6_TRIADIC_CYCLIC_BRC_ORDER3_EXACT_PASS',
      'axis_count':6,'axis_subsets':20,'source_states':len(states),
      'six_step_closed_branch_words':witnesses,'degree2_fiber_count':len(C2),
      'degree2_fiber_size':2,'degree3_combined_observer_classes':len(C23),
      'degree3_combined_observer_fiber_size':1,
      'signed_axis_permutations':720,'covariance_checks':checked,
      'formula':'M_iji(cyclic W)=-orientation*sign_j for i<j<k',
      'implementation':'integer subsequence moments of 6-letter signed X6 paths',
      'limits':'syntactic Port-incidence C1 candidate states; no native V29/V39 event legality or independent Driver acceptance'}
    print(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2))
    return report

if __name__=='__main__':verify()
