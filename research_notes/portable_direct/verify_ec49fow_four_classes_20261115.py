#!/usr/bin/env python3
"""EC49FOW exact census checker (stdlib only). Usage:
python verify_ec49fow.py frozen_original_master.txt CLASS_{33,94,108,112}_PROFILES.csv

The upstream Trie cost generator and independent Python root checks are preserved
in the full EC49FOW evidence package. This checks complete named eligibility,
every rooted subset row, complete terminal sums and finite observer sufficiency.
"""
import collections, csv, hashlib, itertools, json, math, pathlib, sys

ROOTS=(3,5,6,7)
REPS=(33,94,108,112)
EXPECTED={
33:(206,304,1296,136,884,"19fb4176c84219d28edb920d1a18d90c919a40e6ccab99a8d7fbab3a54b3e35c",(587,1272,745,205,356,1263,8)),
94:(119,284,384,73,470,"7221fd7148e7f368e8432ee8269feec42a666c076854b6d713b2d31aeb8f1c7c",(267,148,222,26,9)),
108:(158,296,864,70,1864,"cbd185d794a27de7a2b280377bd8571f2e0c75f6e468c4fcaca18724b7cfccfc",(168,522,5,324)),
112:(158,296,864,70,1864,"51865d0a4fc16bb9edb31939dc22f93953fb927afbafd8b8f104a45464e97fb2",(164,351,7,486)),
}

def parse_frozen(path):
    assert hashlib.sha256(path.read_bytes()).hexdigest()=="cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
    with path.open() as f:
        nkeys,nwords,ncases=map(int,f.readline().split())
        assert (nkeys,nwords,ncases)==(94,178850,38169)
        fam=[]
        count=0
        for _ in range(nkeys):
            n=int(f.readline());count+=n
            m=[0]*4
            for _ in range(n):
                label,code=f.readline().split()
                label=int(label);root=int(code[:2],16)
                assert 0<=label<24 and root in ROOTS
                m[ROOTS.index(root)] |= 1<<label
            fam.append(m)
        assert count==nwords
        cases=[tuple(map(int,f.readline().split())) for _ in range(ncases)]
    assert all(len(x)==7 and all(0<=k<94 for k in x) for x in cases)
    return fam,cases

def signature(case,fam):
    dom=[0]*24
    for k in case:
        for j,mask in enumerate(fam[k]):
            while mask:
                bit=mask&-mask
                dom[bit.bit_length()-1]|=1<<j
                mask-=bit
    assert all(dom)
    return tuple(dom)

def verify(rep,fam,cases,groups,path):
    n,coords,na,ng,eq,sha,observers=EXPECTED[rep]
    assert hashlib.sha256(path.read_bytes()).hexdigest()==sha
    dom=signature(cases[rep],fam)
    ids=groups[dom]
    assert len(ids)==n and ids[0]==rep
    optional=[l for l,d in enumerate(dom) if d.bit_count()>1]
    choices=[tuple(ROOTS[j] for j in range(4) if dom[l]>>j&1) for l in optional]
    alloc=list(itertools.product(*choices))
    assert len(alloc)==na
    rooted=collections.defaultdict(dict)
    for row in csv.DictReader(path.open(newline="")):
        c,r,m,o,s,v=(int(row[k]) for k in ("config","root","must","opt","subset","cost"))
        assert c in ids and r in ROOTS and v>=0
        j=ROOTS.index(r)
        assert m==sum(1<<l for l,d in enumerate(dom) if d==1<<j)
        assert o==sum(1<<l for l,d in enumerate(dom) if d.bit_count()>1 and d>>j&1)
        assert (s & ~o)==0 and (r,s) not in rooted[c]
        rooted[c][r,s]=v
    assert set(rooted)==set(ids)
    P=collections.defaultdict(list); T=collections.defaultdict(list); O=collections.defaultdict(list)
    for c in ids:
        assert len(rooted[c])==coords
        p=tuple(rooted[c][r,s] for r in ROOTS for s in sorted(x for rr,x in rooted[c] if rr==r))
        term=[]
        for a in alloc:
            masks={r:0 for r in ROOTS}
            for l,r in zip(optional,a): masks[r]|=1<<l
            term.append(sum(rooted[c][r,masks[r]] for r in ROOTS))
        assert len(term)==na
        P[p].append(c)
        T[tuple(term)].append(c)
        O[tuple(term[i] for i in observers)].append(c)
    pairs=lambda partition:sum(len(v)*(len(v)-1)//2 for v in partition.values())
    assert len(P)==len(T)==len(O)==ng and pairs(P)==pairs(T)==pairs(O)==eq
    print(json.dumps({"rep":rep,"configs":n,"root_coordinates":n*coords,
                      "terminal_evaluations":n*na,"root_classes":ng,
                      "terminal_classes":len(T),"observer_count":len(observers),
                      "equal_unordered_pairs":eq,"nonzero_gauges":pairs(T)-pairs(P)}))

if __name__=="__main__":
    assert len(sys.argv)==6,"Need frozen input and exactly four profile CSVs"
    fam,cases=parse_frozen(pathlib.Path(sys.argv[1]))
    groups=collections.defaultdict(list)
    for i,c in enumerate(cases): groups[signature(c,fam)].append(i)
    assert len(groups)==625
    for rep,p in zip(REPS,sys.argv[2:]): verify(rep,fam,cases,groups,pathlib.Path(p))
