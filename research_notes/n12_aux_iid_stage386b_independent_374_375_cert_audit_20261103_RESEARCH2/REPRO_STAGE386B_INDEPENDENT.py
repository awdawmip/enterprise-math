#!/usr/bin/env python3
"""Independent exact full-domain audit of frozen Stage374/375 interval certificates.

Uses original 16 labelled comparisons, four BRC residual channels, exact rationals;
does not import or run earlier stage generators. Optional --emit-dir saves regenerated CSV.
Scientific pins: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53;
EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419;
P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.
"""
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

WEIGHTS=(1,3,3,1); CENTERS=(61,21,9,9)
COEFF=((1,-3,3,-1),(0,1,-2,1),(0,0,1,-1),(0,0,0,1))
E=F(11,5000)
P=(F(577,2500),F(469,2000),F(27,50),F(59,100))
Q=(F(469,2000),F(239,1000),F(57,100),F(29,50))
U=(F(473,2000),F(239,1000),F(143,250),F(2897,5000))
SPECS=(
  ('374',F(6,5),(
    ('LEFT',P,F(37464,10**6)),
    ('RIGHT_LO',(Q[0],Q[1],Q[2],F(143,250)),F(37431,10**6)),
    ('RIGHT_HI',(Q[0],Q[1],F(2897,5000),Q[3]),F(37431,10**6)),
    ('RIGHT_X_LO',(Q[0],F(473,2000),F(143,250),F(2897,5000)),F(37431,10**6))),
    9970,1871013,'636a84ea0eb1e9b4aaf7262d632eb7df8207be039044b832885b4ba00e56d4e4'),
  ('375',F(13,10),(
    ('P_LO',(P[0],P[1],P[2],F(11,20)),F(37970,10**6)),
    ('P_HI',(P[0],P[1],F(14,25),P[3]),F(37900,10**6)),
    ('Q_CORE',U,F(37980,10**6))),
    3619,653418,'75d0233f4425b0ad8f6fb46bea8a68be1568e328b237ef8cf9250c5d3cc8e6e7'))

def bern(k,z):
    a,b,c,d=COEFF[k]
    return ((F(d)*z+c)*z+b)*z+a

def residual(k,x,y): return (4*bern(k,x)+bern(k,y))/5-F(CENTERS[k],160)
def budget(x,y): return F(5,32)*sum(WEIGHTS[k]*abs(residual(k,x,y)) for k in range(4))
def cost(x,y):
    terms=((63,F(1,4),x),(1,F(3,4),x),(9,F(1,4),y),(7,F(3,4),y))
    return sum(F(h*WEIGHTS[k],512)*abs(bern(k,z)-bern(k,a))
               for h,a,z in terms for k in range(4))

def exact_range(k,lo,hi):
    vals=[bern(k,lo),bern(k,hi)]
    s=F(k,3)
    if lo<s<hi: vals.append(bern(k,s))
    return min(vals),max(vals)

def dist_to_interval(t,v):
    lo,hi=v
    if lo<=t<=hi: return F(0)
    return lo-t if t<lo else t-hi

def certified_bounds(box):
    xa,xb,ya,yb=box
    xbds=[exact_range(k,xa,xb) for k in range(4)]
    ybds=[exact_range(k,ya,yb) for k in range(4)]
    b=F(5,32)*sum(WEIGHTS[k]*dist_to_interval(F(CENTERS[k],160),
                ((4*xbds[k][0]+ybds[k][0])/5,(4*xbds[k][1]+ybds[k][1])/5))
                for k in range(4))
    c=sum(F(mult*WEIGHTS[k],512)*dist_to_interval(bern(k,a),bounds[k])
          for mult,a,bounds in ((63,F(1,4),xbds),(1,F(3,4),xbds),
                                (9,F(1,4),ybds),(7,F(3,4),ybds))
          for k in range(4))
    return b,c

def reference():
    xl,xu=F(2310839,10**7),F(2310840,10**7)
    yl,yu=F(5555086,10**7),F(5555091,10**7)
    assert residual(0,xl,yu)>0>residual(0,xu,yl)
    assert residual(1,xl,yl)>0>residual(1,xl,yu)
    assert residual(1,xu,yl)>0>residual(1,xu,yu)
    for z in (xl,xu):
        for k,sign in ((0,-1),(1,1)):
            d=(bern(k,z+F(1,10**9))-bern(k,z))
            assert sign*d>0
    for z in (yl,yu):
        assert bern(0,z+F(1,10**9))<bern(0,z)
        assert bern(1,z+F(1,10**9))<bern(1,z)
    assert residual(2,xl,yl)>0 and residual(3,xu,yu)<0
    lo=F(15,16)*residual(2,xl,yl)
    hi=F(15,16)*residual(2,xu,yu)
    assert lo<hi and 2*hi+E<F(61,6250)
    p=(F(231138,10**6),F(555681,10**6))
    q=(F(237807,10**6),F(575694,10**6))
    ref=cost(*p)+cost(*q)
    assert budget(*p)+budget(*q)<2*lo+E
    assert ref==F(16174439790495832521,256000000000000000000)
    assert ref<F(63182,10**6)
    return lo,hi,ref

def audit_one(tag,rect,target,lam):
    todo=[(*rect,0)]
    leaves=[];splits=0;cover=F(0);minmargin=None;maxdepth=0
    while todo:
        xa,xb,ya,yb,depth=todo.pop()
        eb,ec=certified_bounds((xa,xb,ya,yb))
        support=ec+lam*eb
        if support>target:
            maxdepth=max(maxdepth,depth)
            cover+=(xb-xa)*(yb-ya)
            margin=support-target
            minmargin=margin if minmargin is None else min(margin,minmargin)
            leaves.append((tag,depth,xa,xb,ya,yb,eb,ec,support))
            continue
        assert depth<40,('UNRESOLVED',tag,depth)
        splits+=1
        if 5*(xb-xa)>=yb-ya:
            mid=(xa+xb)/2
            todo.extend(((xa,mid,ya,yb,depth+1),(mid,xb,ya,yb,depth+1)))
        else:
            mid=(ya+yb)/2
            todo.extend(((xa,xb,ya,mid,depth+1),(xa,xb,mid,yb,depth+1)))
    assert len(leaves)==splits+1
    assert cover==(rect[1]-rect[0])*(rect[3]-rect[2])
    return leaves,dict(region=tag,leaves=len(leaves),splits=splits,maxdepth=maxdepth,
                       min_strict_margin=str(minmargin))

def run(emit):
    lo,hi,ref=reference(); stats=[]
    for stage,lam,regions,want_n,want_size,want_hash in SPECS:
        rows=[];part=[]
        for tag,rect,target in regions:
            leaf,s=audit_one(tag,rect,target,lam)
            rows.extend(leaf);part.append(s)
        data=('region,depth,xlo,xhi,ylo,yhi,b_lower,c_lower,L_lower\n'+
              ''.join(','.join([r[0],str(r[1]),*(str(q) for q in r[2:])])+'\n' for r in rows)).encode()
        digest=hashlib.sha256(data).hexdigest()
        assert len(rows)==want_n,(stage,len(rows),want_n)
        assert len(data)==want_size,(stage,len(data),want_size)
        assert digest==want_hash,(stage,digest,want_hash)
        if emit:
            path=emit/('CERTIFICATE_STAGE'+stage+'B_REGENERATED.csv')
            path.write_bytes(data)
            assert hashlib.sha256(path.read_bytes()).hexdigest()==digest
        stats.append(dict(stage=stage,leaves=len(rows),bytes=len(data),sha256=digest,parts=part))
    cmax=F(63182,10**6);budgetup=F(61,6250)
    assert F(37464+37431,10**6)-F(6,5)*budgetup-cmax==F(1,10**6)
    assert F(37970+37980,10**6)-F(13,10)*budgetup-cmax==F(8,10**5)
    assert F(37900+37980,10**6)-F(13,10)*budgetup-cmax==F(1,10**5)
    print('STAGE386B_INDEPENDENT_374_375_ALL_REAL_PASS')
    print(json.dumps(dict(stage=386,mode='EXACT_FRACTION',root_beta_lower=str(lo),
                          root_beta_upper=str(hi),comparator_cost=str(ref),
                          verified_leaf_total=sum(s['leaves'] for s in stats),
                          certificates=stats,conditional_on='Stage373 upstream localization',
                          frozen_global='bf84bd7c61a2444b59b1da96be57df0e9ae47e53',
                          frozen_em='2af3fc484eb11060b69e0afc1b562bcaf5ad1419'),
                     sort_keys=True,ensure_ascii=False,indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--emit-dir',type=Path)
    args=p.parse_args()
    if args.emit_dir:args.emit_dir.mkdir(parents=True,exist_ok=True)
    run(args.emit_dir)
