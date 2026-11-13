#!/usr/bin/env python3
"""Independent exact whole-box audit of Stage376 and Stage377 certificates.

Input CSVs are existing immutable attached artifacts, checked by SHA256.
No import from their generators. Rational signed support and 4D enclosures
are reconstructed directly from the frozen labelled Bernoulli definitions.
Run: python REPRO_STAGE385B_INDEPENDENT.py STAGE377.csv STAGE376.csv
"""
from __future__ import annotations
import csv
import hashlib
import json
import sys
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

COEFFS=((Q(1),Q(-3),Q(3),Q(-1)),(Q(0),Q(1),Q(-2),Q(1)),
        (Q(0),Q(0),Q(1),Q(-1)),(Q(0),Q(0),Q(0),Q(1)))
W=(1,3,3,1); M=(61,21,9,9)
E=Q(11,5000)
P=(Q(577,2500),Q(469,2000),Q(11,20),Q(14,25))
Q377=(Q(473,2000),Q(239,1000),Q(143,250),Q(1439,2500))
R376=P+(Q(473,2000),Q(239,1000),Q(72,125),Q(2897,5000))
BUP377=Q(97582683,10**10)
BUP376=Q(61,6250)
C377=Q(16174336378406867755705673,256000000000000000000000000)
C376=Q(16174439790495832521,256000000000000000000)
LAM377=Q(97,80);LAM376=Q(13,10)
TARGET377={'P':Q(3753605,10**8),'Q':Q(3747692,10**8)}
REF377=((Q(23113910,10**8),Q(55568442,10**8)),
        (Q(23780690,10**8),Q(57569391,10**8)))
REF376=((Q(231138,10**6),Q(555681,10**6)),
        (Q(237807,10**6),Q(575694,10**6)))
SHA377='bcb2b5b8ba4f07288fc462de02ce7cb4873fce84734c1015433beac0e33338c3'
SHA376='5f0452e3b8488d7a843233c0c12f5f6b2cc9cf6916a38e8f5cbdf143b9bfb8ac'

@lru_cache(None)
def B(k,z):
    a=COEFFS[k]
    return ((a[3]*z+a[2])*z+a[1])*z+a[0]

def db(k,z):
    a=COEFFS[k]
    return (3*a[3]*z+2*a[2])*z+a[1]

def r(k,x,y):
    return (4*B(k,x)+B(k,y))/5-Q(M[k],160)

def bc(x,y):
    res=Q(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))
    audit=Q(0)
    for z,a,mult in ((x,Q(1,4),63),(x,Q(3,4),1),
                     (y,Q(1,4),9),(y,Q(3,4),7)):
        for k in range(4):
            audit+=Q(mult*W[k],512)*abs(B(k,z)-B(k,a))
    return res,audit

def check_root_and_reference():
    # New proof of each rational face inequality and monotonicity in the tiny boxes.
    xl,xu=Q(231083940,10**9),Q(231083942,10**9)
    yl,yu=Q(555508852,10**9),Q(555508864,10**9)
    assert r(0,xl,yu)>0>r(0,xu,yl)
    assert min(r(1,xl,yl),r(1,xu,yl))>0
    assert max(r(1,xl,yu),r(1,xu,yu))<0
    assert r(2,xl,yl)>0 and r(3,xu,yu)<0
    # r0 decreases in x and y; r1 increases in x, decreases in y;
    # r2 increases in each coordinate on this small rectangle.
    for z in (xl,xu):
        assert db(0,z)<0<db(1,z) and db(2,z)>0
    for z in (yl,yu):
        assert db(0,z)<0 and db(1,z)<0<db(2,z)
    beta_lower=Q(15,16)*r(2,xl,yl)
    beta_upper=Q(15,16)*r(2,xu,yu)
    assert 2*beta_upper+E<BUP377<BUP376
    results={}
    for name,points,C,BUP in [('377',REF377,C377,BUP377),('376',REF376,C376,BUP376)]:
        b0,c0=bc(*points[0]);b1,c1=bc(*points[1])
        assert c0+c1==C
        assert b0+b1<2*beta_lower+E
        assert 2*beta_upper+E<BUP
        results[name]={'reference_budget':str(b0+b1),'reference_variable_cost':str(c0+c1),
                       'strict_budget_slack_lower':str(2*beta_lower+E-(b0+b1))}
    return results, str(beta_lower),str(beta_upper)

def bernstein_floor(coeff,a,b):
    def f(z):return ((coeff[3]*z+coeff[2])*z+coeff[1])*z+coeff[0]
    def d(z):return (3*coeff[3]*z+2*coeff[2])*z+coeff[1]
    return min(f(a),f(a)+(b-a)*d(a)/3,f(b)-(b-a)*d(b)/3,f(b))

def signed_support_377(rect):
    xa,xb,ya,yb=rect
    cx,cy=(xa+xb)/2,(ya+yb)/2
    px=[Q(0)]*4;py=[Q(0)]*4;const=Q(0)
    def add(dst,k,factor):
        for i,v in enumerate(COEFFS[k]):dst[i]+=factor*v
    for k in range(4):
        w=W[k]
        rr=r(k,cx,cy)
        sr=(rr>0)-(rr<0)
        add(px,k,LAM377*Q(w*sr,8));add(py,k,LAM377*Q(w*sr,32))
        const-=LAM377*Q(w*M[k]*sr,1024)
        for z,a,mul,dst in ((cx,Q(1,4),63,px),(cx,Q(3,4),1,px),
                            (cy,Q(1,4),9,py),(cy,Q(3,4),7,py)):
            t=B(k,a)-B(k,z)
            st=(t>0)-(t<0)
            factor=Q(mul*w*st,512)
            add(dst,k,-factor)
            const+=factor*B(k,a)
    return const+bernstein_floor(px,xa,xb)+bernstein_floor(py,ya,yb)

def split_box(b):
    n=len(b)//2
    i=max(range(n),key=lambda k:b[2*k+1]-b[2*k])
    j=2*i;mid=(b[j]+b[j+1])/2
    zero=(*b[:j],b[j],mid,*b[j+2:])
    one=(*b[:j],mid,b[j+1],*b[j+2:])
    return zero,one

def validate_prefix_tree(paths):
    assert paths
    prefixes={s[:j] for s in paths for j in range(len(s)+1)}
    assert not any(s[:-j] in paths for s in paths for j in range(1,len(s)+1))
    todo=[''];n=0
    while todo:
        s=todo.pop()
        if s in paths:n+=1;continue
        assert s+'0' in prefixes and s+'1' in prefixes,('hole',s)
        todo.extend((s+'0',s+'1'))
    assert n==len(paths)
    return n

def audit_377(path):
    data=Path(path).read_bytes()
    assert hashlib.sha256(data).hexdigest()==SHA377
    rects={'P':P,'Q':Q377}
    paths={k:set() for k in rects}
    margins={k:None for k in rects}
    counts=Counter()
    for row in csv.DictReader(data.decode('utf-8').splitlines()):
        tag=row['source']; assert tag in rects
        p=row['path'];assert set(p)<=set('01') and p not in paths[tag]
        assert int(row['depth'])==len(p)
        b=rects[tag]
        for bit in p:b=split_box(b)[int(bit)]
        expected=tuple(Q(row[k]) for k in ('xlo','xhi','ylo','yhi'))
        assert b==expected
        low=signed_support_377(b)
        assert low==Q(row['certified_L_lower'])
        diff=low-TARGET377[tag]; assert diff>0
        margins[tag]=diff if margins[tag] is None else min(margins[tag],diff)
        paths[tag].add(p);counts[tag]+=1
    assert counts=={'P':387,'Q':79},counts
    for tag in rects: validate_prefix_tree(paths[tag])
    gap=sum(TARGET377.values())-C377-LAM377*BUP377
    assert gap>0
    return {'bytes':len(data),'sha256':SHA377,'counts':dict(counts),
            'smallest_support_margins':{k:str(v) for k,v in margins.items()},
            'dual_cost_gap_lower':str(gap),'full_binary_coverage':True}

@lru_cache(None)
def range_B(k,a,b):
    vals=[B(k,a),B(k,b)]
    t=Q(k,3)
    if a<t<b: vals.append(B(k,t))
    return min(vals),max(vals)

def dist_to_interval(v,lo,hi):
    if lo<=v<=hi:return Q(0)
    return min(abs(v-lo),abs(v-hi))

@lru_cache(None)
def source_floor_376(rect):
    a,b,c,d=rect
    X=[range_B(k,a,b) for k in range(4)]
    Y=[range_B(k,c,d) for k in range(4)]
    blo=Q(0);clo=Q(0)
    for k in range(4):
        rrlo=(4*X[k][0]+Y[k][0])/5
        rrhi=(4*X[k][1]+Y[k][1])/5
        blo+=Q(5*W[k],32)*dist_to_interval(Q(M[k],160),rrlo,rrhi)
        for mult,anchor,band in ((63,Q(1,4),X[k]),(1,Q(3,4),X[k]),
                                 (9,Q(1,4),Y[k]),(7,Q(3,4),Y[k])):
            clo+=Q(mult*W[k],512)*dist_to_interval(B(k,anchor),*band)
    return blo,clo

def recover_4d_path(leaf,depth):
    cur=R376
    s=[]
    for _ in range(depth):
        if cur==leaf: raise AssertionError('premature coordinate equality')
        left,right=split_box(cur)
        # Compare leaf coordinates with split axis in the two candidates.
        n=4
        i=max(range(n),key=lambda j:cur[2*j+1]-cur[2*j]);j=2*i
        mid=left[j+1]
        if leaf[j+1]<=mid: cur=left;s.append('0')
        elif leaf[j]>=mid: cur=right;s.append('1')
        else:raise AssertionError(('crosses-parent-split',str(leaf),str(cur)))
    assert cur==leaf
    return ''.join(s)

def audit_376(path):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==SHA376
    paths=set()
    kinds=Counter();margins={};maxdepth=0
    for row in csv.DictReader(raw.decode('utf-8').splitlines()):
        assert row['region']=='RIGHT_Y_UPPER_STRIP'
        kind=row['closure'];assert kind in ('BUDGET','DUAL')
        dep=int(row['depth']);maxdepth=max(maxdepth,dep)
        box=tuple(Q(row[k]) for k in ('px0','px1','py0','py1','qx0','qx1','qy0','qy1'))
        assert all(R376[2*i]<=box[2*i]<box[2*i+1]<=R376[2*i+1] for i in range(4))
        p=recover_4d_path(box,dep)
        assert p not in paths
        paths.add(p)
        bp,cp=source_floor_376(box[:4]);bq,cq=source_floor_376(box[4:])
        blo=bp+bq;clo=cp+cq;ll=clo+LAM376*blo
        assert blo==Q(row['b_lower'])
        assert clo==Q(row['c_lower'])
        assert ll==Q(row['L_lower'])
        diff=(blo-BUP376) if kind=='BUDGET' else (ll-(C376+LAM376*BUP376))
        assert diff>0
        margins[kind]=diff if kind not in margins else min(margins[kind],diff)
        kinds[kind]+=1
    assert kinds=={'BUDGET':19175,'DUAL':47071},kinds
    assert len(paths)==66246
    assert validate_prefix_tree(paths)==66246
    assert maxdepth==38
    return {'bytes':len(raw),'sha256':SHA376,'counts':dict(kinds),'leaves':len(paths),
            'max_depth':maxdepth,'smallest_closure_margins':{k:str(v) for k,v in margins.items()},
            'full_binary_coverage':True}

def main():
    if len(sys.argv)!=3:raise SystemExit('usage: script STAGE377.csv STAGE376.csv')
    references,betalo,betahi=check_root_and_reference()
    a=audit_377(sys.argv[1]);print('STAGE377_INDEPENDENT_COMPLETE',flush=True)
    b=audit_376(sys.argv[2]);print('STAGE376_INDEPENDENT_COMPLETE',flush=True)
    output={'scope':'Stage385 independent upstream audit of Stage376/377 original all-real certificates',
            'arithmetic':'exact rational Fraction; original 16 comparisons and four residual channels',
            'frozen_global':'bf84bd7c61a2444b59b1da96be57df0e9ae47e53',
            'frozen_em':'2af3fc484eb11060b69e0afc1b562bcaf5ad1419',
            'frozen_p000_blob':'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488',
            'root_beta_lower':betalo,'root_beta_upper':betahi,
            'references':references,'stage377':a,'stage376':b,
            'checked_total_leaves':sum(a['counts'].values())+b['leaves'],
            'conclusion':'BOTH_PROVED_CONDITIONAL_CONTINUOUS_EXCLUSIONS_AUDITED; earlier Stage375 global localization retained as hypothesis'}
    print(json.dumps(output,sort_keys=True,ensure_ascii=False,indent=2))
    print('STAGE385B_INDEPENDENT_STAGE376_377_PASS')

if __name__=='__main__': main()
