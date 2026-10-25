#!/usr/bin/env python3
"""C298 exact 125-strip shared denominator and dyadic termination replay.
Frozen positive-rational C195/H168 auxiliary, no native BRC transfer or admission.
Run beside C275, C284, C288, C293 and C297 frozen source files.
"""
import json,hashlib
from math import gcd,lcm
from functools import reduce
from collections import Counter
from pathlib import Path
from fractions import Fraction as F
import C275_STANDALONE_EXACT_REPLAY as s
import C288_ISOLATING_BOXES_EXACT as r
from C297_UNIFORM_WIDTH_AND_HEIGHT_EXACT import poly_mul,poly_add,poly_eval,normalize_pair

def basis(n,d,a,b):
    n,d=normalize_pair(n,d)
    if poly_eval(d,a)<0:d=[-x for x in d]  # original denominator is absolute gap
    assert all(poly_eval(p,t)>0 for p in (n,d) for t in (a,b))
    return n,d

def primitive(d):
    while len(d)>1 and d[-1]==0:d=d[:-1]
    c=reduce(gcd,map(abs,d))
    return c,tuple(x//c for x in d)

def terms(path,a,b,W):
    w,d=path['w'],path['d']; ans=[]
    anchor=F(1)
    for k in s.I:anchor*=s.Z-s.U[k]
    for j in s.J:
        c=F(W[j],s.Q)
        for k in s.I:c*=abs(s.U[j]-s.U[k])
        c/=anchor
        fac=[basis([s.Z-w[k],-d[k]],[s.U[j]-w[k],-d[k]],a,b) for k in range(4)]
        ans.append((c,fac))
    for k in range(4):
        p=[w[k],d[k]];p2=poly_mul(p,p)
        q=poly_mul(poly_add([F(2)],[-x for x in p2]),poly_add([F(3)],[-x for x in p2]))
        fac=[basis([s.A/s.H],poly_mul(poly_mul(q,q),q),a,b)]
        fac += [basis([s.Z-s.U[j]],[w[k]-s.U[j],d[k]],a,b) for j in s.J]
        fac += [basis([s.Z-w[m],-d[m]],[w[k]-w[m],d[k]-d[m]],a,b) for m in range(4) if m!=k]
        ans.append((F(1),fac))
    assert len(ans)==79
    return ans

def run():
    cert=json.loads(Path('C293_125_REFINED_BRACKETS.json').read_text())
    frozen=cert['records']
    assert len(frozen)==125
    assert hashlib.sha256(json.dumps(frozen,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()==cert['records_sha256']
    paths,_=r.build_paths();W,_=s.floor_fixed_masses()
    rows=[]; witnesses=[]
    for i,(row,path) in enumerate(zip(frozen,paths)):
        assert row[0]==i
        a=F(row[1],1<<24);b=F(row[1]+1,1<<24)
        groups=Counter();scalars=[]
        for c,fac in terms(path,a,b,W):
            own=Counter();scalar=c.denominator
            for num,den in fac:
                content,key=primitive(den)
                scalar*=content;own[key]+=1
                assert len(num)<=len(den)
            scalars.append(scalar)
            for key,exp in own.items():groups[key]=max(groups[key],exp)
        S=lcm(*scalars)
        assert all(S%x==0 for x in scalars)
        degree=sum((len(q)-1)*e for q,e in groups.items())
        M=S
        for q,e in groups.items():M*=sum(map(abs,q))**e
        H=M.bit_length()
        assert degree<=354 and H<=13799,(i,degree,H)
        rows.append([i,degree,H,len(groups),S.bit_length()])
        if i in [0,8,24,64,96,124]:
            k=2*int(row[1])+1;t=F(k,1<<25)
            v=tuple(x+t*y for x,y in zip(path['w'],path['d']))
            val=s.original_F(v,W)/s.Q
            den=F(S)
            for q,e in groups.items():den*=poly_eval(q,t)**e
            assert (den*val*(1<<(25*degree))).denominator==1
            witnesses.append(i)
    assert len(rows)==125 and sorted(witnesses)==[0,8,24,64,96,124]
    assert max(x[1] for x in rows)==354 and max(x[2] for x in rows)==13799
    assert Counter(x[1] for x in rows)==Counter({354:124,267:1})
    audit={'schema':'EM_C298_SHARED_DENOMINATOR_CERTIFICATE_V1',
           'source_C293_sha256':cert['records_sha256'],
           'source_C284_sha256':r.SOURCE_CERT_SHA,
           'model':'C195_H168_79_NODE_POSITIVE_RATIONAL_AUXILIARY',
           'paths':125,'degree_histogram':{'267':1,'354':124},
           'max_degree':354,'max_height_bits':13799,
           'old_precision':'P=660*b+73527+134',
           'new_precision':'P=354*b+13799+134',
           'six_full_fraction_integrality_witness_indices':witnesses,
           'source_status':'AUTHOR_ONLY_NO_CLAIM_NO_REVIEW_NOT_ADMITTED'}
    Path('C298_COMPACT_REPLAY_AUDIT.json').write_text(json.dumps(audit,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    Path('C298_COMPACT_REPLAY_ROWS.json').write_text(json.dumps(rows,separators=(',',':'))+'\n')
    print('C298_SHARED_DENOMINATOR_125_EXACT_PASS',json.dumps(audit,sort_keys=True))

if __name__=='__main__':run()
