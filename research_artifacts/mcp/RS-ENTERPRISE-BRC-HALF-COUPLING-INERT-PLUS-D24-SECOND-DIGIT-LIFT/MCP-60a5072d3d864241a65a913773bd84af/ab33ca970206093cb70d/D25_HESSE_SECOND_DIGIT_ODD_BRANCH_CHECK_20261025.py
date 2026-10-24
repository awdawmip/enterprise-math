"""Exact author regression: source-labeled D25 Green second-digit branch split.
Standard-library integer arithmetic; not native CM/DP, Lean or independent review.
"""
from math import comb

PRIMES=(13,19,37,43,61,67,211,373)
EXPECTED={
13:(2,71,8,6,10),19:(14,41,3,98,16),
37:(30,1025,27,655,26),43:(20,264,22,1210,1),
61:(27,1912,42,753,49),67:(8,867,64,666,36),
211:(22,20510,28,26418,200),373:(40,34975,173,99504,0)}

def plus(a,b,q):
    out=[0]*max(len(a),len(b))
    for i,v in enumerate(a):out[i]=(out[i]+v)%q
    for i,v in enumerate(b):out[i]=(out[i]+v)%q
    return out

def mul(a,b,q):
    out=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):out[i+j]=(out[i+j]+u*v)%q
    return out

def at_one_minus_four_y(coeff,q):
    out=[0]
    for v in reversed(coeff):
        out=mul(out,[1,-4],q)
        out[0]=(out[0]+v)%q
    return out

def recurrence(k,q,initial):
    old,new=[initial],[1]
    for _ in range(2,k+1):
        old,new=new,plus(new,[0]+[-v for v in old],q)
    return new

def evaluate(a,y,q):
    return sum(v*pow(y,i,q) for i,v in enumerate(a))%q

def derivative(a,y,q):
    return sum(i*v*pow(y,i-1,q) for i,v in enumerate(a) if i)%q

def integrate_at(a,y,q):
    return sum(v*pow(i+1,-1,q)*pow(y,i+1,q) for i,v in enumerate(a))%q

def verify(p):
    m=(p-1)//6;n=2*m; q=p*p; r=p**3
    assert 6*m+1==p and m>=2
    c=[1]
    for k in range(n):
        c.append(c[-1]*(3*k+1)*(3*k+2)*(3*k+3)
                 *pow(27*(k+1)**3,-1,r)%r)
    # Route A: original factorial coefficients and original X=(1-t)/2 parity.
    x=[0]*(n+1)
    for k,v in enumerate(c):
        a=v*pow(2,-k,r)%r
        for j in range(k+1):
            x[j]=(x[j]+(-1)**j*a*comb(k,j))%r
    assert all(x[j]%p==0 for j in range(1,n+1,2))
    fullG=at_one_minus_four_y([x[j]%q for j in range(0,n+1,2)],q)
    fullPhi=at_one_minus_four_y([2*(x[j]//p)%p
                                   for j in range(1,n+1,2)],p)
    G=fullG[:m+1];Phi=fullPhi[:m]
    assert not any(v%q for v in fullG[m+1:])
    assert not any(v%p for v in fullPhi[m:])
    F=recurrence(n-1,q,1)
    S=recurrence(n,q,2)
    C=(p+1)*c[-1]*pow(9,-1,q)%q

    # Route B: separately verified symmetric terminal resonance and odd Green inverse.
    reconstructed=[0]*(m+1)
    reconstructed[m]=(-1)**m*c[-1]%q
    for j in range(m-1,-1,-1):
        reconstructed[j]=(9*((j+1)**2*reconstructed[j+1]+
                         p*pow(2,-1,q)*C*S[j])*
                         pow((6*j+1)*(6*j+2),-1,q))%q
    assert reconstructed==G,("symmetric",p)
    beta=[0]*(m+1)
    for j in range(m-1,-1,-1):
        lam=(6*j+4)*(6*j+5)*pow(9,-1,p)%p
        fj=(-1)**j*comb(n-1-j,j)%p
        beta[j]=((j+1)**2*beta[j+1]-fj)*pow(lam,-1,p)%p
    assert Phi==[(C%p)*v%p for v in beta[:m]],("odd",p)

    y=pow(8,-1,q)
    ksym=(-C*integrate_at(mul(F,G,q),y,q))%q
    odd_integral=integrate_at(mul([v%p for v in S],Phi,p),y%p,p)
    todd=(-C*pow(2,-1,p)*odd_integral)%p
    total=(ksym+p*todd)%q
    e=(-evaluate(Phi,y%p,p)+
         pow(4,-1,p)*derivative(Phi,y%p,p))%p
    out=(C%p,ksym,todd,total,e)
    assert out==EXPECTED[p],(p,out,EXPECTED[p])
    if p==373:
        assert odd_integral==10 and evaluate(Phi,y%p,p)==243
        assert derivative(Phi,y%p,p)==226
        assert ksym+p*todd==99504
    return (p,*out)

if __name__=="__main__":
    for p in PRIMES:
        print("p=%d C=%d Ksym=%d Todd=%d K=%d E=%d PASS"%verify(p))
