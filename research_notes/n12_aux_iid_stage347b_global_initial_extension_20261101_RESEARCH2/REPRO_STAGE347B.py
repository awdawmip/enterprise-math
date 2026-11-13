#!/usr/bin/env python3
"""Stage347-B: exact continuous Bernstein source-tagged Pareto extender.
Execute from this directory with Python >=3.10 standard library; no external dependencies.
All predicates are Fraction comparisons. Decimal text is display only.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import csv
import io

W=(1,3,3,1); M=(61,21,9,9)
QPUBLIC=Q(271,50000)  # 0.00542
QAUDIT=Q(781,25000)   # 0.03124
LAMBDA=Q(6,5)
LIFT_THRESHOLD=QAUDIT+LAMBDA*QPUBLIC  # 0.037744
RECT=(Q(11,50),Q(6,25),Q(261,500),Q(127,200))
LOW=(RECT[0],RECT[1],Q(1,2),Q(531,1000))
HIGH=(RECT[0],RECT[1],Q(5,8),RECT[3])
OUT=Path(__file__).resolve().parent

def B(k,z):return z**k*(1-z)**(3-k)
def Bp(k,z):
    if k==0:return -3*(1-z)**2
    if k==3:return 3*z*z
    return k*z**(k-1)*(1-z)**(3-k)-(3-k)*z**k*(1-z)**(2-k)
def r(k,x,y):return (4*B(k,x)+B(k,y))/5-Q(M[k],160)
def D(a,z):return sum((Q(W[k],2)*abs(B(k,a)-B(k,z)) for k in range(4)),Q(0))
def c(x,y):return (63*D(Q(1,4),x)+D(Q(3,4),x)+9*D(Q(1,4),y)+7*D(Q(3,4),y))/256
def b(x,y):return Q(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))
def px(z):return (-189*z+186*z*z-61*z*z*z)/256
def dpx(z):return (-189+372*z-183*z*z)/256
def pylo(z):return (3*z*z-2*z*z*z)/128
def dpylo(z):return (6*z-6*z*z)/128
def pyhi(z):return (27*z*z-25*z*z*z)/256
def dpyhi(z):return (54*z-75*z*z)/256
KL=c(Q(23,100),Q(53,100))-px(Q(23,100))-pylo(Q(53,100))
KH=c(Q(23,100),Q(63,100))-px(Q(23,100))-pyhi(Q(63,100))
assert KL==Q(2673,16384) and KH==Q(621,4096)

def bernmin(f,df,a,d):
    t=(d-a)/3
    return min(f(a),f(a)+t*df(a),f(d)-t*df(d),f(d))

@lru_cache(maxsize=None)
def bs_min(mask,a,d):
    f=lambda z:sum((W[k]*B(k,z) for k in range(4) if mask>>k&1),Q(0))
    df=lambda z:sum((W[k]*Bp(k,z) for k in range(4) if mask>>k&1),Q(0))
    return bernmin(f,df,a,d)

def global_bound(xlo,xhi,ylo,yhi):
    v=[]
    for mask in range(1,16):
        mm=sum(W[k]*M[k] for k in range(4) if mask>>k&1)
        h=Q(5,16)*((4*bs_min(mask,xlo,xhi)+bs_min(mask,ylo,yhi))/5-Q(mm,160))
        v.append((h,mask))
    return max(v)

def fused_bound(xlo,xhi,ylo,yhi,high):
    py=dpy=None
    if high:py,dpy,K=pyhi,dpyhi,KH
    else:py,dpy,K=pylo,dpylo,KL
    vals=[]
    for mask in range(16):
        mm=sum(W[k]*M[k] for k in range(4) if mask>>k&1)
        Fs=lambda z:sum((W[k]*B(k,z) for k in range(4) if mask>>k&1),Q(0))
        Fsp=lambda z:sum((W[k]*Bp(k,z) for k in range(4) if mask>>k&1),Q(0))
        f=lambda z:px(z)+LAMBDA*Q(1,4)*Fs(z)
        df=lambda z:dpx(z)+LAMBDA*Q(1,4)*Fsp(z)
        h=lambda z:py(z)+LAMBDA*Q(1,16)*Fs(z)
        dh=lambda z:dpy(z)+LAMBDA*Q(1,16)*Fsp(z)
        lo=K-LAMBDA*Q(mm,512)+bernmin(f,df,xlo,xhi)+bernmin(h,dh,ylo,yhi)
        vals.append((lo,mask))
    return max(vals)

def make_leaves(box,mode):
    leaves=[]
    def split(a,d,e,f,level):
        if mode=='GLOBAL' and RECT[0]<=a<=d<=RECT[1] and RECT[2]<=e<=f<=RECT[3]:
            leaves.append((level,a,d,e,f,'INNER',0,Q(0)));return
        if mode=='GLOBAL':v,mask=global_bound(a,d,e,f);ok=v>QPUBLIC;kind='HIGH_B'
        else:
            v,mask=fused_bound(a,d,e,f,mode=='HIGH');ok=v>LIFT_THRESHOLD;kind='FUSED'
        if ok:
            leaves.append((level,a,d,e,f,kind,mask,v));return
        assert level<16,(mode,level,a,d,e,f)
        x=(a+d)/2;y=(e+f)/2
        for rect in [(a,x,e,y),(x,d,e,y),(a,x,y,f),(x,d,y,f)]:split(*rect,level+1)
    if mode=='GLOBAL':split(Q(0),Q(1),Q(0),Q(1),0)
    elif mode=='LOW':split(*LOW,0)
    else:split(*HIGH,0)
    return leaves

def to_csv(leaves):
    buf=io.StringIO(newline='')
    wr=csv.writer(buf,lineterminator='\n')
    wr.writerow(['depth','x_lo','x_hi','y_lo','y_hi','kind','mask','exact_lower_bound'])
    for depth,a,d,e,f,kind,mask,value in leaves:wr.writerow([depth,str(a),str(d),str(e),str(f),kind,mask,str(value)])
    return buf.getvalue()

def validate_partition(rows,box):
    leaves={(a,d,e,f):(dep,k,m,v) for dep,a,d,e,f,k,m,v in rows}
    assert len(leaves)==len(rows)
    def walk(a,d,e,f,depth):
        if (a,d,e,f) in leaves:
            dep,kind,mask,val=leaves.pop((a,d,e,f));assert dep==depth
            if kind=='INNER':
                assert box=='GLOBAL' and RECT[0]<=a and d<=RECT[1] and RECT[2]<=e and f<=RECT[3]
            elif box=='GLOBAL':
                v,ma=global_bound(a,d,e,f);assert (val,mask)==(v,ma) and val>QPUBLIC
            else:
                v,ma=fused_bound(a,d,e,f,box=='HIGH');assert (val,mask)==(v,ma) and val>LIFT_THRESHOLD
            return (d-a)*(f-e)
        assert depth<17
        xm=(a+d)/2;ym=(e+f)/2
        return sum((walk(*rect,depth+1) for rect in [(a,xm,e,ym),(xm,d,e,ym),(a,xm,ym,f),(xm,d,ym,f)]),Q(0))
    bounds=(Q(0),Q(1),Q(0),Q(1)) if box=='GLOBAL' else (LOW if box=='LOW' else HIGH)
    total=walk(*bounds,0);assert total==(bounds[1]-bounds[0])*(bounds[3]-bounds[2]);assert not leaves

def fixed_tag_check():
    # Exact tag signs via degree-3 Bernstein hull on each coordinate interval.
    regions=[('x',Q(11,50),Q(6,25)),('low_y',Q(1,2),Q(531,1000)),('high_y',Q(5,8),Q(127,200))]
    expected={('x',Q(1,4)):'-+++',('x',Q(3,4)):'--++',
              ('low_y',Q(1,4)):'++--',('low_y',Q(3,4)):'--++',
              ('high_y',Q(1,4)):'++--',('high_y',Q(3,4)):'---+'}
    # Note high_y relative to 3/4: B2(y)>B2(3/4) => third comparison NEGATIVE.
    for name,lo,hi in regions:
        for a in (Q(1,4),Q(3,4)):
            signs=''
            for k in range(4):
                f=lambda z:B(k,a)-B(k,z)
                df=lambda z:-Bp(k,z)
                h=(hi-lo)/3
                controls=(f(lo),f(lo)+h*df(lo),f(hi)-h*df(hi),f(hi))
                assert all(t>0 for t in controls) or all(t<0 for t in controls),(name,a,k,controls)
                signs+='+' if controls[0]>0 else '-'
            assert signs==expected[(name,a)],(name,a,signs)
    # Distinct source-tag function, exact piecewise cubic identities (no floating approximation).
    for x in (Q(11,50),Q(23,100),Q(6,25)):
        for y in (Q(1,2),Q(53,100),Q(531,1000)):
            assert c(x,y)==KL+px(x)+pylo(y)
        for y in (Q(5,8),Q(63,100),Q(127,200)):
            assert c(x,y)==KH+px(x)+pyhi(y)

def exact_budget_and_curvature():
    xL=Q(2310839408,10**10);xU=Q(2310839409,10**10)
    yL=Q(555508855,10**9);yU=Q(555508860,10**9)
    betaL=Q(15,16)*r(2,xL,yL);betaU=Q(15,16)*r(2,xU,yU)
    assert betaL<betaU
    assert betaU+Q(1,625)<QPUBLIC
    # Old E=7/5000 candidate x > .235341, y<.568564 -> c < 0.03124.
    xo=Q(235341,10**6);yo=Q(568564,10**6)
    assert r(1,xo,yo)<0
    assert Q(15,16)*r(2,xo,yo)<betaL+Q(7,5000)
    assert c(xo,yo)<QAUDIT
    # New E=1/625 endpoint bracket x_E in (.2359,.236), y_E<.571.
    xl=Q(2359,10000);xu=Q(59,250)
    yl=Q(5703,10000);yu=Q(571,1000)
    assert r(1,xl,yl)<0
    assert Q(15,16)*r(2,xl,yl)<betaL+Q(1,625)
    assert r(1,xu,yl)>0 and r(1,xu,yu)<0
    assert Q(15,16)*r(2,xu,yl)>betaU+Q(1,625)
    assert c(xl,yu)<QAUDIT
    # C' x in [.231,.236], Y in [.555,.571]. Exact rational interval bounds.
    ax=Q(231,1000);bx=Q(59,250);ay=Q(555,1000);by=Q(571,1000)
    g=lambda y:(1-y)*(3*y-1)
    N=lambda x:4*(1-x)*(1-3*x)
    assert N(bx)/g(by)>Q(29,10)
    assert N(ax)/g(ay)<Q(33,10)
    # Y'' = (4(6x-4)+(6Y-4)(Y')^2)/g(Y) < -48.
    ymax_ypp=(4*(6*bx-4)+(6*by-4)*Q(29,10)**2)/g(by)
    assert ymax_ypp < -48
    # p(x)>0.43 and c'<-0.39 on the curvature box.
    p=lambda x:(1-x)*(189-183*x)/256
    assert p(bx)-Q(3,256)*Q(33,10)>Q(39,100)
    assert Q(3,16)*(4*bx*(2-3*bx)+ay*(2-3*ay)*Q(33,10))<Q(2,5)
    bpp_upper=Q(3,16)*(4*(2-6*ax)+(2-6*ay)*Q(29,10)**2+by*(2-3*by)*(-48))
    assert bpp_upper< -3
    assert Q(372-366*ax,256)<Q(9,8)
    # Thus c''b'-c'b'' < (9/8)(2/5) -(39/100)*3 = -18/25.
    assert Q(9,8)*Q(2,5)-Q(39,100)*3 == -Q(18,25)
    # Middle y in [0.531,0.625]: (-,+) chamber strict constant-b audit descent.
    yc=Q(531,1000);xmin=RECT[0];xmax=RECT[1]
    assert p(xmax)>Q(43,100)
    assert Q(3,256)*4*(1-2*xmin)/(2*yc-1)<Q(43,100)
    # Above cusp y_dagger=(1+sqrt(13))/8 >23/40: exact square comparison.
    assert Q(23,40)>Q(1,8) and (8*Q(23,40)-1)**2<13
    assert Q(1,40)*4*(1-2*xmin)/(2*Q(23,40)-1)<Q(43,100)
    # r2 positive throughout R since B2 increasing on [0,2/3].
    assert r(2,RECT[0],RECT[2])>0
    # r0 curve left of qstar: f(x)<f(y) on both subintervals.
    f=lambda z:z*(2-3*z)/(1-z)**2
    assert f(Q(3,5))>f(Q(231084,10**6))
    assert r(0,Q(228,1000),Q(3,5))<0
    assert f(Q(5,8))>f(Q(228,1000))
    # r1=0 arc derivative Y1'<5 from interval endpoints on full R.
    assert N(RECT[0])/g(RECT[2])<5
    assert p(xmax)>Q(1,40)*5
    return {'beta_lower':str(betaL),'beta_upper':str(betaU),
            'old_cost_upper':str(c(xo,yo)),'new_cost_upper':str(c(xl,yu)),
            'curvature_explicit_upper':str(-Q(18,25))}

def run():
    fixed_tag_check()
    endpoint=exact_budget_and_curvature()
    modes=[('GLOBAL','CERTIFICATE_STAGE347B_GLOBAL.csv',193),
           ('LOW','CERTIFICATE_STAGE347B_LOW_STRIP.csv',55),
           ('HIGH','CERTIFICATE_STAGE347B_HIGH_STRIP.csv',1)]
    for mode,path,n in modes:
        rows=make_leaves(RECT,mode)
        validate_partition(rows,mode)
        assert len(rows)==n,(mode,len(rows))
        content=to_csv(rows)
        dest=OUT/path
        if dest.exists():assert dest.read_text(encoding='utf-8')==content
        else:dest.write_text(content,encoding='utf-8')
        print(mode,'leaves',n,'max_depth',max(row[0] for row in rows),'area',str(sum(((row[2]-row[1])*(row[4]-row[3]) for row in rows),Q(0))),
              'sha256',sha256(content.encode('utf-8')).hexdigest())
    print('EXACT_ENDPOINTS',endpoint)
    print('STAGE347B_GLOBAL_E_0p0016_AUTHOR_EXACT_193_55_1_PASS')

if __name__=='__main__':run()
