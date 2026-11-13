#!/usr/bin/env python3
"""R354: exact symbolic and r<=24 audit of BRC top three Newton differences.
Original full signed K/J source from R346_verify.py on the same PR branch.
Author-side conditional result, NOT independent mathematical admission.
"""
import json,sys
from fractions import Fraction
from hashlib import sha256
from math import factorial,comb
from pathlib import Path
import sympy as sp
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE.parent/'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import C,J,K,add,mul,forward_differences,eval_newton

def check_symbolic():
    y,z=sp.symbols('y z');x=(1-y)/2;t=y*z
    polys=lambda a:sp.expand(sum(sp.Rational(c)*t**i for i,c in enumerate(a)))
    Kpoly=sp.Poly(sp.expand(sum(polys(K(i))*x**i for i in range(1,13))),y)
    Npoly=sp.Poly(sp.expand(1+t+sum(polys(J(i))*x**i for i in range(1,11))),y)
    E=[sp.factor(-Kpoly.nth(i+1)) for i in range(4)]
    N=[sp.factor(Npoly.nth(i)) for i in range(3)]
    assert sp.simplify(E[0]-(1-sp.Rational(5,4)*z))==0
    assert sp.simplify(E[1]-z)==0
    assert sp.simplify(E[2]-(z/4-z**2+sp.Rational(11,16)*z**3))==0
    assert sp.simplify(E[3]-z**2*(3*z-8)*(3*z-2)/8)==0
    assert sp.simplify(N[2]+z*(5*z-2)/2)==0
    z0=sp.Rational(4,5);a=-z0
    assert E[2].subs(z,z0)==-sp.Rational(11,125)
    assert sp.diff(E[2],z).subs(z,z0)==-sp.Rational(3,100)
    assert E[3].subs(z,z0)==-sp.Rational(112,625)
    g1=sp.expand(N[1]*E[0]-E[1])
    g2=sp.expand(N[2]*E[0]**2-E[1]*g1-E[2]*E[0])
    assert g1==-z and sp.diff(g2,z,2).subs(z,z0)==-sp.Rational(23,40)
    r,j,m=sp.symbols('r j m',integer=True)
    n=r-j;A=r-m+j;B=2*r-j
    S1=j*(A-(j-1)/2);S2=n*(B-(n-1)/2)/2
    V1=j*A**2-A*j*(j-1)+j*(j-1)*(2*j-1)/6
    V2=(n*B**2-B*n*(n-1)+n*(n-1)*(2*n-1)/6)/4
    T=sp.factor(((S1+S2)**2-V1-V2)/2)
    T0=sp.expand(T.subs(m,0))
    T1=sp.expand(sp.diff(T,m).subs(m,0))
    T2=sp.expand(sp.diff(T,m,2).subs(m,0)/2)
    assert sp.simplify(T1+j*(3*j**2-j+3*r**2-3*r-2)/4)==0
    assert sp.simplify(T2-j*(j-1)/2)==0
    v=(69*j+11)/80
    h=(4761*j*j-1165*j-8474)/6400
    Z=sp.expand(T0+T1*v+T2*h)
    from sympy.functions.combinatorial.numbers import stirling
    msum=0
    for (d,),coef in sp.Poly(Z,j).terms():
        moment=sum(stirling(d,k,kind=2)*sp.ff(r,k)*(-sp.Rational(2,3))**k for k in range(d+1))
        msum+=coef*moment
    second=sp.factor(msum)
    assert second==r*(r-1)*(1323*r*r+1525*r-3542)/5400
    def tcoef(x):return x*(7*x+3)/10
    def scoef(x):return x*(x-1)*(1323*x*x+1525*x-3542)/5400
    def cb(x,k):return sp.prod(x-i for i in range(k))/factorial(k)
    Aa=2*scoef(r)+3*(r-1)*tcoef(r)+5*cb(r,2)+(tcoef(r)+r)*(tcoef(r)+2*r)
    Bb=scoef(r-1)+2*(r-2)*tcoef(r-1)+4*cb(r-1,2)+scoef(r+1)+r*tcoef(r+1)+cb(r+1,2)+(tcoef(r-1)+2*(r-1))*(tcoef(r+1)+r+1)
    cQ=sp.factor((r+1)*Aa-r*Bb)
    assert cQ==r*(1323*r**3+5582*r*r+822*r+133)/1350
    bQ=r*(7*r+16)/5
    ratio=sp.factor((cQ+bQ*cb(2*r-1,2)+cb(2*r,3)+3*cb(2*r,4))/(2*r*(2*r-1)))
    assert sp.simplify(ratio-(7803*r**3+2252*r*r-5523*r+3328)/(2700*(2*r-1)))==0
    return {'E3':str(E[3]),'N2':str(N[2]),'g2_second_at_z0':'-23/40',
            'H_third_ratio':str(second),'Q_third_over_top':str(ratio)}

def check_finite(max_r=24):
    hmax=max_r+1;smax=3*hmax+2;lim=2*hmax+2
    KK=[None]+[K(i) for i in range(1,13)]
    B=[[1,1]]
    for ss in range(1,smax+1):
        p=J(ss)
        for i in range(1,min(ss,12)+1):p=add(p,mul(KK[i],B[ss-i],lim),lim)
        B.append(p)
    L={}
    for r in range(hmax+1):
        vals=[]
        for u in range(r+2):
            q=r+u
            D=sum((-1)**(u-w)*C(u,w)*2**(q-w)*B[q+w][q] for w in range(u+1))
            vals.append(Fraction(D,5**u))
        ds=forward_differences(vals)
        assert ds[-1]==0 and ds[-2]==6**r
        if r>=2:
            a=Fraction(ds[r],factorial(r))
            e2=Fraction((r*(r-1)//2)**2-r*(r-1)*(2*r-1)//6,2)
            c=Fraction(ds[r-2],factorial(r-2))-Fraction(ds[r-1],factorial(r-1))*comb(r-1,2)+a*e2
            assert c/a==Fraction(r*(r-1)*(1323*r*r+1525*r-3542),5400)
        scale=[x*5**r for x in ds[:-1]]
        assert all(x.denominator==1 for x in scale)
        L[r]=eval_newton([int(x) for x in scale],2*max_r+3)
    rows=[]
    for r in range(1,max_r+1):
        vals=[L[r][u+1]*L[r][u+2]-L[r-1][u+2]*L[r+1][u+1] for u in range(2*r+1)]
        ds=forward_differences(vals)
        assert all(x>0 for x in ds)
        assert ds[-1]==30**(2*r)*comb(2*r,r)//(r+1)
        assert Fraction(ds[-2],ds[-1])==Fraction(17*r+11,10)
        assert Fraction(ds[-3],ds[-1])==Fraction(7803*r**3+2252*r*r-5523*r+3328,2700*(2*r-1))
        rows.append(f'{r},{ds[-3]},{ds[-2]},{ds[-1]}')
    return {'r_range':[1,max_r],'total':max_r,'top3_rows_sha256':sha256(('\n'.join(rows)+'\n').encode()).hexdigest(),'signed_B_smax':smax}

if __name__=='__main__':
    symbolic=check_symbolic()
    finite=check_finite()
    result={'schema':'R354_TOP3_AUTHOR_EXACT_AUDIT_V1','conditional_on':'R348 A1-A5 unreviewed',
            'native_X6_claim':False,'symbolic':symbolic,'finite':finite}
    (BASE/'R354_TOP3_EVIDENCE.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print('R354_TOP3_PASS',json.dumps(result,ensure_ascii=False))
