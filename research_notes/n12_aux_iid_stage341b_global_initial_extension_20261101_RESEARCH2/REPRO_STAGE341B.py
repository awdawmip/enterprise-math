#!/usr/bin/env python3
"""Stage341-B: an exact continuous 193-leaf BRC/Bernoulli global localisation certificate.

Requires Python3 and SymPy; the CSV, not finite sampling, certifies the [0,1]^2 cover.
Upstream Stage329 strict concavity is a separately declared author-level dependency.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import csv
import hashlib
import sympy as s

HERE=Path(__file__).resolve().parent
CERT=HERE/'CERTIFICATE_STAGE341B.csv'
W=(1,3,3,1)
M=(61,21,9,9)
K=F(5,16)
R_X=(F(29,128),F(15,64))
R_Y=(F(69,128),F(39,64))
Q=F(109,25000)
E=F(29,50000)


def B(k,z):return z**k*(1-z)**(3-k)
def dB(k,z):return (-3*(1-z)**2,(1-z)*(1-3*z),z*(2-3*z),3*z*z)[k]
def r(k,x,y):return (4*B(k,x)+B(k,y))/5-F(M[k],160)
def b(x,y):return F(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))
def d(a,z):return F(1,2)*sum(W[k]*abs(B(k,a)-B(k,z)) for k in range(4))
def c(x,y):return (63*d(F(1,4),x)+d(F(3,4),x)+9*d(F(1,4),y)+7*d(F(3,4),y))/256

def bern_low(mask,a,b):
    """A degree-3 exact Bernstein lower bound on an *entire interval*."""
    f=lambda t:sum(W[k]*B(k,t) for k in range(4) if mask&(1<<k))
    df=lambda t:sum(W[k]*dB(k,t) for k in range(4) if mask&(1<<k))
    h=b-a
    return min(f(a),f(a)+h*df(a)/3,f(b)-h*df(b)/3,f(b))

def rect_lower(a,b,c,d):
    vals=[]
    for mask in range(1,16):
        target=sum(W[k]*M[k] for k in range(4) if mask&(1<<k))
        val=K*((4*bern_low(mask,a,b)+bern_low(mask,c,d))/5-F(target,160))
        vals.append((val,mask))
    return max(vals)

def inside(a,b,c,d):
    return R_X[0]<=a<=b<=R_X[1] and R_Y[0]<=c<=d<=R_Y[1]

def strq(z):return f'{z.numerator}/{z.denominator}'
def readq(z):return F(z)

def cover():
    leaves=[]
    def visit(a,b,c,d,depth):
        if inside(a,b,c,d):leaves.append(('INNER',depth,a,b,c,d,0,F(0)));return
        val,mask=rect_lower(a,b,c,d)
        if val>Q:leaves.append(('HIGH',depth,a,b,c,d,mask,val));return
        assert depth<23,('uncovered rectangle',a,b,c,d,val)
        midx=(a+b)/2;midy=(c+d)/2
        for xl,xh in ((a,midx),(midx,b)):
            for yl,yh in ((c,midy),(midy,d)):
                visit(xl,xh,yl,yh,depth+1)
    visit(F(0),F(1),F(0),F(1),0)
    assert sum((xh-xl)*(yh-yl) for _,_,xl,xh,yl,yh,_,_ in leaves)==1
    with CERT.open('w',newline='',encoding='utf-8') as fh:
        writer=csv.writer(fh,lineterminator='\n')
        writer.writerow(['label','depth','xlo','xhi','ylo','yhi','witness_mask','bernstein_lower'])
        for lab,dep,a,b,c,d,mask,val in leaves:
            writer.writerow((lab,dep,strq(a),strq(b),strq(c),strq(d),mask,strq(val)))
    # Independently parse back and recompute every bound and closed-square split.
    with CERT.open(newline='',encoding='utf-8') as fh:rr=list(csv.DictReader(fh))
    assert len(rr)==len(leaves)
    got=set();area=F(0)
    for row in rr:
        label=row['label'];depth=int(row['depth']);mask=int(row['witness_mask'])
        a,b,c,d=map(readq,[row['xlo'],row['xhi'],row['ylo'],row['yhi']])
        assert a<b and c<d and F(0)<=a<b<=1 and F(0)<=c<d<=1
        assert (depth,a,b,c,d) not in got
        got.add((depth,a,b,c,d));area+=(b-a)*(d-c)
        if label=='INNER':assert inside(a,b,c,d) and mask==0
        else:
            val,newmask=rect_lower(a,b,c,d)
            assert label=='HIGH' and val>Q and val==F(row['bernstein_lower']) and newmask==mask
    assert area==1
    # Complete depth-ordered quadtree: each non-leaf must have four present children.
    current={(0,F(0),F(1),F(0),F(1))}
    L=set(got)
    seen_leaves=set()
    for _ in range(24):
        if not current:break
        nxt=set()
        for dep,a,b,c,d in current:
            if (dep,a,b,c,d) in L:
                seen_leaves.add((dep,a,b,c,d));continue
            mx=(a+b)/2;my=(c+d)/2
            for xl,xh in ((a,mx),(mx,b)):
                for yl,yh in ((c,my),(my,d)):
                    nxt.add((dep+1,xl,xh,yl,yh))
        current=nxt
    assert not current
    assert seen_leaves==L and len(L)==len(rr)
    counts=Counter(lab for lab,*_ in leaves)
    return len(leaves),counts,max(item[1] for item in leaves),hashlib.sha256(CERT.read_bytes()).hexdigest()


def b_extrema(k,a,b):
    vv=[B(k,a),B(k,b)]
    if k==1 and a<F(1,3)<b:vv.append(B(k,F(1,3)))
    if k==2 and a<F(2,3)<b:vv.append(B(k,F(2,3)))
    return min(vv),max(vv)


def verify():
    assert r(2,R_X[0],R_Y[0])==F(24111,10485760)>0
    assert r(3,R_X[1],R_Y[1])==F(-7272,10485760)<0
    tagged={('x',F(1,4)):(-1,1,1,1),('x',F(3,4)):(-1,-1,1,1),('y',F(1,4)):(1,1,-1,-1),('y',F(3,4)):(-1,-1,0,1)}
    for (v,ref),signs in tagged.items():
        lo,hi=R_X if v=='x' else R_Y
        for k,sgn in enumerate(signs):
            if sgn==0:continue
            lowval,highval=b_extrema(k,lo,hi)
            assert ref>=0
            assert (B(k,ref)-highval>0) if sgn>0 else (B(k,ref)-lowval<0)
    # At the only changing tagged comparison, the two local signs meet precisely
    # at y_dagger=(1+sqrt(13))/8 inside R_Y.
    Y=s.Symbol('y');X=s.Symbol('x')
    assert s.expand(B(2,s.Rational(3,4))-B(2,Y)-(4*Y-3)*(16*Y**2-4*Y-3)/64)==0
    assert 8*R_Y[0]-1< s.sqrt(13)<8*R_Y[1]-1
    def tagD(t,a,sign):return s.expand(s.Rational(1,2)*sum(W[k]*sign[k]*(B(k,a)-B(k,t)) for k in range(4)))
    cx=(63*tagD(X,s.Rational(1,4),tagged['x',F(1,4)])+tagD(X,s.Rational(3,4),tagged['x',F(3,4)]))/256
    assert s.expand(s.diff(cx,X)+(1-X)*(189-183*X)/256)==0
    for sig,formula in [(1,3*Y*(1-Y)/64),(-1,3*Y*(18-25*Y)/256)]:
        cy=(9*tagD(Y,s.Rational(1,4),tagged['y',F(1,4)])+7*tagD(Y,s.Rational(3,4),(-1,-1,sig,1)))/256
        assert s.expand(s.diff(cy,Y)-formula)==0
    p=lambda t:(1-t)*(189-183*t)/256
    f=lambda t:t*(2-3*t)/(1-t)**2
    assert p(R_X[1])==F(458199,1048576)>F(2,5)
    assert f(R_X[1])==F(1245,2401)<F(429,625)==f(R_Y[1])
    assert F(3,256)*F(3,4)*(1-2*R_X[0])/(F(3,16)*(2*R_Y[0]-1))==F(21,64)<F(2,5)
    assert F(1,40)*F(3,4)*(1-2*R_X[0])/(F(3,16)*(2*F(23,40)-1))==F(35,96)<F(2,5)
    assert 3*F(23,40)*(18-25*F(23,40))/256<F(1,40)
    # Bound for the r1=0 graph derivative y'(x) over the enlarged R.
    ypupper=4*(1-R_X[0])*(1-3*R_X[0])/((1-R_Y[0])*(3*R_Y[0]-1))
    assert ypupper==F(16236,4661)<5
    assert F(2,5)-F(1,40)*5>0
    assert F(12,5)*(1-2*F(6,25))-F(3,5)*(2*F(2,3)-1)*5==F(31,125)>0
    # Rigorous double-zero bracketing inherited from Stage338/340.
    xl,xh=F(231083,10**6),F(231085,10**6)
    yl1,yh1=F(5555201,10**7),F(5555202,10**7)
    yl2,yh2=F(5554961,10**7),F(5554962,10**7)
    assert r(0,xl,yl1)>0 and r(0,xl,yh1)<0
    assert r(1,xl,yl1)<0 and r(1,xl,yh1)<0
    assert r(0,xh,yl2)>0 and r(0,xh,yh2)<0
    assert r(1,xh,yl2)>0 and r(1,xh,yh2)>0
    bstar_up=K*(-r(3,xl,yl2))
    assert bstar_up==F(60478550833982446319,16000000000000000000000)
    assert bstar_up+E<Q
    # The right-hand r1=0 arc at x=15/64 is beyond E=1/2000.
    assert r(1,R_X[1],F(565,1000))>0 and r(1,R_X[1],F(566,1000))<0
    b_right_low=K*(-r(3,R_X[1],F(566,1000))-r(0,R_X[1],F(566,1000)))
    assert b_right_low>bstar_up+E
    # Entire short right r1=0 arc is in Stage329's exact curvature box.
    assert R_X[0]<xl<xh<R_X[1] and R_Y[0]<yl2<yh1<R_Y[1]
    assert r(1,R_X[1],F(577,1000))<0
    # Precise rational bracketing of a nearby r3=0 obstruction.  r3 grows
    # strictly with x>0 at fixed y, so IVT puts a zero between these points.
    xlo,xhi,yy=F(56671,250000),F(45337,200000),F(771,1250)
    assert xhi-xlo==F(1,10**6)
    assert r(3,xlo,yy)<0<r(3,xhi,yy)
    # Globally |d b/dx|<=3: |B_k'|<=3, sum W=8, x-weight=4/5.
    assert b(xlo,yy)<F(4407,10**6)
    assert b(xlo,yy)+F(3,10**6)<F(441,10**5)
    return bstar_up,b_right_low


def main():
    upper,lower=verify()
    n,counts,depth,sha=cover()
    assert n==193 and counts['HIGH']==184 and counts['INNER']==9 and depth==14
    print('GLOBAL_PIN=6f405b5977bced88a276d67a47d9d87c220dad2c')
    print('EM_MAIN_PIN=c8a23c3049786196117d590abdc90560199f6911')
    print('P000_BLOB=bcc2590d3168a28f72e8b9f0f9b1f76faadcd488')
    print('PR_PREDECESSOR=51ec3d8d6af154e3afb520ab20adfaa094f4ee94')
    print('THRESHOLD_Q=109/25000; RECT_X=[29/128,15/64]; RECT_Y=[69/128,39/64]')
    print('BETA_UPPER='+strq(upper)+'; ENDPOINT_B_LOWER='+strq(lower))
    print(f'CERT_LEAVES={n}; HIGH={counts["HIGH"]}; INNER={counts["INNER"]}; MAX_DEPTH={depth}')
    print('CERT_AREA=1/1; CSV_SHA256='+sha)
    print('ALL_16_TAG_COMPARISONS_AND_CUSP=CHECKED; DERIVATIVES_AND_R1_ENDPOINT=EXACT_PASS')
    print('R3_ZERO_EXISTS_AT_Y=771/1250_X_IN=(56671/250000,45337/200000)_B_BELOW=441/100000')
    print('E_MAX=29/50000; STAGE329_STRICT_CONCAVITY_REUSED_UNREVIEWED')
    print('STAGE341B_GLOBAL_INITIAL_INTERVAL_EXTENSION_EXACT_PASS')

if __name__=='__main__':main()
