"""Exact independent checks for reflected residue reciprocity (author-side)."""
from fractions import Fraction
from math import comb

def rat(m):
    q=[Fraction(comb(m,i)*comb(2*m,i),2**i) for i in range(m+1)]
    c=[Fraction(0)]*(m+1); c[1]=Fraction(1,10)
    for r in range(1,m):
        c[r+1]=c[r]*Fraction(36*r*r,(6*r+5)*(3*r+2))
    R=2*sum(q[i]*c[r]*(1+6*(i-r)) for i in range(1,m+1) for r in range(1,i+1))
    B=sum(q[i]*c[r]*(6*(r-i)-1) for r in range(1,m+1) for i in range(r))
    Q=sum(q); J=sum(i*q[i] for i in range(m+1)); U=sum(c); V=sum(r*c[r] for r in range(1,m+1))
    assert R==2*(B+(Q+6*J)*U-6*Q*V)
    return R

def prime(p):
    return p>1 and all(p%d for d in range(2,int(p**0.5)+1))

def test(p):
    m=(p-1)//6
    q=[1]
    for i in range(m):
        q.append(q[-1]*(m-i)*(2*m-i)*pow(2*(i+1)**2,-1,p)%p)
    a=[1]   # independent original 216 Gauss coefficient
    for i in range(m):
        a.append(a[-1]*(6*i+1)*(3*i+1)*pow(36*(i+1)**2,-1,p)%p)
    assert a==q
    c=[0,pow(10,-1,p)]
    for r in range(1,m):
        c.append(c[-1]*36*r*r*pow((6*r+5)*(3*r+2),-1,p)%p)
    Ucum=Scum=R=0
    for i in range(1,m+1):
        Scum=(Scum+c[i]+6*Ucum)%p
        Ucum=(Ucum+c[i])%p
        R=(R+2*a[i]*Scum)%p
    prefix_Q=1; prefix_J=0; B=0
    for r in range(1,m+1):
        B=(B+c[r]*((6*r-1)*prefix_Q-6*prefix_J))%p
        prefix_Q=(prefix_Q+q[r])%p
        prefix_J=(prefix_J+r*q[r])%p
    Q=prefix_Q; J=prefix_J; U=sum(c)%p; V=sum(r*c[r] for r in range(1,m+1))%p
    assert R==2*(B+(Q+6*J)*U-6*Q*V)%p
    if p%24 in (13,19):
        assert Q==0
        assert R==(2*B+12*J*U)%p
    return (p,m,Q,J,U,B,(2*B)%p,(12*J*U)%p,R)

if __name__=="__main__":
    print("rational:",[str(rat(m)) for m in range(1,9)])
    ps=[p for p in range(13,2001) if p%24 in (13,19) and prime(p)]
    rows=[test(p) for p in ps]
    assert len(rows)==77
    for p in (13,19,43,67,373):
        print("certificate:",next(row for row in rows if row[0]==p))
    print("PASS: m=1..8 rational and",len(ps),"target prime certificates")
