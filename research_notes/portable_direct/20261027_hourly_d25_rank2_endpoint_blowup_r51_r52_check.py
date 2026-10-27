"""R51/R52: exact rational endpoint and integral jet checks (author-only)."""
from math import factorial, isqrt
from fractions import Fraction as Q

def prime(n): return n > 1 and all(n % d for d in range(2, isqrt(n)+1))
def vi(n,p):
    n,v=abs(n),0
    if not n: return 10**8
    while n%p==0: n//=p; v+=1
    return v
def v(q,p): return vi(q.numerator,p)-vi(q.denominator,p)
def residue(q,p):
    if not q: return 0
    z=v(q,p)
    assert z>=0
    if z: return 0
    n=q.numerator//p**vi(q.numerator,p)
    d=q.denominator//p**vi(q.denominator,p)
    return n*pow(d,-1,p)%p
def factv(n,p):
    z=0
    while n: n//=p; z+=n
    return z
def w(k): return Q((6*k+1)*factorial(2*k)*factorial(3*k),factorial(k)**5*216**k)
def s(k): return Q((8*k+1)*factorial(4*k),factorial(k)**4*2304**k)
def a(k): return Q((6*k+7)*(2*k+1)*(3*k+1)*(3*k+2),36*(6*k+1)*(k+1)**3)
def b(k): return Q((8*k+9)*(2*k+1)*(4*k+1)*(4*k+3),288*(8*k+1)*(k+1)**3)
def P(k): return 2688*k**4+6160*k**3+4456*k**2+1166*k+85

def main():
    assert P(Q(1,4))==Q(3047,4) and P(Q(3,4))==Q(27661,4)
    assert 3047==11*277 and 27661==139*199
    cnt=0
    for p in range(13,1000):
        if p%6!=1 or not prime(p): continue
        N=(3*p-1)//4+1
        assert N+1<p
        assert vi(6*N+1,p)+factv(2*N,p)+factv(3*N,p)-5*factv(N,p)==3
        assert vi(8*N+1,p)+factv(4*N,p)-4*factv(N,p)==3
        assert (P(N)%p==0)==(p in (139,199,277))
        cnt+=1
    expected={139:(105,120,130,8,32,94,100,102,100,90),
              199:(150,189,99,62,148,66,70,36,70,116),
              277:(208,155,131,81,66,195,27,42,27,95)}
    for p in [13,19,37,139,181,199,277,373]:
        N=(3*p-1)//4+1
        A,B=w(N)/w(1),s(N)/s(1)
        aa,bb=a(N),b(N); D=aa-bb; lam=v(D,p)
        assert v(A,p)==v(B,p)==3
        assert D==Q((2*N+1)*P(N),288*(N+1)**3*(6*N+1)*(8*N+1))
        assert lam==(1 if p in expected else 0)
        qN,qNp=(aa/B-bb/A)/D,(1/A-1/B)/D
        assert min(v(qN,p),v(qNp,p))==-3-lam
        if lam: assert v(qN,p)==v(qNp,p)==-4
        A0,B0,D0=A/p**3,B/p**3,D/p**lam
        for U,V in [(Q(1),Q(0)),(Q(0),Q(1)),(w(1),s(1))]:
            dn,dnp=A*U-B*V,aa*A*U-bb*B*V
            assert qN*dn+qNp*dnp==U-V
            X,Y=dn/p**3,(dnp-aa*dn)/p**(3+lam)
            assert X==A0*U-B0*V and Y==D0*B0*V
            Vrec=Y/(D0*B0); Urec=(X+B0*Vrec)/A0
            assert (Urec,Vrec)==(U,V)
            if (U,V)==(w(1),s(1)) and lam:
                row=(N,residue(D0,p),residue(A0,p),residue(B0,p),
                     residue(p**4*qN,p),residue(p**4*qNp,p),
                     residue(dn/p**3,p),residue(dnp/p**3,p),
                     residue(X,p),residue(Y,p))
                assert row==expected[p],(p,row)
                assert (row[4]*row[6]+row[5]*row[7])%p==0
    print('PASS R51/R52: 79 target-prime classifications; 8 exact free-state cases; all 3 exceptional jets')
if __name__=='__main__': main()
