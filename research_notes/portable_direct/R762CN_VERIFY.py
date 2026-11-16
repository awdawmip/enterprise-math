#!/usr/bin/env python3
"""R762CN two-mark weighted positive N-BRC exhaustive exact verifier.
Standard library only; all source counts use integer arithmetic.
"""
import itertools, json
from collections import defaultdict

VERTICES = range(4)
EDGES = tuple(itertools.combinations(VERTICES, 2))
NAMES = tuple(''.join(map(str,e)) for e in EDGES)
STATES = tuple(sorted(set(min(tuple(sorted(s)),tuple(i for i in range(6) if i not in s))
                         for s in itertools.combinations(range(6),3))))
INDEX = {s:i for i,s in enumerate(STATES)}
STARS = {frozenset(EDGES.index(tuple(sorted((v,w)))) for w in VERTICES if w!=v)
         for v in VERTICES}
KIND = tuple('F' if frozenset(s) in STARS or
             frozenset(set(range(6))-set(s)) in STARS else 'P' for s in STATES)

def canonical(s):
    s=tuple(sorted(s))
    return min(s,tuple(i for i in range(6) if i not in s))

def transfer(a,b,lam,mu):
    M=[[0]*10 for _ in range(10)]
    for i,s in enumerate(STATES):
        A=set(s); B=set(range(6))-A
        for x,y in itertools.product(A,B):
            j=INDEX[canonical((A-{x})|{y})]
            w=(lam if a in (x,y) else 1)*(mu if b in (x,y) else 1)
            M[i][j]=w
    return M

def output_signatures(M,depth):
    vectors=[[int(k=='F') for k in KIND],[int(k=='P') for k in KIND]]
    out=[[] for _ in STATES]
    for t in range(depth+1):
        for i in range(10):out[i].extend(v[i] for v in vectors)
        vectors=[[sum(M[i][j]*v[j] for j in range(10)) for i in range(10)]
                 for v in vectors]
    return tuple(map(tuple,out))

def classes(M,depth):
    groups=defaultdict(list)
    for i,signature in enumerate(output_signatures(M,depth)):
        groups[signature].append(i)
    return tuple(sorted(tuple(g) for g in groups.values()))

def quotient(M,groups):
    Q=[]
    for g in groups:
        r=[sum(M[g[0]][j] for j in h) for h in groups]
        for i in g:
            assert [sum(M[i][j] for j in h) for h in groups]==r
        Q.append(r)
    return Q

def expected_count(adj,lam,mu):
    if lam==mu==1:return 2
    if not adj:return 3
    if lam==1 or mu==1:return 3
    if lam==mu:return 5
    return 7

PAIRS={'adjacent':(0,1),'disjoint':(0,5)}
GROUPS={
 'adjacent': ((0,1),(2,),(3,),(4,),(5,7),(6,8),(9,)),
 'disjoint': ((0,1,5,7),(2,4),(3,6,8,9)),
}
ASSERTIONS=0
for geometry,(a,b) in PAIRS.items():
    for lam,mu in itertools.product(range(13),repeat=2):
        M=transfer(a,b,lam,mu)
        assert all(M[i][i]==0 for i in range(10));ASSERTIONS+=1
        assert all(M[i][j]==M[j][i] for i in range(10) for j in range(10));ASSERTIONS+=1
        assert all(sum(w!=0 for w in row)<=9 for row in M);ASSERTIONS+=1
        for i,s in enumerate(STATES):
            same=(a in s)==(b in s)
            degree=3*(lam+mu+1) if same else 4+2*lam+2*mu+lam*mu
            assert sum(M[i])==degree;ASSERTIONS+=1
        assert len(classes(M,1))==expected_count(geometry=='adjacent',lam,mu);ASSERTIONS+=1
        assert classes(M,1)==classes(M,9);ASSERTIONS+=1
        quotient(M,GROUPS[geometry]);ASSERTIONS+=1
        for dep in range(1,7):
            sig=output_signatures(M,dep)
            assert all(sig[i]==sig[j] for g in classes(M,1) for i in g for j in g)
            ASSERTIONS+=1

for lam,mu in itertools.product(range(9),repeat=2):
    Q=quotient(transfer(0,1,lam,mu),GROUPS['adjacent'])
    want=[[1,1,1,mu,lam+mu,lam+mu,lam],
          [2,0,1,lam,2*mu,2*lam,mu],
          [2,1,0,lam,2*lam,2*mu,mu],
          [2*mu,lam,lam,0,2,2,lam*mu],
          [lam+mu,mu,lam,1,1,lam*mu+1,1],
          [lam+mu,lam,mu,1,lam*mu+1,1,1],
          [2*lam,mu,mu,lam*mu,2,2,0]]
    assert Q==want;ASSERTIONS+=1
    Q=quotient(transfer(0,5,lam,mu),GROUPS['disjoint'])
    want=[[lam*mu+2,2,2*lam+2*mu],
          [4,lam*mu,2*lam+2*mu],
          [2*lam+2*mu,lam+mu,3]]
    assert Q==want;ASSERTIONS+=1

W={geometry:{'pair':[NAMES[a],NAMES[b]],'class_count':len(classes(transfer(a,b,2,3),1)),
             'class_sizes':sorted(map(len,classes(transfer(a,b,2,3),1))),
             'degree_distribution':dict(sorted({str(d):sum(sum(r)==d for r in transfer(a,b,2,3))
                                            for d in set(map(sum,transfer(a,b,2,3)))}.items()))}
   for geometry,(a,b) in PAIRS.items()}
print(json.dumps({'schema':'R762CN_EXACT_EVIDENCE_V1',
 'parameter_domain_checked':'0<=lambda,mu<=12',
 'depths_checked':'one-step predictive quotient equals all-horizon through 9; quotient future counts through 6',
 'assertion_groups':ASSERTIONS,'state_count':10,'edge_count':6,'cases':W,
 'status':'AUTHOR_EXACT_CHECK_PASSED','independent_review':'NOT_REVIEWED'},
 ensure_ascii=False,indent=2))
