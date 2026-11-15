#!/usr/bin/env python3
"""PREFIX-804: exact named-edge cut convolution, independent full-cartesian verification.
Python >=3.9 standard library only. No rounding, no external scientific libraries.
"""
from collections import defaultdict
from itertools import product
import json
import time

SHAPES = ((2,2,2), (2,3,2), (3,3,1))

def weight(i,j):
    return ((i+2*j)%5-2, (2*i-j+9)%5-2)

def zero(n):return (0,)*n

def add(a,b):return tuple(x+y for x,y in zip(a,b))

def enumerate_edges(b,c,K,edges,w=weight):
    """Group every named assignment to these edges by FULL global margins and signed observer."""
    out={}
    R=[0]*b;S=[0]*c
    def rec(k,obs):
        if k==len(edges):
            m=(tuple(R),tuple(S)); h=out.setdefault(m,{})
            h[obs]=h.get(obs,0)+1
            return
        e=edges[k];i,j=divmod(e,c);u,v=w(i,j)
        for t in range(K[e]+1):
            R[i]+=t;S[j]+=t
            rec(k+1,(obs[0]+u*t,obs[1]+v*t))
            R[i]-=t;S[j]-=t
    rec(0,(0,0))
    return out

def cut_groups(b,c,K,rowsA,colsA):
    AA,BB,X=[],[],[]
    U=set(rowsA);V=set(colsA)
    for e in range(b*c):
        i,j=divmod(e,c)
        if i in U and j in V: AA.append(e)
        elif i not in U and j not in V: BB.append(e)
        else:X.append(e)
    return AA,BB,X

def split_histograms(b,c,K,rowsA,colsA,w=weight):
    """Independent cut expansion of exact fiber generating functions, grouped by all margins."""
    A,B,X=cut_groups(b,c,K,rowsA,colsA)
    HA=enumerate_edges(b,c,K,A,w)
    HB=enumerate_edges(b,c,K,B,w)
    HX=enumerate_edges(b,c,K,X,w)
    ans={}
    pair_merges=0
    for (rA,sA),pA in HA.items():
        for (rB,sB),pB in HB.items():
            marginI=(add(rA,rB),add(sA,sB))
            for (rX,sX),pX in HX.items():
                m=(add(marginI[0],rX),add(marginI[1],sX))
                p=ans.setdefault(m,{})
                for (a,b0),na in pA.items():
                    for (c0,d),nb in pB.items():
                        for (f,g),nx in pX.items():
                            z=(a+c0+f,b0+d+g)
                            p[z]=p.get(z,0)+na*nb*nx
                            pair_merges+=1
    return ans,{'A_edges':len(A),'B_edges':len(B),'cross_edges':len(X),'partA_fibers':len(HA),'partB_fibers':len(HB),'cross_fibers':len(HX),'exponent_multiplications':pair_merges}

def signed_cut_transport(b,c,t,rowsA,colsA):
    """t is a full edge-value vector, returns crossing signed flow A to B."""
    U=set(rowsA);V=set(colsA)
    return sum(t[i*c+j] if (i in U and j not in V) else -t[i*c+j]
               for i in range(b) for j in range(c)
               if (i in U)!=(j in V))

def direct_tables(b,c,K,rowsA,colsA):
    """Independently track cut conservation over all named tables."""
    expected={}
    zero_cut_count=0;cut_violations=0
    R=[0]*b;S=[0]*c
    def rec(e,t):
        nonlocal zero_cut_count,cut_violations
        if e==b*c:
            D=sum(R[i] for i in rowsA)-sum(S[j] for j in colsA)
            actual=signed_cut_transport(b,c,t,rowsA,colsA)
            if D!=actual:cut_violations+=1
            if D==0:zero_cut_count+=1
            return
        i,j=divmod(e,c)
        for x in range(K[e]+1):
            t.append(x);R[i]+=x;S[j]+=x
            rec(e+1,t)
            R[i]-=x;S[j]-=x;t.pop()
    rec(0,[])
    return zero_cut_count,cut_violations

def linked_example():
    b=c=4;K=[0]*16
    for i in (0,1):
        for j in (0,1):K[i*c+j]=1
    for i in (2,3):
        for j in (2,3):K[i*c+j]=1
    K[0*c+2]=K[1*c+2]=1
    R=(1,2,1,1); S=(1,1,2,1)
    def w(i,j):
        return {(0,0):(1,0),(2,2):(0,1),(0,2):(2,-1),(1,2):(-1,2)}.get((i,j),(0,0))
    direct=enumerate_edges(b,c,K,range(16),w)
    split,stats=split_histograms(b,c,K,(0,1),(0,1),w)
    assert direct==split
    h=direct[(R,S)]
    cut_per_t=defaultdict(int)
    contributions=defaultdict(lambda:defaultdict(int))
    for values in product(*(range(k+1) for k in K)):
        rr=[0]*b;ss=[0]*c;obs=(0,0)
        for e,t in enumerate(values):
            i,j=divmod(e,c);rr[i]+=t;ss[j]+=t
            a,d=w(i,j);obs=(obs[0]+a*t,obs[1]+d*t)
        if tuple(rr)==R and tuple(ss)==S:
            pair=(values[2],values[6]);cut_per_t[pair]+=1;contributions[pair][obs]+=1
    assert cut_per_t=={(0,1):4,(1,0):2},cut_per_t
    assert sum(h.values())==6
    assert signed_cut_transport(4,4,[0]*16,(0,1),(0,1))==0
    return {'edge_capacities':K,'rows':R,'cols':S,'crossing_named_edges':[[0,2],[1,2]],
            'cut_demand':sum(R[:2])-sum(S[:2]),
            'crossing_multiplicities':{f'{a},{b}':n for (a,b),n in sorted(cut_per_t.items())},
            'histogram':[{ 'exponent':list(z), 'count':n} for z,n in sorted(h.items())],
            'per_transfer_histogram':{f'{a},{b}':[{'exponent':list(z),'count':n} for z,n in sorted(contributions[(a,b)].items())]
                                      for a,b in sorted(cut_per_t)},
            'stats':stats}

def run():
    start=time.perf_counter()
    report={'schema':'PREFIX804_NAMED_TWO_SIDED_CUT_CONVOLUTION_V1',
            'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'arithmetic':'arbitrary-precision integer histograms / signed integer Laurent exponents',
            'coverage':'all capacities in 0..max for each declared complete bipartite shape; all feasible row/col margins',
            'shapes':[]}
    P=F=T=C=Q=0
    for b,c,maxcap in SHAPES:
        rowsA,colsA= ((0,), (0,)) if (b,c)==(2,2) else (((0,), (0,1)) if (b,c)==(2,3) else ((0,1),(0,1)))
        pcount=fcount=tcount=checks=transfers=0
        t0=time.perf_counter()
        for K in product(range(maxcap+1),repeat=b*c):
            pcount+=1
            raw=enumerate_edges(b,c,K,range(b*c))
            cut,stats=split_histograms(b,c,K,rowsA,colsA)
            assert raw==cut,('cut expansion',b,c,K)
            n=sum(sum(h.values()) for h in raw.values())
            assert n==len(list(product(*(range(k+1) for k in K))))
            fcount+=len(raw);tcount+=n
            transfers+=stats['exponent_multiplications']
            checks+=1+len(raw)*2
            for key,h in raw.items():
                assert cut[key]==h,('fiber',b,c,K,key)
                assert sum(h.values())==sum(cut[key].values()),('coefficient sum',b,c,K,key)
            if K==tuple([maxcap]*(b*c)):
                z,violation=direct_tables(b,c,K,rowsA,colsA)
                assert violation==0,('cut conservation',b,c,K)
                checks+=n
        report['shapes'].append({'rows':b,'cols':c,'max_capacity':maxcap,
                                'patterns':pcount,'fibers':fcount,'complete_named_tables':tcount,
                                'checks':checks,'expansion_monomial_multiplications':transfers,
                                'wall_seconds':round(time.perf_counter()-t0,6)})
        P+=pcount;F+=fcount;T+=tcount;C+=checks;Q+=transfers
    w=linked_example()
    C+=6
    report.update({'totals':{'patterns':P,'fibers':F,'complete_named_tables':T,
                              'exact_checks':C,'expansion_monomial_multiplications':Q},
                   'two_edge_cut_witness':w,'elapsed_seconds':round(time.perf_counter()-start,6),
                   'result':'ALL_CHECKS_PASS PREFIX804 NAMED_EDGE_CUT_LAURENT_CONVOLUTION'})
    return report

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
