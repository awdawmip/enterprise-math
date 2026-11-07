"""Exact reflected-source adjoint resonance: rational and prime tests."""
from fractions import Fraction
from math import comb

def rational(m):
    q=[Fraction(comb(m,i)*comb(2*m,i),2**i) for i in range(m+1)]
    c=[Fraction(0)]*(m+1); c[1]=Fraction(1,10)
    for r in range(1,m):
        c[r+1]=c[r]*Fraction(36*r*r,(6*r+5)*(3*r+2))
    H=[sum((1+6*(i-r))*c[r] for r in range(1,i+1)) for i in range(m+1)]
    h=[]
    for n in range(m):
        h.append((H[n]+36*n*n*(h[-1] if h else 0))/((6*n+1)*(3*n+1)))
    E=H[m]+36*m*m*h[-1]
    left=sum(q[i]*H[i] for i in range(m+1))
    P=6*m+1
    right=q[m]*E+P*sum((9*i+2)*q[i]*h[i] for i in range(m))-P*P*sum(q[i]*h[i] for i in range(m))
    assert left==right
    return m

def prime(p):
    return p>1 and all(p%i for i in range(2,int(p**0.5)+1))

def modular(p):
    m=(p-1)//6
    q=[1];c=[0,pow(10,-1,p)]
    for n in range(m):
        q.append(q[-1]*(m-n)*(2*m-n)*pow(2*(n+1)**2,-1,p)%p)
    for n in range(1,m):
        c.append(c[-1]*36*n*n*pow((6*n+5)*(3*n+2),-1,p)%p)
    H=[0]*(m+1);S=U=0
    for i in range(1,m+1):
        S=(S+c[i]+6*U)%p
        U=(U+c[i])%p
        H[i]=S
    h=[]
    for n in range(m):
        h.append((H[n]+36*n*n*(h[-1] if h else 0))*pow((6*n+1)*(3*n+1),-1,p)%p)
    E=(H[m]+36*m*m*h[-1])%p
    R=2*sum(q[i]*H[i] for i in range(m+1))%p
    assert R==2*q[m]*E%p
    return (p,m,q[m],H[m],h[-1],E,R)

if __name__=='__main__':
    assert [rational(m) for m in range(1,8)]==list(range(1,8))
    ps=[p for p in range(13,2001) if p%24 in (13,19) and prime(p)]
    rows=[modular(p) for p in ps]
    assert len(rows)==77
    for p in (13,19,43,67,373):
        print(next(row for row in rows if row[0]==p))
    print('PASS: rational m1..7 and all',len(rows),'frozen-prime adjoint certificates')
