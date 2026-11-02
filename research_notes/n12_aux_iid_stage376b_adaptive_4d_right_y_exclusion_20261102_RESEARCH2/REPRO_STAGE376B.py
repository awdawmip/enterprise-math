#!/usr/bin/env python3
"""Stage376-B: exact 4D coupled exclusion of upper right-source y strip.

Frozen scientific inputs: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53;
EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419;
P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.
All calculations use exact Python Fraction arithmetic. No sampled-point inference.
"""
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import argparse

W=(1,3,3,1); M=(61,21,9,9)
LAM=F(13,10); E=F(11,5000)
BUDGET_UP=F(61,6250)
CREF=F(16174439790495832521,256000000000000000000)
THRESHOLD=CREF+LAM*BUDGET_UP
PX=(F(577,2500),F(469,2000)); QX=(F(473,2000),F(239,1000))
QY=(F(72,125),F(2897,5000)) # 0.576 .. 0.5794
REGIONS=(('RIGHT_Y_UPPER_STRIP',(*PX,F(11,20),F(14,25),*QX,*QY)),)

@lru_cache(None)
def B(k,z): return z**k*(1-z)**(3-k)
def r(k,x,y): return (4*B(k,x)+B(k,y))/5-F(M[k],160)
def b(x,y): return F(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))
def D(a,z): return sum(W[k]*abs(B(k,a)-B(k,z)) for k in range(4))/2
def c(x,y): return (63*D(F(1,4),x)+D(F(3,4),x)+9*D(F(1,4),y)+7*D(F(3,4),y))/256

@lru_cache(None)
def band(k,lo,hi):
    values=[B(k,lo),B(k,hi)]; t=F(k,3)
    if lo<t<hi: values.append(B(k,t))
    return min(values),max(values)
def gap(target,lo,hi):
    return F(0) if lo<=target<=hi else min(abs(target-lo),abs(target-hi))

@lru_cache(maxsize=None)
def source_lower(rect):
    x0,x1,y0,y1=rect
    X=[band(k,x0,x1) for k in range(4)]
    Y=[band(k,y0,y1) for k in range(4)]
    bmin=F(5,32)*sum(W[k]*gap(F(M[k],160),
        (4*X[k][0]+Y[k][0])/5,(4*X[k][1]+Y[k][1])/5) for k in range(4))
    audit=((63,F(1,4),X),(1,F(3,4),X),(9,F(1,4),Y),(7,F(3,4),Y))
    cmin=sum(F(weight,512)*sum(W[k]*gap(B(k,anchor),boxes[k][0],boxes[k][1])
       for k in range(4)) for weight,anchor,boxes in audit)
    return bmin,cmin

def exact_reference_check():
    xl,xu=F(2310839,10**7),F(2310840,10**7)
    yl,yu=F(5555086,10**7),F(5555091,10**7)
    assert r(0,xl,yu)>0>r(0,xu,yl)
    assert r(1,xl,yl)>0>r(1,xl,yu)
    assert r(1,xu,yl)>0>r(1,xu,yu)
    assert r(2,xl,yl)>0 and r(3,xu,yu)<0
    beta_lo=F(15,16)*r(2,xl,yl)
    beta_hi=F(15,16)*r(2,xu,yu)
    assert 2*beta_hi+E<BUDGET_UP
    P=(F(231138,10**6),F(555681,10**6))
    Q=(F(237807,10**6),F(575694,10**6))
    assert b(*P)+b(*Q)<2*beta_lo+E
    assert c(*P)+c(*Q)==CREF
    assert F(0)<CREF<THRESHOLD

def volume(box):
    ret=F(1)
    for j in range(0,8,2):ret*=box[j+1]-box[j]
    return ret

def cover(tag,rect,rows):
    stack=[(rect,0)]; splits=leaves=maxdepth=0; vol=F(0); minmargin=None
    class_count={'DUAL':0,'BUDGET':0}
    while stack:
        box,depth=stack.pop()
        bp,cp=source_lower(box[:4]); bq,cq=source_lower(box[4:])
        bl=bp+bq; cl=cp+cq; ll=cl+LAM*bl
        klass='BUDGET' if bl>BUDGET_UP else 'DUAL' if ll>THRESHOLD else None
        if klass:
            leaves+=1;maxdepth=max(maxdepth,depth);class_count[klass]+=1
            vol+=volume(box)
            margin=(bl-BUDGET_UP) if klass=='BUDGET' else (ll-THRESHOLD)
            minmargin=margin if minmargin is None else min(minmargin,margin)
            rows.append((tag,klass,depth,*box,bl,cl,ll))
            continue
        assert depth<48,('UNRESOLVED',tag,depth,*box)
        splits+=1
        j=max(range(4),key=lambda i:box[2*i+1]-box[2*i])*2
        mid=(box[j]+box[j+1])/2
        box0=box[:j]+(box[j],mid)+box[j+2:]
        box1=box[:j]+(mid,box[j+1])+box[j+2:]
        stack.extend(((box0,depth+1),(box1,depth+1)))
    assert splits+1==leaves and vol==volume(rect)
    return (tag,splits,leaves,maxdepth,class_count['BUDGET'],class_count['DUAL'],minmargin)

def run(path=None):
    exact_reference_check()
    rows=[]; stats=[cover(tag,rect,rows) for tag,rect in REGIONS]
    header='region,closure,depth,px0,px1,py0,py1,qx0,qx1,qy0,qy1,b_lower,c_lower,L_lower\n'
    data=(header+''.join(','.join((tag,kind,str(depth),*(str(t) for t in (*box,bl,cl,ll))))+'\n'
      for tag,kind,depth,*rest in rows for box,bl,cl,ll in [(tuple(rest[:8]),*rest[8:])])).encode()
    if path is not None:
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(data)
        assert path.read_bytes()==data
    print('STAGE376B_EXACT_COUPLED_FOUR_PARAMETER_RIGHT_Y_EXCLUSION_PASS')
    print('scientific_input_pin_GLOBAL=bf84bd7c61a2444b59b1da96be57df0e9ae47e53')
    print('scientific_input_pin_EM=2af3fc484eb11060b69e0afc1b562bcaf5ad1419')
    print('budget_E=11/5000;dual_lambda=13/10;budget_upper='+str(BUDGET_UP))
    print('reference_cost='+str(CREF))
    print('dual_threshold='+str(THRESHOLD))
    print('theorem=global_minimizer_has_q_y<72/125')
    for tag,splits,leaves,depth,nb,nd,m in stats:
        print('region',tag,'splits',splits,'leaves',leaves,'maxdepth',depth,
              'budget_leaves',nb,'dual_leaves',nd,'minimum_certificate_margin',str(m))
    print('total_leaves',len(rows),'csv_bytes',len(data),'csv_sha256',sha256(data).hexdigest())

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--emit',type=Path,default=None)
    run(parser.parse_args().emit)
