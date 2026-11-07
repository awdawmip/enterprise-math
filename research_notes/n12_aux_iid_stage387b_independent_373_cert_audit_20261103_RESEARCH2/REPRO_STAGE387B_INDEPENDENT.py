#!/usr/bin/env python3
"""Stage387-B: independent proof-certificate replay for Stage373-B.

Frozen scientific inputs: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53;
EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob
bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.
Uses only the 16 original independently labelled Bernoulli audit terms and
four BRC residuals. All arithmetic exact (fractions.Fraction).
No imports/calls to Stages 370-386. The original Stage373 deterministic
serialisation is reconstructed for a byte-exact reproducibility check.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from functools import lru_cache
import argparse, json

# Power basis is independent of original factored Bernoulli representation.
COEFF=((1,-3,3,-1),(0,1,-2,1),(0,0,1,-1),(0,0,0,1))
W=(1,3,3,1)
M=(61,21,9,9)
A=F(1,4); H=F(3,4)
LAMBDA=F(6,5)
SPECS=(
 ('LEFT_X',(F(577,2500),F(469,2000),F(27,50),F(59,100)), F(1873,50000),4200,20),
 ('RIGHT_Y_LE_57_100',(F(469,2000),F(239,1000),F(27,50),F(57,100)), F(37443,10**6),4258,23),
 ('RIGHT_Y_GE_29_50',(F(469,2000),F(239,1000),F(29,50),F(59,100)), F(37445,10**6),86,14),
)

def bern(k,z):
    a,b,c,d=COEFF[k]
    return (((F(d)*z+c)*z+b)*z+a)

def residual(k,x,y):
    return (4*bern(k,x)+bern(k,y))/5-F(M[k],160)

def budget(x,y):
    return F(5,32)*sum(W[k]*abs(residual(k,x,y)) for k in range(4))

def cost(x,y):
    return sum(F(h*W[k],512)*abs(bern(k,z)-bern(k,a))
      for h,a,z in ((63,A,x),(1,H,x),(9,A,y),(7,H,y)) for k in range(4))

@lru_cache(None)
def interval_bern(k,lo,hi):
    assert F(0)<=lo<=hi<=F(1)
    vals=[bern(k,lo),bern(k,hi)]
    extremum=F(k,3)
    if lo<extremum<hi: vals.append(bern(k,extremum))
    return (min(vals),max(vals))

def distance_to_closed_interval(q,inter):
    u,v=inter
    return max(F(0),u-q,q-v)

def bounds(box):
    xl,xh,yl,yh=box
    X=[interval_bern(k,xl,xh) for k in range(4)]
    Y=[interval_bern(k,yl,yh) for k in range(4)]
    port_lower=sum(F(h*W[k],512)*distance_to_closed_interval(bern(k,a),ranges[k])
        for h,a,ranges in ((63,A,X),(1,H,X),(9,A,Y),(7,H,Y)) for k in range(4))
    residual_lower=sum(F(5*W[k],32)*distance_to_closed_interval(F(M[k],160),
         ((4*X[k][0]+Y[k][0])/5, (4*X[k][1]+Y[k][1])/5)) for k in range(4))
    return residual_lower,port_lower

def check_root_and_reference():
    xl,xu=F(2310839,10**7),F(2310840,10**7)
    yl,yu=F(5555086,10**7),F(5555091,10**7)
    # Poincare--Miranda: r0 has opposite signs on x-faces,
    # r1 has opposite signs on y-faces. Both partial signs are strict.
    assert residual(0,xl,yu)>0 and residual(0,xu,yl)<0
    assert residual(1,xl,yl)>0 and residual(1,xu,yl)>0
    assert residual(1,xl,yu)<0 and residual(1,xu,yu)<0
    # B0 strictly decreasing for x,y in (0,1), B1 increasing on x<1/3
    # and decreasing on y>1/3: r0=0 trace yields unique r1 root.
    assert xu<F(1,3)<yl
    for xx in (xl,xu):
        for yy in (yl,yu):
            assert residual(2,xx,yy)>0 and residual(3,xx,yy)<0
    bl=F(15,16)*residual(2,xl,yl)
    bu=F(15,16)*residual(2,xu,yu)
    assert bl<bu
    E=F(11,5000)
    assert 2*bu+E<F(61,6250)
    p=(F(231138,10**6),F(555681,10**6))
    q=(F(237807,10**6),F(575694,10**6))
    ref_b=budget(*p)+budget(*q)
    ref_c=cost(*p)+cost(*q)
    assert ref_b<2*bl+E
    assert ref_c==F(16174439790495832521,256000000000000000000)
    assert ref_c<F(6319,100000)
    return bl,bu,ref_b,ref_c

def check_cover(tag,region,threshold):
    todo=[(*region,0)]
    rows=[];split_count=0;area=F(0);maxdepth=0;min_margin=None
    while todo:
        xa,xb,ya,yb,depth=todo.pop()
        bb,cc=bounds((xa,xb,ya,yb))
        value=cc+LAMBDA*bb
        if value>threshold:
            rows.append((tag,depth,xa,xb,ya,yb,bb,cc,value))
            area+=(xb-xa)*(yb-ya)
            maxdepth=max(maxdepth,depth)
            gap=value-threshold
            min_margin=gap if min_margin is None else min(min_margin,gap)
        else:
            assert depth<40,(tag,'unclosed',depth)
            split_count+=1
            # Same explicit closed dyadic partition as original certificate;
            # independent lower-bound computation and polynomial form.
            if (xb-xa)*5>=yb-ya:
                mid=(xa+xb)/2
                todo.append((xa,mid,ya,yb,depth+1))
                todo.append((mid,xb,ya,yb,depth+1))
            else:
                mid=(ya+yb)/2
                todo.append((xa,xb,ya,mid,depth+1))
                todo.append((xa,xb,mid,yb,depth+1))
    assert len(rows)==split_count+1
    assert area==(region[1]-region[0])*(region[3]-region[2])
    assert min_margin>0
    return rows,dict(region=tag,leaves=len(rows),max_depth=maxdepth,
                     strict_min_support_margin=str(min_margin))

def run(output):
    bl,bu,rb,rc=check_root_and_reference()
    entries=[];detail=[]
    for name,rect,target,count,depth in SPECS:
        rows,summary=check_cover(name,rect,target)
        assert len(rows)==count and summary['max_depth']==depth,(name,summary)
        entries+=rows;detail.append(summary)
    text='region,depth,xlo,xhi,ylo,yhi,b_lower,c_lower,L_lower\n'
    text+=''.join(','.join([row[0],str(row[1]),*(str(val) for val in row[2:])])+'\n' for row in entries)
    raw=text.encode('utf-8')
    digest=sha256(raw).hexdigest()
    assert len(entries)==8544
    assert len(raw)==1581616,(len(raw),digest)
    assert digest=='fd8a761683245556cef44f15bd44fd1fadb539d6c3fa868f1dec6ff75b0bd5ae',digest
    if output:
        output.parent.mkdir(parents=True,exist_ok=True)
        output.write_bytes(raw)
        assert sha256(output.read_bytes()).hexdigest()==digest
    gaplo=F(1873,50000)+F(37443,10**6)-LAMBDA*F(61,6250)-F(6319,100000)
    gaphi=F(1873,50000)+F(37445,10**6)-LAMBDA*F(61,6250)-F(6319,100000)
    assert gaplo==F(1,10**6) and gaphi==F(3,10**6)
    print('STAGE387B_INDEPENDENT_STAGE373_ALL_REAL_PASS')
    print(json.dumps(dict(stage=387,frozen_global='bf84bd7c61a2444b59b1da96be57df0e9ae47e53',
     frozen_em='2af3fc484eb11060b69e0afc1b562bcaf5ad1419',
     p000_blob='bcc2590d3168a28f72e8b9f0f9b1f76faadcd488',
     certificate_bytes=len(raw),certificate_sha256=digest,leaf_total=len(entries),
     min_gap_low=str(gaplo),min_gap_high=str(gaphi),reference_cost=str(rc),
     beta_interval=[str(bl),str(bu)],parts=detail,
     conditional_on='Stage370 optimizer core and Stage372 x-straddle; prior Stages368-369'),
     indent=2,sort_keys=True))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--emit',type=Path)
    run(p.parse_args().emit)
