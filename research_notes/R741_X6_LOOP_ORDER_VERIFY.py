#!/usr/bin/env python3
"""R741: exact finite signed X6 path BRC and typed V39 loop model.
Pure Python standard-library integer / S3-permutation arithmetic.
No native TRIADIC_CLOSURE_E physical event execution is claimed.
"""
from collections import Counter, defaultdict
from itertools import permutations, product
from math import comb, factorial

def current(w, axes):
    p={a:0 for a in axes}
    f=Counter()
    for a,s in w:
        lo=tuple(p[i]-(1 if i==a and s<0 else 0) for i in axes)
        f[(lo,a)]+=s
        p[a]+=s
    assert all(v==0 for v in p.values())
    return tuple(sorted((edge,n) for edge,n in f.items() if n))

def nb(w):
    return all(w[t]!=(w[t-1][0],-w[t-1][1]) for t in range(1,len(w)))

def qe(w,axes):
    q={}; order=[]
    for a,s in w:
        if a not in q:q[a]=s;order.append(a)
    inv=sum(order[i]>order[j] for i in range(len(order))
            for j in range(i+1,len(order)))
    return tuple(q[a] for a in axes), 1 if inv%2==0 else -1

def hist(group):
    return dict(sorted(Counter(map(len,group.values())).items()))

def compose(g,h):return tuple(g[h[i]] for i in range(3))

def four_axis_census():
    axes=(0,1,2,3)
    signed=tuple((a,s) for a in axes for s in (+1,-1))
    allj=defaultdict(list);nbj=defaultdict(list)
    jQ=defaultdict(list);jQe=defaultdict(list);jfirst=defaultdict(list)
    supp=Counter()
    for w in permutations(signed):
        j=current(w,axes);allj[j].append(w);supp[len(j)]+=1
        if nb(w):
            nbj[j].append(w)
            q,e=qe(w,axes)
            jQ[j,q].append(w)
            jQe[j,q,e].append(w)
            jfirst[j,w[0]].append(w)
    assert sum(map(len,allj.values()))==factorial(8)==40320
    assert len(allj)==14449
    assert hist(allj)=={1:13056,2:384,14:960,160:48,5376:1}
    assert supp=={0:5376,4:10752,6:12288,8:11904}
    nbcount=sum(map(len,nbj.values()))
    assert nbcount==sum((-1)**k*comb(4,k)*2**k*factorial(8-k)
                        for k in range(5))==13824
    assert len(nbj)==13440 and hist(nbj)=={1:13056,2:384}
    assert len(jQ)==13440 and hist(jQ)=={1:13056,2:384}
    assert len(jQe)==13632 and hist(jQe)=={1:13440,2:192}
    assert len(jfirst)==13824 and hist(jfirst)=={1:13824}
    typ=Counter((len(j),len(v)) for j,v in nbj.items())
    assert typ=={(4,2):192,(6,1):1536,(8,1):11520,(8,2):192}
    assert all(v[0][0]!=v[1][0] for v in nbj.values() if len(v)==2)
    pats=set(permutations((0,0,1,1,2,2,3,3)))
    assert len(pats)==2520
    second=set()
    for pat in pats:
        for signs in product((-1,1),repeat=4):
            used=[0]*4;w=[]
            for a in pat:
                w.append((a,signs[a]*(-1 if used[a] else 1)))
                used[a]+=1
            second.add(tuple(w))
    assert len(second)==40320
    return {'all_branches':40320,'all_j_classes':14449,
            'all_j_fibers':hist(allj),'all_current_support':dict(supp),
            'NB_branches':13824,'NB_j_classes':len(nbj),
            'NB_j_fibers':hist(nbj),
            'NB_support_fibers':{str(k):v for k,v in sorted(typ.items())},
            'NB_jQ_classes':len(jQ),'NB_jQepsilon_classes':len(jQe),
            'NB_j_firststep_classes':len(jfirst),
            'residual_worst_bits':1,'uniform_expected_residual_bits':'1/18'}

def three_loop_wedge():
    axes=tuple(range(6))
    loops=[((a,+1),(b,+1),(a,-1),(b,-1))
           for a,b in ((0,1),(2,3),(4,5))]
    gens=((1,0,2),(0,2,1),(2,1,0))
    rows=[];flowset=set()
    for order in permutations(range(3)):
        w=tuple(s for i in order for s in loops[i])
        assert nb(w)
        flowset.add(current(w,axes))
        q,e=qe(w,axes)
        h=(0,1,2)
        for i in order:h=compose(gens[i],h)
        rows.append((''.join('ABC'[i] for i in order),h,q,e))
    assert len(rows)==6 and len(flowset)==1
    assert len(next(iter(flowset)))==12
    assert len(set(r[2] for r in rows))==1
    assert set(r[3] for r in rows)=={1}
    assert Counter(Counter(r[1] for r in rows).values())=={2:3}
    assert {r[1] for r in rows}==set(gens)
    return {'histories':6,'shared_current_support_edges':12,
            'same_Q':True,'same_epsilon':True,
            'S3_distinct_h':3,'S3_h_fibers':{'2':3},
            'per_order':[{'word_order':r[0],'h':list(r[1])} for r in rows],
            'j_only_residual_bits':3,'j_h_residual_bits':1}

def check_S6_covariance():
    axes=(0,1,2,3)
    signed=tuple((a,s) for a in axes for s in (+1,-1))
    n=0
    for w in permutations(signed):
        flow=current(w,axes)
        for k in range(5):
            g={i:(i+1 if i==k else i-1 if i==k+1 else i)
               for i in range(6)}
            dst=tuple(sorted(g[a] for a in axes))
            mapped=tuple((g[a],s) for a,s in w)
            transformed=[]
            for (pos,a),v in flow:
                ren={g[axes[i]]:pos[i] for i in range(4)}
                transformed.append(((tuple(ren[a] for a in dst),g[a]),v))
            assert current(mapped,dst)==tuple(sorted(transformed))
            n+=1
    assert n==201600
    return n

if __name__=="__main__":
    a=four_axis_census()
    b=three_loop_wedge()
    n=check_S6_covariance()
    print("R741_X6_LOOP_ORDER_BRC_EXACT_PASS")
    print("W4:",a)
    print("X6 three loops:",b)
    print("S6 generator checks:",n)
