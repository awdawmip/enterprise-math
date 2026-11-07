"""Stage470-B: exact positive BRC transfer for Stage469 (h=0).
Native X6 directions retained for the observer; original +E1/+E2/+E3.
Computes every class mass and lexicographic rank without original-history enumeration.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product, combinations_with_replacement
from math import comb
import json

A,B,C=0,2,4
ABC=(A,B,C)
DIR=tuple((i,s) for i in range(6) for s in (1,-1))

def observer(p,q):
    def one(w):
        disp=[0]*6; edges=[0]*144
        for t in w:
            i,s=DIR[t]; disp[i]+=s
        for x,y in zip(w,w[1:]):edges[12*x+y]+=1
        return (len(w),tuple(disp),tuple(edges))
    return (one(p),one(q),sum(x==y for x,y in zip(p,q)))

def letter_edges(o):
    edges=o[2]
    return tuple(edges[12*x+y] for x in ABC for y in ABC)

def count_classes(phi):
    """One memoized joint transfer; counts P,Q paths, not a Cartesian list of paths.
    Only h=0, POP_P<=1/APPEND_P<=1, APPEND_Q<=1 and initial ternary.
    Returns exact Stage469 repair key (Q_n,P_{m-1},Q_m,Q_{m+1}) -> mass.
    """
    pobs,qobs,K=phi
    m,n=pobs[0],qobs[0]
    assert 2<=m<n
    assert K>=1
    ep,eq=letter_edges(pobs),letter_edges(qobs)
    assert sum(ep)==m-1 and sum(eq)==n-1
    assert sum(pobs[2])==m-1 and sum(qobs[2])==n-1
    # First step A is fixed, so edges determine all letter multiplicities,
    # hence the signed six-axis displacement; verify the full input observer.
    for ob,edges in ((pobs,ep),(qobs,eq)):
        incoming=[sum(edges[3*a+b] for a in range(3)) for b in range(3)]
        cnt=[incoming[a]+(a==0) for a in range(3)]
        expected=tuple(cnt)+(0,0,0)
        assert tuple(ob[1])==expected
    inds={t:i for i,t in enumerate(ABC)}
    empty=(-1,-1,-1)
    visited=[0]
    @lru_cache(None)
    def dp(i,lp,lq,prem,qrem,need):
        # i emitted positions (index i is last); 1<=i<=n
        visited[0]+=1
        if i==n:
            return {empty:1} if need==0 and not any(prem) and not any(qrem) else {}
        j=i+1
        out=defaultdict(int)
        qopts=[z for z in ABC if qrem[3*inds[lq]+inds[z]]]
        popts=([z for z in ABC if prem[3*inds[lp]+inds[z]]] if j<=m else [None])
        for q in qopts:
            iq=3*inds[lq]+inds[q]
            qr=list(qrem);qr[iq]-=1; qr=tuple(qr)
            for p in popts:
                pr=prem
                if p is not None:
                    ip=3*inds[lp]+inds[p]
                    z=list(prem);z[ip]-=1;pr=tuple(z)
                nn=need-int(p==q) if p is not None else need
                if nn<0:continue
                for suffix,mass in dp(j,p if p is not None else lp,q,pr,qr,nn).items():
                    ptag,qtag,ntag=suffix
                    if j==m-1:ptag=p
                    if j==m:qtag=q
                    if j==m+1:ntag=q
                    # For m=2 the first (fixed) position P_{m-1}=A.
                    out[(ptag,qtag,ntag)]+=mass
        return dict(out)
    masses=dp(1,A,A,ep,eq,K-1)
    qlast_candidates=[]
    for w in ABC:
        incoming=sum(eq[3*a+inds[w]] for a in range(3))
        outgoing=sum(eq[3*inds[w]+b] for b in range(3))
        if incoming-outgoing==1-(w==A):
            qlast_candidates.append(w)
    # Rather than infer terminal by a fragile formula: directed imbalance
    # out-in = [start=A]-[end].
    qlast_candidates=[w for w in ABC if all(sum(eq[3*inds[z]+b] for b in range(3))-sum(eq[3*a+inds[z]] for a in range(3))==int(z==A)-int(z==w) for z in ABC)]
    assert len(qlast_candidates)==1
    qlast=qlast_candidates[0]
    fixed={}
    for (ptag,qtag,ntag),mass in masses.items():
        if m==2:ptag=A
        assert ptag in ABC and qtag in ABC and ntag in ABC
        fixed[(qlast,ptag,qtag,ntag)]=mass
    return fixed,dict(states=dp.cache_info().currsize,transitions=visited[0])

def key(p,q):return (q[-1],p[-2],q[len(p)-1],q[len(p)])

def exhaustive_tests():
    counters=Counter()
    for m,n in ((2,3),(3,5),(4,6)):
        fibers=defaultdict(Counter)
        for pp in product(ABC,repeat=m-1):
            p=(A,)+pp
            for qq in product(ABC,repeat=n-1):
                q=(A,)+qq
                fibers[observer(p,q)][key(p,q)]+=1
        for phi,actual in fibers.items():
            predicted,stats=count_classes(phi)
            assert predicted==dict(actual),(m,n,phi,predicted,actual)
            ks=sorted(predicted)
            for rank,k in enumerate(ks):
                assert ks[rank]==k and ks.index(k)==rank
                assert predicted[k]>0
            counters['classes']+=len(ks)
            counters['mass']+=sum(predicted.values())
            counters['states']+=stats['states']
        counters['fibers']+=len(fibers)
        counters['configs']+=1
    return dict(counters)

def star_phi(k,b,loops,m, prefix_k=None):
    # A (X A)^k A^loops, first b excursions B, remaining C.
    q=[A]
    for ix in range(k):q.extend((B if ix<b else C,A))
    q.extend([A]*loops)
    p=[A]*m
    assert m+1<len(q)
    phi=observer(tuple(p),tuple(q))
    if prefix_k is not None:
        assert phi[2]==prefix_k
    return phi

def independent_star(k,b,loops,m,K):
    """Independent combinatorial counting over AA-loop allocations, never over B/C words.
    Each of k+1 gaps receives >=0 AA loops; color assignments counted by binomial.
    """
    masses=defaultdict(int); num_alloc=0
    for gaps in combinations_with_replacement(range(k+1),loops):
        loopcounts=Counter(gaps)
        w=['A']
        for i in range(k+1):
            w.extend(['A']*loopcounts[i])
            if i<k:w.extend([i,'A']) # numbered color-unknown excursion
        if sum(x=='A' for x in w[:m])!=K:continue
        num_alloc+=1
        x,y=w[m-1],w[m]
        if x=='A' and y=='A':masses[(A,A,A,A)]+=comb(k,b)
        else:
            assert (x=='A')!=(y=='A')
            for color,ways in ((B,comb(k-1,b-1) if b else 0),(C,comb(k-1,b) if b<=k-1 else 0)):
                masses[(A,A,color if x!='A' else A,color if y!='A' else A)]+=ways
    return {x:v for x,v in masses.items() if v},num_alloc

def large():
    k,b,loops,m=26,14,3,35
    phi=star_phi(k,b,loops,m)
    computed,stats=count_classes(phi)
    independent,allocations=independent_star(k,b,loops,m,phi[2])
    assert computed==independent,(computed,independent)
    ordered=sorted(computed)
    return dict(k=k,b=b,AA_loops=loops,m=m,n=phi[1][0],K=phi[2],
                classes=len(ordered),fiber_population=sum(computed.values()),
                unconstrained_K_population=comb(k,b)*comb(k+loops,loops),
                populations=[{'repair':[int(v) for v in tag],'mass':str(computed[tag]),'rank':idx} for idx,tag in enumerate(ordered)],
                dp_states=stats['states'],integer_transfer_calls=stats['transitions'],
                independent_matching_loop_allocations=allocations)

if __name__=='__main__':
    result={'stage':'470-B','scope':'complete ternary observer fiber, h=0, original X6 +E1/+E2/+E3; full signed 12 future APPEND alphabet via Stage469 theorem','small_exhaustive':exhaustive_tests(),'large_exact':large(),'all_assertions_passed':True}
    with open('/mnt/data/STAGE470B_EXECUTED.json','w') as f:json.dump(result,f,indent=2,ensure_ascii=False)
    print(json.dumps(result,indent=2,ensure_ascii=False))
