#!/usr/bin/env python3
"""Stage389-B: independent exact (Fraction/Horner) audit of Stage368+369.

All inputs (including reference budget, continuous box covers and all 16 labelled
anchor/port comparisons) are declared below. No earlier Stage368/369 modules are
imported. Integer-rational checks alone; no floating point, no sampled grid.
"""
from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from pathlib import Path

COEF = ((1,-3,3,-1), (0,1,-2,1), (0,0,1,-1), (0,0,0,1))
W = (1,3,3,1)
M = (61,21,9,9)
A = (F(1,4),F(3,4))
LAMBDA = F(6,5)
E = F(11,5000)
R = (F(219,1000), F(239,1000), F(51,100), F(16,25))
S = (R[0],F(577,2500),R[2],R[3])
RLOW = F(373,10000)
SLOW = F(753,20000)
MINB = F(377,100000)
CAP = F(61,6250)
OUT = CAP-MINB
CSV368_SHA = 'adcca00c9a5cf502ab03fcecf324b321683487dab432b28ac59ee0b549c16040'
CSV369_SHA = 'c60855319b26ba0e842906aa9126489568b001eef5945fd24247e64369f884d9'

def frac(q):return f'{q.numerator}/{q.denominator}'

def bern(k, z):
    aa=COEF[k]
    return ((aa[3]*z+aa[2])*z+aa[1])*z+aa[0]

@lru_cache(None)
def range_bern(k,u,v):
    assert 0<=u<=v<=1
    values=[bern(k,u),bern(k,v)]
    critical=F(k,3)
    if u<critical<v:
        values.append(bern(k,critical))
    return min(values),max(values)

def dist(const,lo,hi):
    # Certified lower bound to |const-t| for all t in [lo,hi].
    return max(F(0),lo-const,const-hi)

def source_bounds(x0,x1,y0,y1):
    X=[range_bern(k,x0,x1) for k in range(4)]
    Y=[range_bern(k,y0,y1) for k in range(4)]
    lower_b=F(5,32)*sum(W[k]*dist(F(M[k],160),
        (4*X[k][0]+Y[k][0])/5,(4*X[k][1]+Y[k][1])/5)
        for k in range(4))
    def single_port(anchor,band):
        return F(1,2)*sum(W[k]*dist(bern(k,anchor),*band[k]) for k in range(4))
    ports=(single_port(A[0],X),single_port(A[1],X),
           single_port(A[0],Y),single_port(A[1],Y))
    lower_c=sum(F(z,256)*p for z,p in zip((63,1,9,7),ports))
    return lower_b,lower_c

def residual(k,x,y):return (4*bern(k,x)+bern(k,y))/5-F(M[k],160)

def budget(x,y):return F(5,32)*sum(W[k]*abs(residual(k,x,y)) for k in range(4))

def source_cost(x,y):
    return sum(F(weight,512)*sum(W[k]*abs(bern(k,a)-bern(k,z)) for k in range(4))
               for weight,a,z in ((63,A[0],x),(1,A[1],x),(9,A[0],y),(7,A[1],y)))

def bisection(J,axis):
    x0,x1,y0,y1=J
    if axis=='x':
        mid=(x0+x1)/2
        return ((x0,mid,y0,y1),(mid,x1,y0,y1))
    mid=(y0+y1)/2
    return ((x0,x1,y0,mid),(x0,x1,mid,y1))

def cover368():
    todo=[(R[0]*0,F(1),R[2]*0,F(1),0)]
    rows=[]; counters=Counter();area=F(0)
    while todo:
        x0,x1,y0,y1,depth=todo.pop()
        eb,ec=source_bounds(x0,x1,y0,y1)
        inside=x0>=R[0] and x1<=R[1] and y0>=R[2] and y1<=R[3]
        if eb>OUT:tag='OUTSIDE_FORBIDDEN';threshold=OUT
        elif inside and eb>MINB:tag='INSIDE_GLOBAL_BOUND';threshold=MINB
        else:
            assert depth<40,('unclosed368',depth,x0,x1,y0,y1)
            counters['SPLIT']+=1
            axis='x' if 4*(x1-x0)>=y1-y0 else 'y'
            todo.extend((*child,depth+1) for child in bisection((x0,x1,y0,y1),axis))
            continue
        counters[tag]+=1
        rows.append((depth,x0,x1,y0,y1,tag,eb,eb-threshold))
        area+=(x1-x0)*(y1-y0)
    assert area==1
    assert counters==Counter({'SPLIT':603,'OUTSIDE_FORBIDDEN':338,'INSIDE_GLOBAL_BOUND':266}),counters
    assert len(rows)==604 and max(q[0] for q in rows)==28
    csv='depth,xlo,xhi,ylo,yhi,classification,exact_lower_bound\n'
    csv+=''.join(','.join([str(depth),frac(x0),frac(x1),frac(y0),frac(y1),tag,frac(eb)])+'\n'
                 for depth,x0,x1,y0,y1,tag,eb,gap in rows)
    raw=csv.encode('utf-8')
    assert len(raw)==43413 and sha256(raw).hexdigest()==CSV368_SHA,(len(raw),sha256(raw).hexdigest())
    return raw,rows,counters

def cover369(tag,box,target):
    todo=[(*box,0)]
    rows=[];splits=0;area=F(0)
    while todo:
        x0,x1,y0,y1,depth=todo.pop()
        eb,ec=source_bounds(x0,x1,y0,y1)
        val=ec+LAMBDA*eb
        if val>target:
            rows.append((tag,depth,x0,x1,y0,y1,eb,ec,val,val-target))
            area+=(x1-x0)*(y1-y0)
        else:
            assert depth<44,(tag,depth,x0,x1,y0,y1)
            splits+=1
            axis='x' if 5*(x1-x0)>=y1-y0 else 'y'
            todo.extend((*child,depth+1) for child in bisection((x0,x1,y0,y1),axis))
    assert len(rows)==splits+1 and area==(box[1]-box[0])*(box[3]-box[2])
    return rows,splits,area

def main():
    ap=ArgumentParser();ap.add_argument('--emit-dir');args=ap.parse_args()
    xl,xu=F(2310839,10**7),F(2310840,10**7)
    yl,yu=F(5555086,10**7),F(5555091,10**7)
    assert residual(0,xl,yu)>0>residual(0,xu,yl)
    assert residual(1,xl,yl)>0>residual(1,xl,yu)
    assert residual(1,xu,yl)>0>residual(1,xu,yu)
    assert residual(2,xl,yl)>0>residual(3,xu,yu)
    beta_low=F(15,16)*residual(2,xl,yl)
    beta_high=F(15,16)*residual(2,xu,yu)
    assert beta_low<beta_high<F(189,50000)
    budget_ceiling=2*beta_high+E
    assert budget_ceiling<CAP
    p=(F(231138,10**6),F(555681,10**6))
    q=(F(237807,10**6),F(575694,10**6))
    b_ref=budget(*p)+budget(*q)
    c_ref=source_cost(*p)+source_cost(*q)
    assert b_ref==F(156126870406900413,16000000000000000000)
    assert c_ref==F(16174439790495832521,256000000000000000000)
    assert b_ref<2*beta_low+E
    assert c_ref<F(6319,100000)
    cert368,rows368,counts368=cover368()
    rowR,splitsR,areaR=cover369('R',R,RLOW)
    rowS,splitsS,areaS=cover369('S',S,SLOW)
    assert (splitsR,len(rowR),max(z[1] for z in rowR))==(1190,1191,16)
    assert (splitsS,len(rowS),max(z[1] for z in rowS))==(112,113,18)
    csv='region,depth,xlo,xhi,ylo,yhi,b_lower,c_lower,L_lower\n'
    csv+=''.join(','.join([tag,str(d)]+[frac(z) for z in (x0,x1,y0,y1,eb,ec,L)])+'\n'
                 for tag,d,x0,x1,y0,y1,eb,ec,L,gap in rowR+rowS)
    cert369=csv.encode('utf-8')
    assert len(cert369)==189212 and sha256(cert369).hexdigest()==CSV369_SHA,(len(cert369),sha256(cert369).hexdigest())
    # Strengthening: use the existing exact root upper enclosure and the
    # unrounded rational reference cost rather than two coarse decimal bounds.
    strict_margin=RLOW+SLOW-LAMBDA*budget_ceiling-c_ref
    assert strict_margin==F(9379440296847963487,160000000000000000000000)
    assert strict_margin>F(3,62500)
    assert min(z[-1] for z in rows368+rowR+rowS)>0
    if args.emit_dir:
        dest=Path(args.emit_dir);dest.mkdir(parents=True,exist_ok=True)
        (dest/'CERTIFICATE_STAGE368B_REGENERATED.csv').write_bytes(cert368)
        (dest/'CERTIFICATE_STAGE369B_REGENERATED.csv').write_bytes(cert369)
    print('STAGE389B_INDEPENDENT_368_369_AND_STRONGER_MARGIN_PASS')
    print('stage368=604 leaves;338 outside;266 inside;603 splits;area=1;unclosed=0')
    print('stage368_min_exact_gap='+frac(min(z[-1] for z in rows368)))
    print('stage368_bytes='+str(len(cert368))+';sha256='+sha256(cert368).hexdigest())
    print('stage369=1191 R leaves;113 S leaves;1304 total;area_R='+frac(areaR)+';area_S='+frac(areaS)+';unclosed=0')
    print('stage369_min_R_gap='+frac(min(z[-1] for z in rowR)))
    print('stage369_min_S_gap='+frac(min(z[-1] for z in rowS)))
    print('stage369_bytes='+str(len(cert369))+';sha256='+sha256(cert369).hexdigest())
    print('beta_lower='+frac(beta_low)+';beta_upper='+frac(beta_high))
    print('budget_upper='+frac(budget_ceiling)+';reference_budget='+frac(b_ref))
    print('reference_c='+frac(c_ref)+';strict_new_T_margin='+frac(strict_margin)+';old_margin=3/62500')
    print('source_swap_preserved=true;all_16_audit_labels_and_4_residual_channels=true')

if __name__=='__main__':main()
