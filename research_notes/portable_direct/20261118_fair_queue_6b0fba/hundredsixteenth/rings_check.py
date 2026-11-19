"""Exact sparse bracelet reconstruction from windows, with the original Q22 comparator."""
import argparse
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
from itertools import combinations, permutations
import json
from math import comb, factorial
from pathlib import Path

W61_SHA = '81cc6e5c4490a689f7de90abd8056f2c77706449b753f56d330f7152c40fae6b'


def dihedral(x):
    return min(y[i:]+y[:i] for y in (x,x[::-1]) for i in range(len(x)))


def binary(g):
    return ''.join('1'+'0'*(d-1) for d in g)


def windows(x,W):
    circle = x+x
    blocks = (circle[i:i+W+1] for i in range(len(x)))
    return tuple(sorted(min(b,b[::-1]) for b in blocks))


def compositions(k,m):
    for a in combinations(range(1,k),m-1):
        p=(0,)+a+(k,)
        yield tuple(v-u for u,v in zip(p,p[1:]))


def gap_key(g,W):
    visible=tuple(sorted(x for x in g if x<=W))
    pairs=tuple(sorted(tuple(sorted((a,b))) for a,b in zip(g,g[1:]+g[:1]) if a+b<=W))
    return visible,pairs


def three_size(k,W,known):
    if len(known)>=2:
        return 1
    if len(known)==1:
        return (k-known[0])//2-W
    slack=k-3*(W+1)
    return (slack*slack+6*slack+12)//12


def order_width(g):
    a,b,c,d=sorted(g)
    adj=set(tuple(sorted((u,v))) for u,v in zip(g,g[1:]+g[:1]))
    return a+c if (a,b) in adj else a+b


def census(lib,kernel,k,m,native_bound):
    reps=sorted({dihedral(g) for g in compositions(k,m)})
    xs=[binary(g) for g in reps]
    maximum=(k-1)//2-1 if m==3 else k//2-1
    maximum=max(0,maximum)
    if (m,k) in ((3,4),(4,4),(4,5)):
        maximum=0
    native=k<=native_bound
    by_round=[lib.native_rounds(kernel,x,1+(maximum+1)//2) for x in xs] if native else []
    earliest=[None]*len(xs)
    rows=[]
    checked=0
    for W in range(min(k-1,maximum+1)+1):
        counts=Counter()
        bij,back={},{}
        nk,nr={},{}
        for j,(g,x) in enumerate(zip(reps,xs)):
            read=windows(x,W)
            singles,pairs=gap_key(g,W)
            key=singles if m==3 else (singles,pairs)
            assert bij.setdefault(key,read)==read and back.setdefault(read,key)==key
            if native and W%2==0:
                signature=by_round[j][1+W//2]
                assert nk.setdefault(key,signature)==signature and nr.setdefault(signature,key)==key
                checked+=1
            counts[key]+=1
        rows.append(len(counts))
        for j,g in enumerate(reps):
            singles,pairs=gap_key(g,W)
            key=singles if m==3 else (singles,pairs)
            if m==3:
                assert three_size(k,W,singles)==counts[key]
            if counts[key]==1 and earliest[j] is None:
                earliest[j]=W
    assert max(earliest)==maximum
    for W,g in zip(earliest,reps):
        if m==3:
            a,b,c=sorted(g)
            assert W==b-int(c-b<=1)
        else:
            a,b,c,d=sorted(g)
            multiplicities=sorted(Counter(g).values())
            if len(multiplicities)==4:
                bound=order_width(g)
            elif multiplicities in ([2,2],[1,1,2]):
                bound=a+b
            else:
                bound=0
            assert W==max(c-int(d-c<=1),bound)
    label_weights=[]
    for g in reps:
        # Number of expanded words with arbitrary marked positions and fixed origin.
        variants={h[i:]+h[:i] for h in (g,g[::-1]) for i in range(m)}
        weight=len(variants)*k//m
        assert weight*m==len(variants)*k
        label_weights.append(weight)
    assert sum(label_weights)==comb(k,m)
    return dict(k=k,marks=m,bracelets=len(reps),max_width=maximum,
                mean_first_width_labelled=str(F(sum(w*q for w,q in zip(earliest,label_weights)),sum(label_weights))),
                mean_first_width_bracelets=str(F(sum(earliest),len(earliest))),
                classes_by_width=rows,original_graphs=len(reps) if native else 0,
                original_packets=checked)


def completions(labels, edges):
    adj={v:set() for v in labels}
    for a,b in edges:
        adj[a].add(b)
        adj[b].add(a)
    if any(len(nbr)>2 for nbr in adj.values()):
        return 0
    unvisited=set(labels)
    paths=isolated=0
    while unvisited:
        todo=[next(iter(unvisited))]
        comp=set()
        while todo:
            u=todo.pop()
            if u not in comp:
                comp.add(u)
                todo.extend(adj[u]-comp)
        unvisited-=comp
        if len(comp)==1:
            isolated+=1
        elif all(len(adj[v])==2 for v in comp):
            return int(len(comp)==len(labels))
        else:
            paths+=1
    return 2**paths * factorial(paths+isolated-1)//2


def fiber_size(labels,W,key):
    mandatory=set(key[1])
    allowed_to_forbid=[(a,b) for a,b in combinations(labels,2) if a+b<=W and (a,b) not in mandatory]
    return sum((-1)**j*completions(labels,mandatory|set(xs))
               for j in range(len(allowed_to_forbid)+1) for xs in combinations(allowed_to_forbid,j))


def larger_cases():
    cases=[]
    for labels in [(1,2,3,4,5),(1,3,4,7,9),(1,2,3,4,5,6),(2,3,5,7,11,13,17)]:
        orders=sorted({dihedral(g) for g in permutations(labels)})
        xs=list(map(binary,orders))
        hist=[]
        for W in [w for w in range(sum(labels)) if sum(x>w for x in labels)<=1]:
            by_key,by_deck={},{}
            counts=Counter()
            for g,x in zip(orders,xs):
                key=gap_key(g,W)
                counts[key]+=1
                packet=windows(x,W)
                assert by_key.setdefault(key,packet)==packet and by_deck.setdefault(packet,key)==key
            if len(labels)<=5:
                for key,count in counts.items():
                    assert count==fiber_size(labels,W,key)
            hist.append([W,len(by_key)])
        cases.append(dict(labels=labels,hamilton_cycles=len(orders),classes_by_width=hist))
    return cases


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path)
    p.add_argument('--wave61',type=Path,default=Path(__file__).resolve().parents[1]/'sixtyfirst'/'rings_check.py')
    args=p.parse_args()
    assert sha256(args.wave61.read_bytes()).hexdigest()==W61_SHA
    spec=importlib.util.spec_from_file_location('wave61',args.wave61)
    lib=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lib)
    kernel=lib.get_kernel(args.source)
    cases=[census(lib,kernel,k,m,16) for k in range(4,33) for m in (3,4)]
    more=larger_cases()
    out=dict(original_source_sha256=lib.SHA,wave61_adapter_sha256=W61_SHA,
             original_graphs=sum(r['original_graphs'] for r in cases),
             original_packets=sum(r['original_packets'] for r in cases),
             sparse_bracelets=sum(r['bracelets'] for r in cases),
             sparse_cases=cases,distinct_gap_cases=more)
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
