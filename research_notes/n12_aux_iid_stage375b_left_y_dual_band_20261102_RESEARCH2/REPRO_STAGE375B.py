#!/usr/bin/env python3
"""Exact continuous-domain budget/cost exclusion for Stage375-B.

Frozen scientific input: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53;
EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419;
P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.
16 provenance-distinct audit comparisons, four independent audit channels.
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from pathlib import Path

W=(1,3,3,1); M=(61,21,9,9)
LAM=F(13,10); E=F(11,5000)
BUDGET_UP=F(61,6250); CREF_UP=F(63182,10**6)
P_LO=(F(577,2500),F(469,2000),F(27,50),F(11,20))
P_HI=(F(577,2500),F(469,2000),F(14,25),F(59,100))
Q_CORE=(F(473,2000),F(239,1000),F(143,250),F(2897,5000))
REGIONS=(('P_LO',P_LO,F(37970,10**6)),
         ('P_HI',P_HI,F(37900,10**6)),
         ('Q_CORE',Q_CORE,F(37980,10**6)))

@lru_cache(None)
def B(k,z):return z**k*(1-z)**(3-k)
def residual(k,x,y):return (4*B(k,x)+B(k,y))/5-F(M[k],160)
def error(x,y):return F(5,32)*sum(W[k]*abs(residual(k,x,y)) for k in range(4))
def D(anchor,z):return sum(W[k]*abs(B(k,anchor)-B(k,z)) for k in range(4))/2
def cost(x,y):
    return (63*D(F(1,4),x)+D(F(3,4),x)
           +9*D(F(1,4),y)+7*D(F(3,4),y))/256

@lru_cache(None)
def band(k,a,z):
    values=[B(k,a),B(k,z)]
    critical=F(k,3)
    if a<critical<z: values.append(B(k,critical))
    return min(values),max(values)
def gap(target,lo,hi):
    return F(0) if lo<=target<=hi else min(abs(target-lo),abs(target-hi))

def pointwise_lower_bounds(x0,x1,y0,y1):
    X=[band(k,x0,x1) for k in range(4)]
    Y=[band(k,y0,y1) for k in range(4)]
    bmin=F(5,32)*sum(W[k]*gap(F(M[k],160),
                        (4*X[k][0]+Y[k][0])/5,
                        (4*X[k][1]+Y[k][1])/5) for k in range(4))
    audit=((63,F(1,4),X),(1,F(3,4),X),
           (9,F(1,4),Y),(7,F(3,4),Y))
    cmin=sum(F(h,512)*sum(W[k]*gap(B(k,anchor),ranges[k][0],ranges[k][1])
                         for k in range(4)) for h,anchor,ranges in audit)
    return bmin,cmin

def fmt(q):return f'{q.numerator}/{q.denominator}'
def exact_reference_check():
    xl,xu=F(2310839,10**7),F(2310840,10**7)
    yl,yu=F(5555086,10**7),F(5555091,10**7)
    assert residual(0,xl,yu)>0>residual(0,xu,yl)
    assert residual(1,xl,yl)>0>residual(1,xl,yu)
    assert residual(1,xu,yl)>0>residual(1,xu,yu)
    assert residual(2,xl,yl)>0 and residual(3,xu,yu)<0
    beta_lo=F(15,16)*residual(2,xl,yl)
    beta_hi=F(15,16)*residual(2,xu,yu)
    assert 2*beta_hi+E<BUDGET_UP
    P=(F(231138,10**6),F(555681,10**6))
    Q=(F(237807,10**6),F(575694,10**6))
    assert error(*P)+error(*Q)<2*beta_lo+E
    assert cost(*P)+cost(*Q)==F(16174439790495832521,256000000000000000000)
    assert cost(*P)+cost(*Q)<CREF_UP
    assert (F(37970+37980,10**6)-LAM*BUDGET_UP-CREF_UP==F(8,10**5))
    assert (F(37900+37980,10**6)-LAM*BUDGET_UP-CREF_UP==F(1,10**5))

def cover(tag,rect,target,rows):
    stack=[(*rect,0)]
    splits=leaves=maxdepth=0
    min_margin=None
    area=F(0)
    while stack:
        x0,x1,y0,y1,depth=stack.pop()
        bmin,cmin=pointwise_lower_bounds(x0,x1,y0,y1)
        lower=cmin+LAM*bmin
        if lower>target:
            leaves+=1
            maxdepth=max(maxdepth,depth)
            area+=(x1-x0)*(y1-y0)
            margin=lower-target
            if min_margin is None or margin<min_margin: min_margin=margin
            rows.append((tag,depth,x0,x1,y0,y1,bmin,cmin,lower))
            continue
        assert depth<36, ('UNRESOLVED',tag,depth,x0,x1,y0,y1)
        splits+=1
        if 5*(x1-x0)>=y1-y0:
            mid=(x0+x1)/2
            stack.extend([(x0,mid,y0,y1,depth+1),
                          (mid,x1,y0,y1,depth+1)])
        else:
            mid=(y0+y1)/2
            stack.extend([(x0,x1,y0,mid,depth+1),
                          (x0,x1,mid,y1,depth+1)])
    assert leaves==splits+1
    assert area==(rect[1]-rect[0])*(rect[3]-rect[2])
    return tag,splits,leaves,maxdepth,min_margin

def run(output_path):
    exact_reference_check()
    rows=[]
    stats=[cover(tag,rect,target,rows) for tag,rect,target in REGIONS]
    header='region,depth,xlo,xhi,ylo,yhi,b_lower,c_lower,L_lower\n'
    csv=header+''.join(','.join([tag,str(depth),*(fmt(z) for z in (x0,x1,y0,y1,bmin,cmin,lower))])+'\n'
                       for tag,depth,x0,x1,y0,y1,bmin,cmin,lower in rows)
    data=csv.encode('utf-8')
    if output_path is not None:
        output_path.write_bytes(data)
        assert output_path.read_bytes()==data
    print('STAGE375B_LEFT_Y_BAND_EXACT_PASS')
    print('scientific_input_pin_GLOBAL=bf84bd7c61a2444b59b1da96be57df0e9ae47e53')
    print('scientific_input_pin_EM=2af3fc484eb11060b69e0afc1b562bcaf5ad1419')
    print('budget_E=11/5000;lambda=13/10;budget_upper=61/6250;cost_ref_upper=63182/1000000')
    print('P_y<=11/20_cost_gap>8/100000;P_y>=14/25_cost_gap>1/100000')
    print('necessary_left_source_band=11/20<y_P<14/25')
    for tag,splits,nleaf,maxdep,margin in stats:
        print('region',tag,'splits',splits,'leaves',nleaf,
              'maxdepth',maxdep,'strict_margin',fmt(margin))
    print('total_leaves',len(rows),'csv_bytes',len(data),'csv_sha256',sha256(data).hexdigest())

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--emit',type=Path,default=None)
    args=ap.parse_args()
    run(args.emit)
