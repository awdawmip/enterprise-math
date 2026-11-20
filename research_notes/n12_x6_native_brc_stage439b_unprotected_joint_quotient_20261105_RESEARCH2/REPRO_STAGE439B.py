#!/usr/bin/env python3
"""Stage439-B exact future quotient checker, static signed X6 paths.
Python stdlib only. All 12 native signed directions are explored as future APPEND labels.
"""
import json
from collections import defaultdict, Counter
from functools import lru_cache
from itertools import product

DIRECTIONS = tuple(range(12))
A, B, C = 0, 6, 1

@lru_cache(None)
def own(word):
    v = [0]*6
    for d in word:
        v[d%6] += 1 if d<6 else -1
    j = tuple(sorted(Counter(zip(word,word[1:])).items()))
    return (len(word),tuple(v),j)

@lru_cache(None)
def observe(P,Q):
    return (own(P), own(Q), sum(a==b for a,b in zip(P,Q)))

def repair_key(P,Q,pP,rP,pQ,rQ):
    m,n=len(P),len(Q)
    assert 0<=pP<m and 0<=pQ<n and rP>=0 and rQ>=0
    c = min(m-pP, n-pQ)
    # Store one-source removal tails, the opposite source's original symbols
    # at rewritable positions, and unprotected original match bits.
    sP=P[m-pP-1:]
    sQ=Q[n-pQ-1:]
    cross_P=tuple((i,P[i-1]) for i in range(n-pQ+1,min(m,n+rQ)+1)) if rQ else ()
    cross_Q=tuple((i,Q[i-1]) for i in range(m-pP+1,min(n,m+rP)+1)) if rP else ()
    bits=tuple((i,int(P[i-1]==Q[i-1])) for i in range(c+1,min(m,n)+1))
    return (sP,sQ,cross_P,cross_Q,bits)

def options(P,Q,b):
    pP,rP,pQ,rQ=b
    if pP and len(P)>1:
        yield ('PP',None),P[:-1],Q,(pP-1,rP,pQ,rQ)
    if pQ and len(Q)>1:
        yield ('QP',None),P,Q[:-1],(pP,rP,pQ-1,rQ)
    if rP:
        for d in DIRECTIONS:
            yield ('PA',d),P+(d,),Q,(pP,rP-1,pQ,rQ)
    if rQ:
        for d in DIRECTIONS:
            yield ('QA',d),P,Q+(d,),(pP,rP,pQ,rQ-1)

def distinguish(P,Q,P2,Q2,b):
    """Return None iff all finite labelled traces agree; else first witness operation word."""
    @lru_cache(None)
    def rec(X,Y,U,V,budget):
        if observe(X,Y)!=observe(U,V):
            return ()
        for op,Xn,Yn,bn in options(X,Y,budget):
            if op[0]=='PP': Un,Vn=U[:-1],V
            elif op[0]=='QP': Un,Vn=U,V[:-1]
            elif op[0]=='PA': Un,Vn=U+(op[1],),V
            else: Un,Vn=U,V+(op[1],)
            witness=rec(Xn,Yn,Un,Vn,bn)
            if witness is not None:
                return (op,)+witness
        return None
    return rec(P,Q,P2,Q2,b)

def strpath(w): return ''.join({A:'A',B:'B',C:'C'}.get(d, str(d)) for d in w)

def family():
    P=(C,)*4
    histories=[(P,(A,)*(j-1)+(B,)+(A,)*(8-j)) for j in range(2,8)]
    budget=(1,1,1,1)
    assert len({observe(*h) for h in histories})==1
    classes=defaultdict(list)
    for idx,h in enumerate(histories,2):classes[repair_key(*h,*budget)].append(idx)
    populations=sorted((len(v) for v in classes.values()),reverse=True)
    assert populations==[3,1,1,1],populations
    trace=[]
    for i,h in enumerate(histories):
        for j,h2 in enumerate(histories[:i]):
            w=distinguish(*h,*h2,budget)
            equal=repair_key(*h,*budget)==repair_key(*h2,*budget)
            assert (w is None)==equal,(i,j,w,equal)
            if w is not None and len(trace)<5:
                trace.append({'j':i+2,'j2':j+2,'word':w,'end_observers':[observe(*apply(h,w)),observe(*apply(h2,w))]})
    # Exact designated witnesses between j=4/5 and j=2.
    assert observe(*apply(histories[2],(('PP',None),('PA',B))))[-1]==1
    assert observe(*apply(histories[0],(('PP',None),('PA',B))))[-1]==0
    assert observe(*apply(histories[3],(('PA',B),)))[-1]==1
    assert observe(*apply(histories[0],(('PA',B),)))[-1]==0
    return {'initial_histories':6,'classes':len(classes),'class_populations':populations,
            'representatives':sorted([list(v) for v in classes.values()]),
            'witness_P_pop_then_append_B':{'j4_K':1,'j2_K':0},
            'witness_P_append_B':{'j5_K':1,'j2_K':0},
            'checked_all_history_pairs':15}

def apply(h,w):
    P,Q=h
    for op,d in w:
        if op=='PP': P=P[:-1]
        elif op=='QP': Q=Q[:-1]
        elif op=='PA': P=P+(d,)
        elif op=='QA': Q=Q+(d,)
    return P,Q

def domain(m,n,budget,alphabet=(A,B,C)):
    fibers=defaultdict(list)
    for P in product(alphabet,repeat=m):
        for Q in product(alphabet,repeat=n):
            fibers[observe(P,Q)].append((P,Q))
    compared=equal=separated=0; nontrivial=0; total_classes=0; nontrivial_quotients=0; largest_class=0
    for f in fibers.values():
        classes=Counter(repair_key(P,Q,*budget) for P,Q in f)
        total_classes+=len(classes)
        nontrivial_quotients+=int(len(classes)>1)
        largest_class=max(largest_class,max(classes.values()))
        if len(f)<2: continue
        nontrivial+=1
        for i,(P,Q) in enumerate(f):
            key=repair_key(P,Q,*budget)
            for P2,Q2 in f[:i]:
                w=distinguish(P,Q,P2,Q2,budget)
                prediction=key==repair_key(P2,Q2,*budget)
                assert (w is None)==prediction,(m,n,budget,P,Q,P2,Q2,w)
                compared+=1
                equal+=int(prediction); separated+=int(not prediction)
    return {'m':m,'n':n,'budgets':budget,'raw_pairs':len(alphabet)**(m+n),
      'complete_O_fibers':len(fibers),'nonsingleton_fibers':nontrivial,
      'history_pair_checks':compared,'equivalent_pair_checks':equal,'separated_pair_checks':separated,
      'total_future_classes_across_fibers':total_classes, 'split_fibers':nontrivial_quotients, 'largest_class_population':largest_class}

if __name__=='__main__':
    results={'result':'STAGE439B_UNPROTECTED_TWO_SIDED_EXACT_QUOTIENT_PASS',
      'native_directions':12,'family':family(),'domains':[]}
    for args in [(3,3,(1,1,1,1)),(4,3,(1,1,1,1)),(3,4,(1,1,1,1)),(4,4,(1,1,1,1)),
                 (4,3,(2,1,1,1)),(3,4,(1,1,2,1)),(5,4,(1,1,1,1)),(4,5,(1,1,1,1)),(5,5,(1,1,1,1)),
                 (4,5,(1,0,1,0)),(5,4,(1,0,1,0))]:
        d=domain(*args)
        results['domains'].append(d)
    print(json.dumps(results,sort_keys=True,ensure_ascii=False,separators=(',',':')))
