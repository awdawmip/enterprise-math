#!/usr/bin/env python3
"""R284EY: exact integer verification of four-label one-change model.

The dynamic test checks all effective errors of Hamming weight <=u+q.
Each such effective error is realizable by a persistent mask of weight <=q
and an independent read mask of weight <=u; at most one change in the
persistent mask suffices to realize any two selected reads.
"""
import itertools, json
from pathlib import Path

def masks(n,rad):
    yield 0
    for j in range(1,rad+1):
        for comb in itertools.combinations(range(n),j):
            yield sum(1<<x for x in comb)

def codes_and_paths(v):
    if v == 0:
        codes=(0,1,3,2)
        paths=[(codes[i],codes[(i+1)%4]) for i in range(4)]
        return codes,paths,2
    a,b,c=v,3*v+1,v+1
    A=((1<<a)-1)
    B=((1<<b)-1)<<a
    C=((1<<c)-1)<<(a+b)
    codes=(0,B|C,A|C,A|B)
    paths=[]
    for i in range(4):
        bbits=list(range(a,a+b))
        if i%2==0:
            seq=bbits[:2*v]
            for z,t in zip(range(a+b,a+b+c),bbits[2*v:]):
                seq.extend([z,t])
        else:
            seq=bbits[:2*v+1]
            for z,t in zip(range(a),bbits[2*v+1:]):
                seq.extend([z,t])
        x=codes[i]
        row=[x]
        for bit in seq:
            x^=1<<bit
            row.append(x)
        assert x==codes[(i+1)%4]
        assert len(seq)==(codes[i]^codes[(i+1)%4]).bit_count()
        paths.append(tuple(row))
    return codes,paths,a+b+c

def split_error(mask,q,u):
    bits=[j for j in range(mask.bit_length()) if mask>>j & 1]
    F=sum(1<<x for x in bits[:q])
    R=mask^F
    assert F.bit_count()<=q and R.bit_count()<=u
    return F,R

def boundary(u,q):
    v=u+q
    if not v:
        return {"u":u,"q":q,"edge_distance":0,"obstruction":"distinct stable labels"}
    d=4*v
    j=2*v
    x=(1<<j)-1
    a=0
    b=(1<<d)-1
    toward_new=sum(1<<p for p in range(j,j+v))
    toward_old=sum(1<<p for p in range(v,j))
    f1,r1=split_error(toward_new,q,u)
    f2,r2=split_error(toward_old,q,u)
    y1=x^f1^r1
    y2=x^f2^r2
    assert (x^b).bit_count()==2*v and (x^a).bit_count()==2*v
    assert (y1^b).bit_count()==v and (y2^a).bit_count()==v
    assert f1.bit_count()<=q and f2.bit_count()<=q
    assert r1.bit_count()<=u and r2.bit_count()<=u
    return {"u":u,"q":q,"edge_distance":d,"same_prefix_index":j,
            "old":hex(a),"new":hex(b),"prefix":hex(x),
            "first_mask":hex(f1),"first_read_error":hex(r1),"read_new":hex(y1),
            "second_mask":hex(f2),"second_read_error":hex(r2),"read_old":hex(y2),
            "mask_changes":int(f1!=f2),"result":"NEW_THEN_OLD"}

def test(u,q):
    v=u+q
    codes,paths,n=codes_and_paths(v)
    masks_all=list(masks(n,v))
    assert n==5*v+2
    assert len(set(codes))==4
    assert min((codes[i]^codes[j]).bit_count() for i in range(4) for j in range(i))>=2*v+1
    checked=0
    for i,ps in enumerate(paths):
        seen_new=False
        for k,p in enumerate(ps):
            for err in masks_all:
                y=p^err
                matches=[j for j,c in enumerate(codes) if (c^y).bit_count()<=v]
                assert len(matches)<=1
                dec=matches[0] if matches else None
                assert dec in (None,i,(i+1)%4),(u,q,i,k,dec)
                if k==0: assert dec==i
                if k==len(ps)-1: assert dec==(i+1)%4
                if dec==i: assert not seen_new,(u,q,i,k,err)
                if dec==(i+1)%4: seen_new=True
                checked+=1
    return {"u":u,"q":q,"v":v,"n":n,"paths_prefix_states":sum(map(len,paths)),"admissible_effective_masks":len(masks_all),"exact_reads":checked,"result":"PASS"}

if __name__=='__main__':
    cases=[test(u,q) for u in range(3) for q in range(3)]
    witnesses=[boundary(u,q) for u in range(3) for q in range(3)]
    cert={"record":"R284EY_ONE_ARBITRARY_MASK_CHANGE_4TAG",
          "model":"one arbitrary change F_before -> F_after between any two observations, wt(F_before),wt(F_after)<=q; each read has independent <=u flips; output unique radius-(u+q) endpoint or RETRY; writer may pause at prefixes",
          "result":"n_min=5*(u+q)+2 for nonnegative integers u,q; unrestricted single-change mask",
          "cases":cases,"sharp_edge_witnesses":witnesses,
          "proof_scope":"General integer proof in R284EY theorem note; finite exact checks only for u,q in {0,1,2}",
          "review":"NOT_REVIEWED"}
    p=Path('/mnt/data/R284EY_one_mask_change_certificate.json')
    p.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({"total_reads":sum(t['exact_reads'] for t in cases),"cases":cases,"certificate":str(p)},ensure_ascii=False))
