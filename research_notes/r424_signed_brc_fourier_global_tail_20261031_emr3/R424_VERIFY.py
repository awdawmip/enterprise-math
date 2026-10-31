#!/usr/bin/env python3
"""R424 signed BRC auxiliary: exact finite checks; proof is R424_PROOF.zh-CN.md."""
from math import comb, sqrt
from fractions import Fraction
from decimal import Decimal, localcontext
import json
from pathlib import Path

def bc(n,k):
    return comb(n,k) if 0<=k<=n else 0

def delta(q,n):
    r=q+n
    return sum(comb(n,k)*(bc(2*q,r-2*k)-bc(2*q,r-2*k-1)) for k in range(n+1))

def rho(q,d):
    return Fraction(bc(2*q,q+abs(d)),comb(2*q,q))

def kernel(q,d):
    return Fraction(q*(q+1-2*d*d),(q+1)**2-d*d)

def F(q,n):
    return Fraction(q*delta(q,n),comb(2*q,q)*(1<<n))

def check():
    identity=bound=positive=zero=0
    for q in range(1,81):
        for n in range(q+1):
            lhs=F(q,n)
            rhs=sum((Fraction(comb(n,k),1<<n)*rho(q,n-2*k)*kernel(q,n-2*k) for k in range(n+1)),Fraction(0))
            assert lhs==rhs,(q,n,lhs,rhs)
            identity+=1
            if q>=2*n:
                gap=1-lhs
                assert 0<=gap<=Fraction(11*n+8,3*q),(q,n,gap)
                bound+=1
            if lhs>0: positive+=1
            elif lhs==0: zero+=1
    finite_scaling=[]
    with localcontext() as c:
        c.prec=32
        for alpha in ('0','0.25','0.5','1'):
            for q in (64,128,256,512,1024):
                n=int(sqrt(q)) if alpha=='0' else int(Decimal(alpha)*q)
                exact=F(q,n)
                val=Decimal(exact.numerator)/Decimal(exact.denominator)
                target=Decimal(1)/(Decimal(1)+2*Decimal(alpha))**Decimal('1.5')
                finite_scaling.append(dict(alpha=alpha,q=q,n=n,actual=str(+val),target=str(+target),abs_error=str(+abs(val-target))))
    tests=[]
    for s in (50,51,64,80,100,168,192,256,300,384):
        for m in sorted({1,2,3,4,min(20,s),s//2,s,2*s,max(2*s+1,3*s)}):
            r=s+m
            def H(q): return bc(r+q,2*q)*delta(q,r-q)
            D=H(s)**2-H(s-1)*H(s+1)
            assert D>0,(s,m,D)
            A=bc(r+s,2*s)
            lam=Fraction(m*(2*s)*(2*s-1)*(2*s+m+1),(m+1)*(2*s+m)*(2*s+1)*(2*s+2))
            J={h:Fraction(delta(s+h,m-h),4**(s+h)*2**(m-h)) for h in (-1,0,1)}
            assert Fraction(D,(A*4**s*2**m)**2)==J[0]**2-lam*J[-1]*J[1]
            if m==1:
                assert Fraction(D,comb(2*s,s)**2)==Fraction(4*(2*s+1)*(s**3-5*s+1),(s+1)**2*(s+2)**2)
            tests.append(dict(s=s,m=m,positive=True,normalization=True))
    assert (bc(6,4)*delta(2,1))**2-(bc(4,2)*delta(1,2))*(bc(6,6)*delta(3,0))==-5
    result=dict(status='R424_EXACT_PASS',identity_pairs=identity,linear_moment_pairs=bound,positive_kernel_pairs=positive,zero_kernel_pairs=zero,global_tail_turan_samples=tests,finite_scaling_samples=finite_scaling,negative_edge=dict(s=2,m=1,r=3,D=-5))
    Path(__file__).with_name('R424_EVIDENCE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('R424_EXACT_PASS',identity,bound,positive,zero,'global_tail_samples',len(tests),'negative_edge',-5)

if __name__=='__main__':
    check()
