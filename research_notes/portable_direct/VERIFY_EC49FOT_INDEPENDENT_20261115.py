#!/usr/bin/env python3
"""EC49FOT independent exact byte-Trie verifier for four native gauges.

Usage: python3 VERIFY_EC49FOT_INDEPENDENT.py ORIGINAL_INPUT
Original frozen file SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e
The file is parsed independently from the C++ root-cost CSV.
"""
import hashlib
import itertools
from pathlib import Path
import sys

PIN = "cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
ROOTS = (3,5,6,7)
WITNESSES = (
 (17741,31699,(0,-4,4,0),None),
 (24354,31700,(0,-2,2,0),None),
 (16786,19592,None,"06_17"),
 (20706,35148,None,"05_15"),
)

class Node:
    def __init__(self):
        self.children={}
        self.labels=0

def rooted_table(case,words,root):
    items=[(lab,code[1:]) for key in case for lab,code in words[key] if code[0]==root]
    labels=sorted({lab for lab,_ in items})
    bits={lab:1<<index for index,lab in enumerate(labels)}
    head=Node()
    for lab,suffix in items:
        u=head
        for char in suffix:
            u=u.children.setdefault(char,Node())
        u.labels|=bits[lab]
    def visit(u):
        state={0:0}
        if u.labels:state[u.labels]=0
        for _,child in sorted(u.children.items()):
            other=visit(child)
            merged={}
            for left,a in state.items():
                for right,b in other.items():
                    mask=left|right
                    cost=a+b
                    if cost<merged.get(mask,10**9):merged[mask]=cost
            state=merged
        return {mask:cost+(mask!=0) for mask,cost in state.items()}
    exact=visit(head)
    costs=[10**9]*(1<<len(labels))
    for mask,cost in exact.items():costs[mask]=cost
    for j in range(len(labels)):
        for mask in range(len(costs)):
            if mask&(1<<j)==0:costs[mask]=min(costs[mask],costs[mask|(1<<j)])
    return labels,costs

def profile(case,words):
    tables={r:rooted_table(case,words,r) for r in ROOTS}
    eligible={lab:tuple(r for r in ROOTS if lab in tables[r][0]) for lab in range(24)}
    assert all(eligible.values())
    optional={lab:roots for lab,roots in eligible.items() if len(roots)>1}
    result={}
    for r,(labels,costs) in tables.items():
        local={lab:1<<j for j,lab in enumerate(labels)}
        required=[lab for lab in labels if len(eligible[lab])==1]
        free=[lab for lab in labels if len(eligible[lab])>1]
        for flags in itertools.product((0,1),repeat=len(free)):
            chosen=required+[lab for lab,yes in zip(free,flags) if yes]
            mask=sum(local[lab] for lab in chosen)
            named=sum(1<<lab for lab,yes in zip(free,flags) if yes)
            result[r,named]=costs[mask]
    return result,optional

def main(path):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==PIN,"frozen source mismatch"
    with Path(path).open() as f:
        nk,nw,nc=map(int,f.readline().split())
        assert (nk,nw,nc)==(94,178850,38169)
        words=[]
        for _ in range(nk):
            n=int(f.readline())
            family=[]
            for j in range(n):
                lab,code=f.readline().split()
                family.append((int(lab),bytes.fromhex(code)))
            words.append(family)
        cases=[tuple(map(int,f.readline().split())) for _ in range(nc)]
    for a,b,constants,kind in WITNESSES:
        old,eo=profile(cases[a],words)
        new,en=profile(cases[b],words)
        assert eo==en and set(old)==set(new)
        delta={(r,s):new[r,s]-v for (r,s),v in old.items()}
        if constants is not None:
            for r,c in zip(ROOTS,constants):
                assert all(v==c for (root,_),v in delta.items() if root==r)
        elif kind=="06_17":
            assert {(s):v for (r,s),v in delta.items() if r==6 and v}=={1<<17:1}
            affected={sum(1<<lab for lab in [7,13,21]+list(extra))
                      for extra in ((),(5,),(15,),(5,15))}
            assert {s:v for (r,s),v in delta.items() if r==7 and v}=={s:-1 for s in affected}
            assert all(v==0 for (r,s),v in delta.items() if r in (3,5))
        elif kind=="05_15":
            assert {s:v for (r,s),v in delta.items() if r==5 and v}=={1<<15:1}
            affected={sum(1<<lab for lab in [5,11,19]+list(extra))
                      for extra in ((),(7,),(17,),(7,17))}
            assert {s:v for (r,s),v in delta.items() if r==7 and v}=={s:-1 for s in affected}
            assert all(v==0 for (r,s),v in delta.items() if r in (3,6))
        else:raise AssertionError(kind)
        count=0
        nonzero=0
        optional=sorted(eo)
        for chosen in itertools.product(*(eo[lab] for lab in optional)):
            mask={r:0 for r in ROOTS}
            for lab,r in zip(optional,chosen):mask[r]|=1<<lab
            assert sum(old[r,mask[r]] for r in ROOTS)==sum(new[r,mask[r]] for r in ROOTS)
            components=tuple(delta[r,mask[r]] for r in ROOTS)
            assert sum(components)==0
            count+=1
            if any(components):nonzero+=1
        if kind:assert (count,nonzero)==(64,4)
        else:assert (count,nonzero)==(256,256)
        print("PASS",a,b,"rooted_entries",len(old),"allocations",count,
              "component_cancellation_allocations",nonzero)
    print("PASS four original-corpus gauges, 640 exact legal allocations")

if __name__=="__main__":
    assert len(sys.argv)==2
    main(sys.argv[1])
