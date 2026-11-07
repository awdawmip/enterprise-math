"""D25: original 216/2304 weighted fourth-jet and signed Fricke exact checks.

Author-side finite-field data, NOT native experimental execution or admission.
Uses Python exact modular integers for 107 primes and SymPy rationals for both
signed rational Fricke branches. No floating point in mathematical checks.
"""
from math import comb
from fractions import Fraction
import sympy as s

LIMIT = 3000

def primes(limit):
    sieve=bytearray([1])*limit
    sieve[:2]=b'\x00\x00'
    for x in range(2,int(limit**0.5)+1):
        if sieve[x]:
            sieve[x*x:limit:x]=bytes(len(sieve[x*x:limit:x]))
    return (x for x in range(5,limit) if sieve[x])

def original_jets(p, kind):
    x0=pow(2 if kind=="A" else 9,-1,p)
    invx=pow(x0,-1,p)
    derivatives=[0]*5
    term=1
    for j in range(p):
        obs=term*(1+(6 if kind=="A" else 8)*j)%p
        fall=1
        xinv=1
        for d in range(5):
            if d:
                fall=fall*(j-d+1)%p
                xinv=xinv*invx%p
            derivatives[d]=(derivatives[d]+obs*fall*xinv)%p
        if j<p-1:
            if kind=="A":
                num=(2*j+1)*(3*j+1)*(3*j+2)
                den=18*(j+1)**3
            else:
                num=(4*j+1)*(2*j+1)*(4*j+3)
                den=32*(j+1)**3
            term=term*x0*num*pow(den,-1,p)%p
    assert derivatives[1]!=0
    return derivatives

def check_prime(p):
    assert p%24 in (13,19)
    k=(p-5)//8 if p%8==5 else (p-3)//8
    q=pow(9,-1,p)
    h=sum(comb(3*k+1,j)*comb(k,j)*pow(q,j,p) for j in range(k+1))%p
    dh=sum(j*comb(3*k+1,j)*comb(k,j)*pow(q,j-1,p) for j in range(1,k+1))%p
    assert h==0 and dh!=0,(p,k,h,dh)
    a=original_jets(p,"A")
    b=original_jets(p,"B")
    assert a[0]==b[0]==0,(p,a[0],b[0])
    A=[Fraction(1),Fraction(4,3),Fraction(116,9),Fraction(1520,27)]
    B=[Fraction(1),Fraction(-99,16),Fraction(29403,256),Fraction(-12026313,4096)]
    def reduce(q):return q.numerator*pow(q.denominator,-1,p)%p
    assert [x*pow(a[1],-1,p)%p for x in a[1:]]==[reduce(x) for x in A],('A',p,a)
    assert [x*pow(b[1],-1,p)%p for x in b[1:]]==[reduce(x) for x in B],('B',p,b)
    return p,a[1:],b[1:],dh

def check_fricke():
    t=s.symbols("t"); rt=s.sqrt(2)
    z=108*t**2*(t+9)*(t+8)**2/(t+12)**6
    w=256*t**3*(t+8)*(t+9)**3/(t*t+36*t+216)**4
    dz=[s.diff(z,t,j) for j in range(1,5)]
    dw=[s.diff(w,t,j) for j in range(1,5)]
    Ar=(s.Rational(4,3),s.Rational(116,9),s.Rational(1520,27))
    Br=(-s.Rational(99,16),s.Rational(29403,256),-s.Rational(12026313,4096))
    def chain(ds,ratios):
        a,b,c,d=ds
        r2,r3,r4=ratios
        R=r2*a+b/a
        S=r3*a*a+3*r2*b+c/a
        U=r4*a**3+6*r3*a*b+3*r2*b*b/a+4*r2*c+d/a
        return R,S,U
    output=[]
    for eps in (1,-1):
        T=eps*6*rt
        assert s.simplify(z.subs(t,T)-s.Rational(1,2))==0
        assert s.simplify(w.subs(t,T)-s.Rational(1,9))==0
        x=[s.simplify(d.subs(t,T)) for d in dz]
        y=[s.simplify(d.subs(t,T)) for d in dw]
        Ra,Sa,Ua=chain(x,Ar)
        Rb,Sb,Ub=chain(y,Br)
        ell=s.simplify((Ra-Rb)/2)
        q=s.simplify((Sa-Sb-3*ell*Rb)/3)
        r=s.simplify((Ua-Ub-4*ell*Sb-6*q*Rb)/4)
        log3=s.simplify(r-3*ell*q+2*ell**3)
        expected=[
          -s.Rational(5,4)+eps*s.Rational(11,12)*rt,
          s.Rational(65,9)-eps*s.Rational(245,48)*rt,
          -s.Rational(6697,72)+eps*s.Rational(3157,48)*rt,
          -s.Rational(7829,144)+eps*s.Rational(66431,1728)*rt
        ]
        for actual,expect in zip((ell,q,r,log3),expected):
            assert s.simplify(actual-expect)==0,(eps,actual,expect)
        output.append((eps,expected[2],expected[3]))
    return output

if __name__=="__main__":
    rows=[check_prime(p) for p in primes(LIMIT) if p%24 in (13,19)]
    x13=sum(p%24==13 for p,*_ in rows)
    x19=len(rows)-x13
    print(f"PASS original 3F2 weighted derivatives through fourth, p<{LIMIT}: 13-class {x13}, 19-class {x19}, total {len(rows)}")
    print("Root checks for p≡19 are finite observations, NOT a universal root proof.")
    for rec in rows:
        if rec[0] in (13,19,37,43,109,373):print(rec)
    print("PASS exact Fricke signed fourth-jet:",check_fricke())
