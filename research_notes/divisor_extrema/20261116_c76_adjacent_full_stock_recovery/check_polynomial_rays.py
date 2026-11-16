"""Cross-check the unit algorithm and the two proven explicit residual formulas."""
from fractions import Fraction as F
from math import prod
import json
from check_dyadic import Units, rising, derivatives, evaluate, v2


def direct(gaps):
    first,middle,last=gaps
    c,v,w=sum(gaps)+2,middle+last+2,last+2
    def edge(n,s,k):
        rho=F(4*prod(4*j+k for j in range(s,n+1)),4**(n-s+1)*rising(s+k,n-s+1))
        a=F((s+k-1)*rising(n+k+1,3*k),28*(4*s+k-1)*rising(s+k,3*k))
        return a,a/rho
    a,t=edge(c,v,5)
    b,s=edge(v,w,3)
    W=F((w+2)*(w+3)*(w+4),840)
    l=F(4**(w-2)*rising(4,w-2),prod(4*j+1 for j in range(3,w+1)))
    parts=[k*z for k,z in zip(derivatives(a,b,W),(t,s,l))]
    def ratio(t,s,l):
        def col(j,e):
            p=(1+l*W/e)/(1+j*W)
            p=(1+s*p)/(1+b*p)
            return (1+t*p)/(1+a*p)
        return col(F(1,2),F(6))/col(F(5),F(3,32))
    return list(map(v2,parts)),v2(sum(parts)),v2(ratio(t,s,l)/ratio(0,0,0)-1)


def main():
    U=Units(18)
    cross=0
    for i in range(1,7):
        for j in range(1,7):
            for k in range(2,8):
                rows,linear,physical=direct((i,j,k))
                assert evaluate(U,(i,j,k)) == (rows,linear)
                cross+=1
    real=[]
    for h in (5,6,7,8,9):
        X=1<<h
        for i,g in enumerate([(2*X+6,2*X-2,2*X-4),(3*X-10,2*X-4,2*X-4)]):
            rows,linear,physical=direct(g)
            assert evaluate(U,g)==(rows,linear)
            assert linear==physical==([6*X+3*h-11,6*X+2*h-12][i])
            real.append((i,h,physical))
    curves=[]
    for h in (5,8,13,21,32,60,100):
        x=1<<h
        families=[(x*x+2*x-4,x*x+2*x-4,x**3-3),
                  (x**3-3*x*x+x-1,x*x-2*x+2,x*x-2*x+2),
                  (x-2,x*x-6,x**4-3*x**3+x*x-x+2)]
        for family,gs in enumerate(families):
            row,score=evaluate(U,gs)
            curves.append([family,h,score-3*min(gs),score-min(row)])
    print(json.dumps(dict(fully_cross_checked_words=cross,affine_full_residuals=real,
                          polynomial_linear_residual_controls=curves),indent=2))


if __name__=='__main__':
    main()
