"""D25 Fricke 6:8 first p-cutoff source. Pure Python exact modular checker."""
from math import comb

def mul(a,b,p,n):
    c=[0]*n
    for i,x in enumerate(a[:n]):
        if x:
            for j,y in enumerate(b[:n-i]):
                if y:c[i+j]=(c[i+j]+x*y)%p
    return c
def add(a,b,p,n):
    return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%p for i in range(n)]
def scale(a,s,p,n):return [(a[i] if i<len(a) else 0)*s%p for i in range(n)]
def pw(a,k,p,n):
    c=[1]+[0]*(n-1)
    while k:
        if k&1:c=mul(c,a,p,n)
        a=mul(a,a,p,n);k//=2
    return c
def inv(a,p,n):
    assert a[0]%p
    b=[pow(a[0],-1,p)]+[0]*(n-1)
    for i in range(1,n):
        b[i]=-b[0]*sum(a[j]*b[i-j] for j in range(1,min(i,len(a)-1)+1))%p
    return b
def div(a,b,p,n):return mul(a,inv(b,p,n),p,n)
def derivative(a,p,n):return [((i+1)*a[i+1])%p if i+1<len(a) else 0 for i in range(n)]
def shift(a,k,n):return [0]*k+a[:max(n-k,0)]

def formal_test(p):
    n=2*p+2
    lin=lambda c:[c,1]
    Z2=div(scale(mul(lin(9),pw(lin(8),2,p,n),p,n),108,p,n),pw(lin(12),6,p,n),p,n)
    B3=div(scale(mul(lin(8),pw(lin(9),3,p,n),p,n),256,p,n),pw([216,36,1],4,p,n),p,n)
    z=shift(Z2,2,n);w=shift(B3,3,n)
    H=div(scale(pw(lin(12),2,p,n),3,p,n),scale([216,36,1],2,p,n),p,n)
    E=add(scale(Z2,2,p,n),shift(derivative(Z2,p,n),1,n),p,n)
    ratio=shift(div(Z2,E,p,n),1,n)
    P=add(H,scale(mul(ratio,derivative(H,p,n),p,n),6,p,n),p,n)
    Q=scale(mul(mul(ratio,H,p,n),derivative(w,p,n),p,n),6,p,n)
    UW=[0]*n;B=[0]*n;Bd=[0]*n
    zk=[1]+[0]*(n-1);wk=[1]+[0]*(n-1)
    for k in range(p):
        c=comb(2*k,k)**2*comb(3*k,k)*pow(108,-k,p)%p
        d=comb(2*k,k)**2*comb(4*k,2*k)*pow(256,-k,p)%p
        UW=add(UW,scale(zk,(6*k+1)*c,p,n),p,n)
        B=add(B,scale(wk,d,p,n),p,n)
        zk=mul(zk,z,p,n);wk=mul(wk,w,p,n)
    wk=[1]+[0]*(n-1)
    for k in range(1,p):
        d=comb(2*k,k)**2*comb(4*k,2*k)*pow(256,-k,p)%p
        Bd=add(Bd,scale(wk,k*d,p,n),p,n)
        wk=mul(wk,w,p,n)
    delta=add(UW,scale(add(mul(P,B,p,n),mul(Q,Bd,p,n),p,n),-1,p,n),p,n)
    expected=[0]*(2*p)+[-pow(432,-1,p)%p]+[0]
    assert delta==expected,(p,[(i,x,y) for i,(x,y) in enumerate(zip(delta,expected)) if x!=y])
    cp=comb(2*p,p)**2*comb(3*p,p)*pow(108,-p,p)%p
    assert cp==pow(9,-1,p)
    return dict(p=p,first_coefficient=delta[2*p],next_coefficient=delta[2*p+1])

def finite_fiber(p):
    modulus=p**5; W=V=0;qa=qb=1
    ia=pow(216,-1,modulus);ib=pow(2304,-1,modulus)
    for k in range(p):
        W=(W+(6*k+1)*comb(2*k,k)**2*comb(3*k,k)*qa)%modulus
        V=(V+(8*k+1)*comb(2*k,k)**2*comb(4*k,2*k)*qb)%modulus
        qa=qa*ia%modulus;qb=qb*ib%modulus
    chi=1 if p%3==1 else -1
    residual=(2*V-W-p*chi)%modulus
    assert residual%(p**4)==0
    return dict(p=p,W_mod_p5=W,V_mod_p5=V,residual_p4=residual//p**4)

if __name__=="__main__":
    for p in (5,7,11,13,17,19,23,29,31):
        print(formal_test(p))
    for p in (19,373):
        print(finite_fiber(p))
