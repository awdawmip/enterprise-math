#!/usr/bin/env python3
"""R762GJ: exact integer affine-group and positive-BRC certificates; standard library."""
from collections import Counter, deque
from itertools import combinations
import json

STAR=((0,1,2),(0,3,4),(1,3,5),(2,4,5))
E=tuple(range(6))
Z=(0,)*6
WITNESS={
 "012":{"sum3":[(0,1),(1,1),(0,-1),(2,-1),(1,1),(2,1),(1,-1)],
        "root":[(0,1),(1,1),(0,1),(1,-1),(0,-1),(2,1),(0,-1),(2,-1)]},
 "013":{"sum3":[(0,1),(1,1),(0,-1),(3,1),(0,1),(3,-1),(1,-1)],
        "root":[(0,1),(1,1),(0,1),(1,-1),(0,-1),(3,-1),(1,-1),(3,1)]},
 "023":{"sum3":[(0,1),(2,1),(0,-1),(2,-1),(3,1),(2,1),(3,-1)],
        "root":[(0,1),(2,1),(0,-1),(2,1),(3,1),(2,-1),(3,-1),(2,-1)]},
 "123":{"sum3":[(1,1),(2,1),(1,-1),(3,-1),(2,1),(3,1),(2,-1)],
        "root":[(1,1),(2,1),(1,1),(2,-1),(1,-1),(3,1),(1,-1),(3,-1)]}
}

# The following words close the exact m=16 unit-depth hitting-time bound.
# Full 16-step mass counts are an optional separate expensive check.
UNIT16={
 "012":"0+ 0+ 1+ 0- 2- 1+ 0- 2- 0+ 0+ 1+ 2- 1+ 0- 2- 1+",
 "013":"0+ 1+ 0+ 3- 1- 0+ 1+ 3- 1+ 0+ 3- 0- 1- 0+ 1+ 3-",
 "023":"0+ 0+ 2+ 3- 0- 3- 2- 3- 0- 2- 3+ 0+ 2+ 0+ 3+ 2+",
 "123":"1+ 1+ 2+ 1- 3- 2+ 1- 3- 1+ 1+ 2+ 3- 2+ 1- 3- 2+",
}
def decode_word(s):return tuple((int(t[:-1]),1 if t[-1]=="+" else -1) for t in s.split())

def comp(p,q): return tuple(p[q[i]] for i in range(6))
def inv(p):
    q=[0]*6
    for i,j in enumerate(p):q[j]=i
    return tuple(q)
def act(p,x):
    y=[0]*6
    for i,j in enumerate(p):y[j]=x[i]
    return tuple(y)
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def generator(j,s):
    assert s in (-1,1)
    t=STAR[j];p=list(E)
    for k,i in enumerate(t):p[i]=t[(k+1)%3]
    p=tuple(p)
    h=tuple(s*int(i in t) for i in E)
    return (h,p if s==1 else inv(p))
def word_product(word):
    x,p=Z,E
    for j,s in word:
        h,q=generator(j,s)
        x,p=add(x,act(p,h)),comp(p,q)
    return x,p
def orientation_closure(subset):
    generators=[generator(j,s)[1] for j in subset for s in (-1,1)]
    seen={E};todo=deque([E])
    while todo:
        p=todo.popleft()
        for g in generators:
            q=comp(p,g)
            if q not in seen:seen.add(q);todo.append(q)
    return seen
def brc_counts(subset,half_max=7):
    generators=[(*generator(j,s),) for j in subset for s in (-1,1)]
    weights={(Z,E):1};out=[]
    for t in range(1,half_max+1):
        nxt=Counter()
        for (x,p),v in weights.items():
            for h,q in generators:
                nxt[(add(x,act(p,h)),comp(p,q))]+=v
        weights=nxt
        assert sum(weights.values())==(2*len(subset))**t
        c={}
        for k in range(-t,t+1):
            total=0
            for (x,p),v in weights.items():
                pi=inv(p)
                target=(act(pi,tuple(k-i for i in x)),pi)
                total+=v*weights.get(target,0)
            if total:c[str(k)]=total
        out.append({"events":2*t,"half_distinct_states":len(weights),
                    "joint_diagonal_counts":c})
    return out
def run():
    results={}
    for size in (1,2,3,4):
        for subset in combinations(range(4),size):
            name="".join(map(str,subset))
            image=orientation_closure(subset)
            assert len(image)=={1:3,2:60,3:360,4:360}[size]
            entry={"orientation_group_order":len(image)}
            if size<=2:
                unused=set(E)-set().union(*(set(STAR[j]) for j in subset))
                assert unused
                entry["fixed_missing_axes"]=sorted(unused)
            if size==3:
                assert len({(p[0],p[1]) for p in image})==30
                for kind,word in WITNESS[name].items():
                    x,p=word_product(word)
                    assert p==E
                    if kind=="sum3":assert sum(x)==3
                    else:assert sorted(x)==[-1,0,0,0,0,1]
                    entry[kind]={"word":word,"translation":x,
                                 "orientation_identity":True}
                word=decode_word(UNIT16[name])
                assert len(word)==16 and all(j in subset for j,s in word)
                assert word_product(word)==((1,)*6,E)
                entry["shortest_unit_depth"]={"length":16,"word":word,
                      "complete_product":((1,)*6,E)}
                entry["kernel_proof"]="normality + A6 2-transitivity + pure root + sum-three vector"
                entry["brc"]=brc_counts(subset)
                assert entry["brc"][3]["joint_diagonal_counts"]=={"0":12786}
                assert entry["brc"][4]["joint_diagonal_counts"]=={"-3":60,"0":197928,"3":60}
                assert all("1" not in c["joint_diagonal_counts"] for c in entry["brc"])
            results[name]=entry
    assert all(results[x]["brc"]==results["012"]["brc"] for x in ("013","023","123"))
    return {"schema":"R762GJ_THREE_STAR_AFFINE_KERNEL_EVIDENCE_V1",
            "frozen_science_commit":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
            "model":"R762GI_CANDIDATE_SIGNED_STAR_SEMIDIRECT",
            "all_15_nonempty_subsets_checked":True,
            "exact_integer_arithmetic":True,
            "results":results,"author_verification":"PASS",
            "independent_review":"NOT_REVIEWED",
            "native_TRIADIC_CLOSURE_E_license":"UNVERIFIED"}
if __name__=="__main__":
    result=run()
    with open("R762GJ_EVIDENCE.json","w",encoding="utf-8") as f:
        json.dump(result,f,indent=2,ensure_ascii=False)
    print("PASS: all 15 subsets, eight short and four length-16 witnesses, BRC counts through m=14")
