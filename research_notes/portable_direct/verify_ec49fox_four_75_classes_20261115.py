#!/usr/bin/env python3
"""EC49FOX: exact original BRC finite class and sparse-observer verifier.
Usage: python verify_ec49fox.py /path/to/EC49FOX_EVIDENCE
Input bundle includes the original frozen data and four full C++17 root CSVs.
Python stdlib only. AUTHOR_EXACT_FINITE_CHECKED / NOT_REVIEWED.
"""
from pathlib import Path
from collections import defaultdict
import hashlib, csv, itertools, json, sys

p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(".")
src=p/"EC49FOW_EVIDENCE"/"frozen_original_master.txt"
assert hashlib.sha256(src.read_bytes()).hexdigest()=="cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
R=(3,5,6,7); REPS=(14300,14304,14309,14313)
with src.open() as f:
    nk,nw,nc=map(int,f.readline().split())
    assert (nk,nw,nc)==(94,178850,38169)
    fm=[]; words=[]; num=0
    for k in range(nk):
        n=int(f.readline());num+=n;d=[0]*24;ww=[]
        for _ in range(n):
            l,s=f.readline().split();l=int(l);b=bytes.fromhex(s);r=b[0]
            assert 0<=l<24 and r in R
            d[l]|=1<<R.index(r)
            ww.append((l,r,b[1:]))
        fm.append(d);words.append(ww)
    assert num==nw
    cases=[tuple(map(int,f.readline().split())) for _ in range(nc)]
    assert len(cases)==nc and all(len(c)==7 for c in cases)

def domain(c):
    d=[0]*24
    for k in c:
        for l,m in enumerate(fm[k]):d[l]|=m
    assert all(d)
    return tuple(d)

groups=defaultdict(list)
for i,c in enumerate(cases):groups[domain(c)].append(i)
assert len(groups)==625

class Node:
    def __init__(self):self.children={};self.mask=0

def independent_trie(config,root,D):
    a=[(l,code) for k in cases[config] for l,r,code in words[k] if r==root]
    labels=sorted({l for l,_ in a});local={l:j for j,l in enumerate(labels)}
    tr=Node()
    for l,code in a:
        u=tr
        for ch in code:u=u.children.setdefault(ch,Node())
        u.mask|=1<<local[l]
    def dp(u):
        z={0:0}
        if u.mask:z[u.mask]=0
        for child in u.children.values():
            w=dp(child);nxt={}
            for m,vm in z.items():
                for n,vn in w.items():
                    mask=m|n;v=vm+vn
                    if v<nxt.get(mask,10**10):nxt[mask]=v
            z=nxt
        return {m:v+(m!=0) for m,v in z.items()}
    raw=dp(tr);F=[10**10]*(1<<len(labels))
    for m,v in raw.items():F[m]=v
    for j in range(len(labels)):
        for m in range(len(F)):
            if not m>>j&1:F[m]=min(F[m],F[m|1<<j])
    must=sum(1<<local[l] for l in labels if D[l].bit_count()==1)
    opt=[l for l in labels if D[l].bit_count()>1]
    out={}
    for bits in itertools.product((0,1),repeat=len(opt)):
        mask=must;subset=0
        for l,b in zip(opt,bits):
            if b:mask|=1<<local[l];subset|=1<<l
        out[subset]=F[mask]
    return out

summary=[]; total=[0]*7
for rep in REPS:
    D=domain(cases[rep]);ids=groups[D]
    assert len(ids)==75 and ids[0]==rep
    assert ids==[int(x) for x in (p/("CLASS_%d_IDS.txt"%rep)).read_text().split()]
    opt=[l for l,m in enumerate(D) if m.bit_count()>1]
    allocs=list(itertools.product(*(tuple(R[j] for j in range(4) if D[l]>>j&1) for l in opt)))
    assert len(allocs)==432
    uses=[]
    for a in allocs:
        s={r:0 for r in R}
        for l,r in zip(opt,a):s[r]|=1<<l
        uses.append(tuple((r,s[r]) for r in R))
    optional={r:[l for l in opt if D[l]>>R.index(r)&1] for r in R}
    subsets={r:sorted(sum(1<<l for l,b in zip(optional[r],flags) if b)
                      for flags in itertools.product((0,1),repeat=len(optional[r]))) for r in R}
    nc=sum(map(len,subsets.values()))
    entries=defaultdict(dict)
    with (p/("CLASS_%d_PROFILES.csv"%rep)).open() as f:
        for x in csv.DictReader(f):
            c,r,m,o,s,cost=map(int,(x[k] for k in ("config","root","must","opt","subset","cost")))
            assert c in ids and r in R and s in subsets[r] and (r,s) not in entries[c]
            assert m==sum(1<<l for l in range(24) if D[l]==1<<R.index(r))
            assert o==sum(1<<l for l in optional[r])
            entries[c][r,s]=cost
    assert len(entries)==75 and all(len(entries[c])==nc for c in ids)
    for c in (ids[0],ids[-1]):
        for r in R:
            assert independent_trie(c,r,D)=={s:entries[c][r,s] for s in subsets[r]}
    P={c:tuple(entries[c][r,s] for r in R for s in subsets[r]) for c in ids}
    T={c:tuple(sum(entries[c][r,s] for r,s in u) for u in uses) for c in ids}
    ps=defaultdict(list);ts=defaultdict(list)
    for c in ids:ps[P[c]].append(c);ts[T[c]].append(c)
    eqp=sum(len(a)*(len(a)-1)//2 for a in ps.values())
    eqt=sum(len(a)*(len(a)-1)//2 for a in ts.values())
    assert eqp==eqt
    prof_reps=list(next(iter(a)) for a in ps.values())
    # One bit for each pair of distinct root profiles that one assignment does not separate.
    costs=[T[c] for c in prof_reps]
    pairs=list(itertools.combinations(range(len(prof_reps)),2))
    masks=[]
    for j in range(len(allocs)):
        masks.append(sum(1<<k for k,(a,b) in enumerate(pairs) if costs[a][j]==costs[b][j]))
    uniq=list(dict.fromkeys(masks))
    assert 0 not in uniq
    two=any((a&b)==0 for i,a in enumerate(uniq) for b in uniq[i+1:])
    if rep in (14300,14313):
        assert len(ps)==29 and two
        chosen=(0,329) if rep==14300 else (0,277)
        assert masks[chosen[0]]&masks[chosen[1]]==0
        sparse="optimal 2"
    else:
        assert len(ps)==40 and not two and len(uniq)==425
        # Exhaustively test 12,704,100 triples of distinct pair-collision masks.
        assert not any((a&b&c)==0 for i,a in enumerate(uniq)
                       for j,b in enumerate(uniq[i+1:],i+1) for c in uniq[j+1:])
        chosen=(78,99,226,2,63) if rep==14304 else (119,153,237,6,135)
        z=(1<<len(pairs))-1
        for j in chosen:z&=masks[j]
        assert z==0
        sparse="4 <= minimum <= 5"
    row=(rep,len(ids),nc,len(allocs),len(ps),len(ts),eqp,eqt,sparse)
    summary.append(row)
    print("VERIFIED",row,flush=True)
print("ALL FOUR COMPLETE; 48,600 rooted costs; 129,600 terminal totals; 11,100 pairs; 1,296 independent native Trie root costs",flush=True)
