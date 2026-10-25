#!/usr/bin/env python3
"""D25 compressed Frobenius p^7 seam; nonblind auxiliary exact check.
This reads source formulas and is not independent Driver review.
"""
from math import comb, isqrt
def make_poly_tools(p,deg):
    M=p**7
    def P(x):
        return [(x%M)] + [0]*deg
    def Z():
        return [0]*(deg+1)
    z=Z(); z[1]=1
    def add(*ps):
        return [sum(q[i] for q in ps)%M for i in range(deg+1)]
    def neg(a):
        return [(-t)%M for t in a]
    def sub(a,b):
        return add(a,neg(b))
    def mul(*ps):
        ans=P(1)
        for b in ps:
            c=Z()
            for i in range(deg+1):
                for j in range(deg+1-i):
                    c[i+j]=(c[i+j]+ans[i]*b[j])%M
            ans=c
        return ans
    def inv(b):
        r=Z()
        r[0]=pow(b[0],-1,M)
        for n in range(1,deg+1):
            r[n]=(-r[0]*sum(b[j]*r[n-j] for j in range(1,n+1)))%M
        return r
    def div(a,b):
        return mul(a,inv(b))
    def power(a,n):
        if n<0: return power(inv(a),-n)
        out=P(1)
        while n:
            if n%2:out=mul(out,a)
            a=mul(a,a);n//=2
        return out
    def linear(c,k=1):
        o=P(c)
        o[1]=k%M
        return o
    return M,P,Z,z,add,sub,mul,div,power,linear

def p7check(p):
    assert p>=13 and p%6==1 and all(p%d for d in range(2,isqrt(p)+1))
    m,n=(p-1)//6,(p-1)//3
    M,P,Z,z,add,sub,mul,div,power,linear=make_poly_tools(p,4)
    def q(c):
        return (pow(c,p-1,p**8)-1)//p
    C=div(mul(linear(1),power(linear(-1,2),2),add(mul(P(30),power(z,2)),mul(P(77),z),P(40))),
          mul(P(2),linear(2),linear(1,2),linear(-1,4),linear(5,4)))
    B=P(0);carry=P(1)
    for j in range(1,5):
        B=add(B,mul(linear(6*j+7,6),carry))
        if j<4:
            num=mul(linear(2*j+3,2),linear(3*j-1,2),linear(3*j,2))
            den=mul(P(4),linear(3*j+1,2),linear(j+2),linear(3*j+11,4))
            carry=mul(carry,div(num,den))
    K=mul(power(linear(1,q(108)), -1),power(linear(1,-1),-2))
    for k in range(2,n+1):
        K=mul(K,power(linear(1,-pow(k,-1,M)),2))
    for j in range(1,n):
        K=mul(K,power(linear(1,pow(j,-1,M)),-1))
    A=mul(P(2*m),C,K)
    tail=P(1)
    for c,e in [(-1,2),(2,2),(5,2),(8,1),(11,1)]:
        tail=mul(tail,power(linear(1,pow(c,-1,M)),-e))
    tail=mul(tail,power(linear(1,q(2)),-2),power(linear(1,q(3)),-3))
    for j in range(1,n):
        tail=mul(tail,power(linear(1,-pow(j,-1,M)),2))
    for j in range(1,6):
        tail=mul(tail,linear(1,pow(j,-1,M)))
    for j in range(1,5):
        tail=mul(tail,linear(1,2*pow(j,-1,M)))
    tail=mul(tail,linear(1,2))
    for j in range(1,3):
        tail=mul(tail,power(linear(1,pow(j,-1,M)),-2))
    for j in range(1,n+5):
        tail=mul(tail,power(linear(1,pow(j,-1,M)),-1))
    L=mul(P(3*pow(220,-1,M)),z,B,tail)
    T=comb(2*p-1,p-1)%M
    R=((1-p)**2*pow(1-2*p,-1,M))%M
    raw,source_link,_,_=exact_source_direct(p)
    harmon=lambda r:sum(pow(pow(j,r,M),-1,M) for j in range(1,p))%M
    h2,h4,h6=harmon(2),harmon(4),harmon(6)
    assert h2%p==h4%p==h6%p==0
    theta,omega=h2//p,h4//p
    Tpred=(1-2*p**3*theta-p**5*omega+2*p**6*theta**2)%M
    a0,a1,a2,a3,a4=A
    ell1,ell2,ell3=L[1:4]
    pred=(
        (2*a0)*p**2+
        (2*a1+(4-2*theta)*a0)*p**3+
        (2*a2+(4-2*theta)*a1+9*a0-2*theta*ell1)*p**4+
        (2*a3+(4-2*theta)*a2+9*a1+(20-4*theta-omega)*a0-2*theta*ell2)*p**5+
        (2*a4+(4-2*theta)*a3+9*a2+(20-4*theta-omega)*a1+(44-8*theta+2*theta**2)*a0-2*theta*ell3-omega*ell1)*p**6
    )%M
    return {"p":p,"raw":raw,"pred":pred,"ok":raw==pred,"source_link_ok":source_link==0,"T_ok":T*T%M==Tpred,"theta":theta%p,"omega":omega%p,"quad_coefficient":(2*theta**2*a0)%p,"ell1":ell1%p,"ell3":ell3%p, "M":M}
def exact_source_direct(p):
    m,n=(p-1)//6,(p-1)//3
    M=p**7
    def f(a,b=1):
        return a*pow(b%M,-1,M)%M
    q=lambda c:(pow(c,p-1,p**8)-1)//p
    C=f((p+1)*(2*p-1)**2*(30*p*p+77*p+40),2*(p+2)*(2*p+1)*(4*p-1)*(4*p+5))
    B, carry=0,1
    for j in range(1,5):
        B=(B+(6*p+6*j+7)*carry)%M
        if j<4:
            carry=(carry*f((2*p+2*j+3)*(2*p+3*j-1)*(2*p+3*j),
                4*(2*p+3*j+1)*(p+j+2)*(4*p+3*j+11)))%M
    K=pow(1+p*q(108),-1,M)*pow(1-p,-2,M)%M
    for k in range(2,n+1):
        K=K*f((k-p)**2,k*k)%M
    for j in range(1,n):
        K=K*f(j,j+p)%M
    A=2*m*C*K%M
    P=1
    for c,e in [(-1,2),(2,2),(5,2),(8,1),(11,1)]:
        P=P*pow((1+p*f(1,c))%M,-e,M)%M
    P=P*pow(1+p*q(2),-2,M)*pow(1+p*q(3),-3,M)%M
    for j in range(1,n):
        P=P*f((j-p)**2,j*j)%M
    for j in range(1,6):
        P=P*f(j+p,j)%M
    for j in range(1,5):
        P=P*f(j+2*p,j)%M
    P=P*(1+2*p)%M
    for j in range(1,3):
        P=P*pow(f(j+p,j),-2,M)%M
    for j in range(1,n+5):
        P=P*pow(f(j+p,j),-1,M)%M
    L=p*f(3,220)*B*P%M
    FU=pow(1+p*q(108),-1,M)
    for k in range(2,n+1):
        FU=FU*f((k-p)**2,k*k)%M
    for j in range(1,p-1):
        FU=FU*f((j+p)**2,j*j)%M
    for j in range(1,n):
        FU=FU*f(j,j+p)%M
    T=comb(2*p-1,p-1)%M
    R=f((1-p)**2,1-2*p)
    Q=(2*m*C*FU+T*T*L)%M
    actual=(Q-A-L)%M
    return actual, (FU-T*T*R*R*K)%M, A, L
def main():
    checked=[p for p in range(13,3000)
             if p%6==1 and all(p%d for d in range(2,isqrt(p)+1))]
    assert len(checked)==206
    rows=[]
    for p in checked:
        k=p7check(p)
        assert k["ok"] and k["source_link_ok"] and k["T_ok"], (p,k)
        rows.append(k)
    assert sum(r["quad_coefficient"]!=0 for r in rows)==206
    for p in [13,19,31,37,109]:
        r=next(v for v in rows if v["p"]==p)
        print(f"p={p}: Q-H={r['raw']} mod {r['M']}; nonlinear-term mod p={r['quad_coefficient']}")
    print("PASS 206/206 exact source-vs-jet and binomial checks; nonlinear coefficient nonzero 206/206 tested")

if __name__=="__main__":
    main()
