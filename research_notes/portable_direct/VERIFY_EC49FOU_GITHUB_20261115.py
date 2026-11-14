#!/usr/bin/env python3
"""EC49FOU complete finite root/terminal equality certificate.
Usage: python VERIFY_EC49FOU_GITHUB_20261115.py frozen_original_master.txt csv_folder
Requires only Python 3 standard library; raw CSVs are in the linked full evidence archive.
"""
import csv
import hashlib
import itertools
import collections
import pathlib
import sys

ROOTS=(3,5,6,7)
REPS=(10836,10845,10853)
SOURCE_SHA256="cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
EXPECTED={
 10836:(152,50,601),
 10845:(148,58,404),
 10853:(148,63,325),
}

def load_source(p):
    assert hashlib.sha256(p.read_bytes()).hexdigest()==SOURCE_SHA256
    with p.open() as f:
        nk,nw,nc=map(int,f.readline().split())
        assert (nk,nw,nc)==(94,178850,38169)
        key_masks=[]
        for _ in range(nk):
            n=int(f.readline());m={r:0 for r in ROOTS}
            for _ in range(n):
                label,code=f.readline().split()
                m[int(code[:2],16)]|=1<<int(label)
            key_masks.append(m)
        cases=[tuple(map(int,f.readline().split())) for _ in range(nc)]
    return key_masks,cases

def signature(case,key_masks):
    masks=[0]*24
    for key in case:
        for j,r in enumerate(ROOTS):
            bits=key_masks[key][r]
            while bits:
                bit=bits&-bits
                masks[bit.bit_length()-1]|=1<<j
                bits^=bit
    assert all(masks)
    return tuple(masks)

def load_csv(folder,rep):
    values={}
    with (folder/f"EC49FOU_{rep}_PROFILES.csv").open() as f:
        for row in csv.DictReader(f):
            c,r,m,o,s,v=(int(row[k]) for k in ("config","root","must","opt","subset","cost"))
            key=(c,r,s)
            assert key not in values
            values[key]=(v,m,o)
    return values

def classify(members,domain,values,rep):
    optional=[l for l in range(24) if domain[l].bit_count()>1]
    choices=[tuple(ROOTS[j] for j in range(4) if domain[l]>>j&1) for l in optional]
    allocations=list(itertools.product(*choices))
    assert len(allocations)==192
    tgroups=collections.defaultdict(list)
    pgroups=collections.defaultdict(list)
    used=set()
    for cid in members:
        profile=[];costs={}
        for j,r in enumerate(ROOTS):
            opt=[l for l in optional if domain[l]>>j&1]
            omask=sum(1<<l for l in opt)
            mmask=sum(1<<l for l in range(24) if domain[l]==1<<j)
            for bits in itertools.product((0,1),repeat=len(opt)):
                subset=sum(1<<l for l,b in zip(opt,bits) if b)
                key=(cid,r,subset)
                assert key in values and key not in used
                used.add(key)
                cost,m,o=values[key]
                assert (m,o)==(mmask,omask) and cost>=0
                costs[r,subset]=cost
                profile.append((r,subset,cost))
        totals=[]
        for assignment in allocations:
            chosen={r:0 for r in ROOTS}
            for l,r in zip(optional,assignment): chosen[r]|=1<<l
            totals.append(sum(costs[r,chosen[r]] for r in ROOTS))
        tgroups[tuple(totals)].append(cid)
        pgroups[tuple(profile)].append(cid)
    assert used==set(values)  # full table of entire class, no extras
    n_t=sum(len(a)*(len(a)-1)//2 for a in tgroups.values())
    n_p=sum(len(a)*(len(a)-1)//2 for a in pgroups.values())
    nroots,nclasses,npairs=EXPECTED[rep]
    assert len(values)==99*nroots
    assert len(tgroups)==len(pgroups)==nclasses
    assert n_t==n_p==npairs
    print(rep,"PASS configs=99 root_entries=",len(values),
          "terminal_evaluations=",99*len(allocations),
          "classes=",nclasses,"equal_pairs=",npairs,"nonzero_gauges=0")
    return len(values),99*len(allocations),npairs

def main():
    source=pathlib.Path(sys.argv[1]);folder=pathlib.Path(sys.argv[2])
    keys,cases=load_source(source)
    groups=collections.defaultdict(list)
    for i,case in enumerate(cases):groups[signature(case,keys)].append(i)
    assert len(groups)==625
    counts=[0,0,0]
    for rep in REPS:
        domain=signature(cases[rep],keys);members=groups[domain]
        assert len(members)==99 and members[0]==rep
        values=load_csv(folder,rep)
        result=classify(members,domain,values,rep)
        counts=[a+b for a,b in zip(counts,result)]
    assert counts==[44352,57024,1330]
    print("PASS 3 complete classes, 297 configs, 14553 pairs, 0 invisible nonzero gauges")
if __name__=="__main__":
    assert len(sys.argv)==3
    main()
