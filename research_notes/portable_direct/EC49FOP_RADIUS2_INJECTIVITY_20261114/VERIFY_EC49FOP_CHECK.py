#!/usr/bin/env python3
"""EC49FOP finite original corpus and native-prefix profile observer check (exact integers)."""
import csv, itertools, sys, hashlib, collections, json
from pathlib import Path
R=(3,5,6,7)
E={5:(5,7),7:(6,7),13:(6,7),15:(3,5,7),17:(3,6,7),19:(3,5,7),21:(3,6,7)}
def load(path):
    f=open(path); k,w,n=map(int,f.readline().split())
    assert (k,w,n)==(94,178850,38169)
    keyroots=[]
    for _ in range(k):
        d={r:set() for r in R}
        for j in range(int(f.readline())):
            label,word=f.readline().split()
            rr=int(word[:2],16);assert rr in R
            d[rr].add(int(label))
        keyroots.append(d)
    cases=[tuple(map(int,f.readline().split())) for _ in range(n)]
    assert len(set(cases))==n
    assert all(len(c)==7 and len(set(c))==7 for c in cases)
    return keyroots,cases
def legal(case,keyroots):
    e=[0]*24
    for key in case:
        for r,labs in keyroots[key].items():
            for l in labs:e[l]|=1<<R.index(r)
    assert all(e)
    return tuple(e)
def select(cases,keyroots):
    base=set(cases[32315]);dom=legal(base,keyroots);ids=[];hist=collections.Counter()
    all_domains=set()
    for i,c in enumerate(cases):
        d=legal(c,keyroots);all_domains.add(d)
        radius=len(base-set(c))
        if radius<=2 and d==dom:
            ids.append(i);hist[radius]+=1
    assert len(all_domains)==625
    assert len(ids)==411 and dict(hist)=={0:1,1:73,2:337}
    return ids,dom
def cost_tables(path,ids):
    table=collections.defaultdict(dict);metadata={}
    with open(path) as f:
        for row in csv.DictReader(f):
            i,r=map(int,(row["config"],row["root"]))
            m,o,s,c=map(int,(row["must"],row["opt"],row["subset"],row["cost"]))
            assert i in ids and r in R and (r,s) not in table[i]
            table[i][(r,s)]=c
            if (i,r) in metadata:assert metadata[(i,r)]==(m,o)
            metadata[(i,r)]=(m,o)
    assert set(table)==set(ids)
    for i in ids:
        for r in R:
            m,o=metadata[(i,r)]
            assert set(s for rr,s in table[i] if rr==r)==set(
                sum(1<<l for j,l in enumerate([l for l in range(24) if (o>>l)&1]) if (b>>j)&1)
                for b in range(1<<o.bit_count()))
    return table,metadata
def verify(original,csvfile):
    inp=Path(original).read_bytes()
    assert hashlib.sha256(inp).hexdigest()=="cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
    keyroots,cases=load(original)
    ids,dom=select(cases,keyroots)
    assert len(tuple(open(Path(csvfile).with_name("EC49FOP_IDS.txt"))))==411
    assert [int(x) for x in open(Path(csvfile).with_name("EC49FOP_IDS.txt"))]==ids
    assert all(legal(cases[i],keyroots)==dom for i in ids)
    table,meta=cost_tables(csvfile,ids)
    full=[]
    for rr in itertools.product(*(E[l] for l in E)):
        rho=dict(zip(E,rr))
        full.append(tuple(sum(1<<l for l,v in rho.items() if v==r) for r in R))
    assert len(full)==648
    terms=collections.defaultdict(list);profiles=collections.defaultdict(list)
    for i in ids:
        p=tuple((r,s,c) for (r,s),c in sorted(table[i].items()))
        t=tuple(sum(table[i][(r,m)] for r,m in zip(R,x)) for x in full)
        profiles[p].append(i);terms[t].append(i)
    pairs=lambda groups:sum(len(v)*(len(v)-1)//2 for v in groups.values())
    pcount=pairs(profiles);tcount=pairs(terms)
    assert len(terms)==len(profiles)==178 and pcount==tcount==4068
    collisions=[]
    pv={i:tuple((r,s,c) for (r,s),c in sorted(table[i].items())) for i in ids}
    for group in terms.values():
        if len({pv[i] for i in group})!=1:collisions.append(group)
    assert not collisions
    b=[g for g in terms.values() if 32315 in g][0]
    assert len(b)==38
    result={"schema":"EC49FOP_FROZEN_TWO_KEY_OBSERVER_CENSUS_V1",
        "science_pin":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
        "all_corpus_cases":len(cases),"all_legal_domains":625,
        "selected_cases":len(ids),"selected_by_radius":[1,73,337],
        "assignments_per_case":len(full),"root_entries":sum(len(table[i]) for i in ids),
        "same_domain_pairs":len(ids)*(len(ids)-1)//2,
        "terminal_classes":len(terms),"profile_classes":len(profiles),
        "terminal_equal_pairs":tcount,"profile_equal_pairs":pcount,
        "nonzero_invisible_gauge_pairs":0,"baseline_equivalent_cases":len(b),
        "mathematics":"EXACT_FINITE_CHECKED_NOT_REVIEWED"}
    print(json.dumps(result,sort_keys=True,indent=2))
    return result
if __name__=="__main__":
    if len(sys.argv)<3:
        print("usage: VERIFY_EC49FOP_CHECK.py [--select-only] ORIGINAL [EXACT_PROFILES.csv]",file=sys.stderr)
        sys.exit(2)
    if sys.argv[1]=="--select-only":
        keyroots,cases=load(sys.argv[2]);ids,dom=select(cases,keyroots)
        Path("EC49FOP_IDS.txt").write_text("".join(str(i)+"\n" for i in ids))
        print("SELECT_EXACT_PASS",len(ids))
    else:
        verify(sys.argv[1],sys.argv[2])
