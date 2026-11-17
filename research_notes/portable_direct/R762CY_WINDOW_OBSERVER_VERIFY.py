"""R762CY exact positive C3 Port-window observer seed-budget verifier.

No floating point. Runs complete finite parameter box and explicit integral
De Bruijn flow conservation, plus path decomposition for small cases.
"""
from math import gcd
from functools import reduce
import json
from collections import defaultdict


def gcd_vec(v):
    return reduce(gcd, v, 0)

def counts(p,q,h):
    a=(1,0,0)
    out=[a]
    for t in range(h):
        b=[0]*3
        for i,c in enumerate(a):
            b[(i+1)%3]+=c*p
            b[(i-1)%3]+=c*q
        a=tuple(b)
        out.append(a)
    return out

def paths(r):
    for z in range(1 << r):
        yield tuple((z >> k)&1 for k in range(r))

def transitions(i,w):
    states=[i]
    for b in w:
        i=(i+1)%3 if b==0 else (i-1)%3
        states.append(i)
    return tuple(states)

def window_counts(p,q, Cs, M, D, t, r):
    """integer directed r-window count, indexed by its Port sequence"""
    out={}
    for i in range(3):
        for w in paths(r):
            z=transitions(i,w)
            a=w.count(0); b=r-a
            numerator=M*Cs[t][i]*(p**a)*(q**b)
            denom=D**(t+r)
            assert numerator%denom==0, (p,q,t,r,z,numerator,denom)
            v=numerator//denom
            if v: out[z]=v
    assert sum(out.values())==M
    return out

def check_graph(p,q,h,r, Cs,M,D, do_decompose=False):
    assert r>=1
    layers=[window_counts(p,q,Cs,M,D,t,r) for t in range(h-r+1)]
    for t in range(1,len(layers)):
        incoming=defaultdict(int); outgoing=defaultdict(int)
        for path,m in layers[t-1].items(): incoming[path[1:]]+=m
        for path,m in layers[t].items(): outgoing[path[:-1]]+=m
        assert incoming==outgoing,(p,q,h,r,t)
    if do_decompose:
        # Greedy integer decomposition in layered DAG. Edges with nonzero
        # integer weights suffice due exactly equal intermediate marginal.
        edges=[dict(layer) for layer in layers]
        reconstructed=defaultdict(int)
        while edges[0]:
            start=next(iter(edges[0]))
            path=[]
            for t in range(len(edges)):
                node=tuple(path[-r:])
                eligible=([start] if t==0 else [k for k,v in edges[t].items() if v and k[:-1]==node])
                assert eligible,(p,q,h,r,t,node)
                k=eligible[0]
                if t==0:
                    path=list(k)
                else:
                    path.append(k[-1])
                edges[t][k]-=1
                if not edges[t][k]:del edges[t][k]
            reconstructed[tuple(path)]+=1
        assert sum(reconstructed.values())==M
        for t,L in enumerate(layers):
            actual=defaultdict(int)
            for path,m in reconstructed.items():actual[path[t:t+r+1]]+=m
            assert actual==L, (p,q,h,r,t)
    return len(layers)

def run():
    results=dict(schema='R762CY_WINDOW_OBSERVER_EVIDENCE_V1', arithmetic='Python arbitrary-precision exact integers', finite_domain={'coprime_pq':'1<=p,q<=5','h':'0..8','r':'0..h'}, tests={}, examples={})
    s=results['tests'];s.update(weight_pairs=0,horizon_cases=0,window_cases=0,coefficient_gcd_checks=0,integral_window_checks=0,flow_conservation_layers=0,constructed_path_cases=0)
    for p in range(1,6):
        for q in range(1,6):
            if gcd(p,q)>1:continue
            s['weight_pairs']+=1
            D=p+q; C=counts(p,q,8)
            for h in range(9):
                s['horizon_cases']+=1
                for t in range(h+1):
                    expected = 1 if t==0 or D%3 else 3**((t-1)//2)
                    assert gcd_vec(C[t])==expected, (p,q,t,C[t])
                    s['coefficient_gcd_checks']+=1
                for r in range(h+1):
                    s['window_cases']+=1
                    n=h-r
                    g=gcd_vec(C[n]);M=D**h//g
                    assert D**h %g==0
                    for t in range(n+1):
                        for i in range(3):
                            for w in paths(r):
                                a=w.count(0)
                                numer=M*C[t][i]*p**a*q**(r-a)
                                assert numer%(D**(t+r))==0,(p,q,h,r,t,i,w)
                                s['integral_window_checks']+=1
                    if r>0:
                        s['flow_conservation_layers']+=check_graph(p,q,h,r,C,M,D,do_decompose=(h<=4 and p<=3 and q<=3))
                        if h<=4 and p<=3 and q<=3:
                            s['constructed_path_cases']+=1
            assert C[0]==(1,0,0)
    for p,q,h in [(1,2,6),(1,1,6),(2,3,5),(2,4,5)]:
        p1=p//gcd(p,q);q1=q//gcd(p,q)
        D=p1+q1;C=counts(p1,q1,h)
        results['examples'][f'p={p},q={q},h={h}']={f'r={r}':D**h//gcd_vec(C[h-r]) for r in range(h+1)}
    print(json.dumps(results,ensure_ascii=False,indent=2))
if __name__=='__main__':run()
