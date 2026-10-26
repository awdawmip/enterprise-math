#!/usr/bin/env python3
"""Author exact rational checks for two-chart Hasse source reduction. No native CM."""
from fractions import Fraction as F
from math import comb, factorial
CHECKS=0
def check(expr,msg):
    global CHECKS
    CHECKS+=1
    if not expr: raise AssertionError(msg)
def recurrence(m):
    p=6*m+1
    u=[[F(0) for _ in range(4)] for _ in range(p)]
    u[0][0]=F(1)
    for r in range(1,p):
        A=F(r*(2*r-p),2); B=(r-1-m)*(r-1-2*m); C=3*(r-1)-4*m
        for k in range(4):
            u[r][k]=(B*u[r-1][k]+(3*r*u[r][k-1]-C*u[r-1][k-1] if k else 0)+(2*u[r-1][k-2] if k>=2 else 0))/A
    return u
def mul(a,b):
    q=[F(0)]*4
    for i,x in enumerate(a):
        for j,y in enumerate(b[:4-i]):q[i+j]+=x*y
    return q
def exact_poch(m,r):
    p=6*m+1
    top=[F(1),F(0),F(0),F(0)];bot=top[:]
    for i in range(r):
        top=mul(mul(top,[F(i-m),F(-1)]),[F(i-2*m),F(-2)])
        bot=mul(bot,[F(i+1)-F(p,2),F(-3)])
    q=[F(0)]*4
    for k in range(4):
        q[k]=(top[k]-sum((bot[i]*q[k-i] for i in range(1,k+1)),F(0)))/bot[0]
    return [a/factorial(r) for a in q]
def modp(v,p):
    check(v.denominator%p!=0,"denominator unit")
    return v.numerator%p*pow(v.denominator%p,-1,p)%p
def hlog(m,r):
    p=6*m+1
    return (-sum((F(1,i-m) for i in range(r) if i!=m),F(0))
            -2*sum((F(1,i-2*m) for i in range(r) if i!=2*m),F(0))
            +3*sum((F(1,F(2*i+2-p,2)) for i in range(r)),F(0)))
def test(m):
    p=6*m+1; M=2*m;u=recurrence(m)
    A=lambda j:F(j*(2*j-p),2)
    B=lambda j:(j-1-m)*(j-1-2*m)
    C=lambda j:3*(j-1)-4*m
    delta=lambda j:F(3*j,1)/A(j)-F(C(j),B(j))
    c=lambda j:u[j][0]; d=lambda j:u[j][1]
    h=lambda l:u[p-l][2]; k=lambda l:u[p-l][3]
    for j in range(m+1):check(c(j)!=0,"low c unit")
    for j in range(m+1,M+1):check(c(j)==0 and d(j)!=0,"upper strip")
    for l in range(1,M+2):check(h(l)!=0,"high h unit")
    alpha=F(0);check(d(0)==0,"initial alpha")
    for j in range(1,m+1):
        alpha+=delta(j)
        check(c(j)==F(B(j),1)/A(j)*c(j-1),"low c recurrence")
        check(d(j)==alpha*c(j),"low logarithmic chart")
    check(d(m+1)==m*c(m)/A(m+1),"seam")
    for j in range(m+2,M+1):
        check(d(j)==F(B(j),1)/A(j)*d(j-1),"upper jet recurrence")
    denom=F(1)
    for i in range(4*m):denom*=F(2*i+2-p,2)
    seed=F(2*(-1)**m*factorial(m)*factorial(2*m)*factorial(3*m-1)*factorial(2*m-1),factorial(4*m))/denom
    check(h(M+1)==seed,"factorial high seed")
    beta=hlog(m,4*m);check(k(M+1)==beta*h(M+1),"high beta seed")
    for l in range(M,0,-1):
        r=p-l;beta+=delta(r)
        check(h(l)==F(B(r),1)/A(r)*h(l+1),"high recurrence")
        check(beta==hlog(m,r),"high harmonic source")
        check(k(l)==beta*h(l),"high third jet")
    for j in range(1,M+1):
        for l in range(1,M+1):
            a=c(j)*h(l);b=d(j)*h(l);e=c(j)*k(l)
            if j<=m:check(b+e==(d(j)/c(j)+k(l)/h(l))*a,"two-chart factor")
            else:check(a==0 and e==0 and b!=0,"upper band nonzero")
    def T(a,b):
        return sum((F(1,2)**(j-l)*(1+6*(j-l))*u[j][a]*u[p-l][b]
                    for j in range(1,M+1) for l in range(1,j+1)),F(0))
    direct=T(1,2)+T(0,3)
    lower=sum((F(1,2)**(j-l)*(1+6*(j-l))*c(j)*h(l)*(d(j)/c(j)+k(l)/h(l))
              for j in range(1,m+1) for l in range(1,j+1)),F(0))
    upper=sum((F(1,2)**(j-l)*(1+6*(j-l))*d(j)*h(l)
              for j in range(m+1,M+1) for l in range(1,j+1)),F(0))
    check(direct==lower+upper,"signed ordered sum")
    inf=sum((F(1,2)**(j-l)*(1+6*(j-l))*(d(j)*h(l)+c(j)*k(l))
             for j in range(1,M+1) for l in range(j+1,M+1)),F(0))
    inf_chart = sum(
        F(1,2)**(j-l) * (1+6*(j-l)) * (
            c(j)*h(l)*(d(j)/c(j)+k(l)/h(l)) if j<=m else d(j)*h(l)
        )
        for j in range(1,M+1) for l in range(j+1,M+1)
    )
    check(inf==inf_chart,"complementary infinity orientation")
    if p in [7,13,19,31,37,43,61,67,73,79,97,103]:
        check(modp(c(m),p)==comb(2*m,m)%p,"mod p c_m")
        check(modp(d(m+1),p)==m*pow(m+1,-2,p)*comb(2*m,m)%p,"mod p seam")
        for j in range(m+1,M+1):check(modp(d(j),p)!=0,"mod p first jet")
        for l in range(1,M+2):check(modp(h(l),p)!=0,"mod p high second jet")
    if m<=5:
        for r in range(p):check(u[r]==exact_poch(m,r),"independent Pochhammer coefficients")
if __name__=="__main__":
    for m in range(1,13):
        test(m)
        print("m=%d p=%d PASS"%(m,6*m+1))
    print("PASS exact assertions=%d; native CM NOT_RUN"%CHECKS)
