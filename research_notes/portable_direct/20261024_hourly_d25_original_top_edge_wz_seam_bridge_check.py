"""Author self-check: D25 original WZ top-rank p-adic boundary, not native experiment."""
from fractions import Fraction as F
from math import factorial as fact


def residue(x, p, digits=1):
    a, b = x.numerator, x.denominator
    v = 0
    while a and a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    assert v >= 0, (p, x)
    return (a * pow(b, -1, p**digits) * p**v) % (p**digits)


def poly(m, n):
    return (27*n**4 + (324*m+180)*n**3 +
            (1836*m*m+1746*m+429)*n*n +
            (4320*m**3+5940*m*m+2706*m+412)*n +
            3456*m**4+6336*m**3+4128*m*m+1184*m+128)


def g(m, n):
    return F(4*n*poly(m,n), 9*(n+2*m+1)*(n+4*m+1)*
             (n+4*m+2)*(n+4*m+3)*(6*n+12*m+1))


def a(m):
    return F(fact(6*m), 3**(6*m)*fact(2*m)**3)


def r_terms(m, last):
    out = [F(1)]
    for n in range(last):
        out.append(out[-1]*F((4*m+2*n+1)*(3*n+1)*(3*n+2),
                              36*(n+1)*(2*m+n+1)*(4*m+n+1)))
    return out


def unit_fact(t, p):
    result = 1
    for j in range(1,t+1):
        if j%p:
            result = result*j%p
    return result


def new_tail_unit(m, p, j):
    r,n = m+1,4*m+j
    assert max(6*r,4*r+2*n,3*n,2*r+n,4*r+n) < 3*p
    num = 4*(6*n+12*r+1)*unit_fact(6*r,p)*unit_fact(4*r+2*n,p)*unit_fact(3*n,p)
    den = (pow(3,6*r,p)*unit_fact(2*r,p)*pow(216,n,p)*unit_fact(n,p)**2*
           unit_fact(2*r+n,p)**2*unit_fact(4*r+n,p))
    return num*pow(den,-1,p)%p


def check(p):
    assert p>=13 and p%6==1
    m=(p-1)//6
    R=r_terms(m,4*m+1)
    V=r_terms(m+1,4*m+4)
    endpoint=lambda r,n,rs:a(r)*(6*n+12*r+1)*rs[n]
    S0=sum(endpoint(m,n,R) for n in range(4*m+1))
    S1=sum(endpoint(m+1,n,V) for n in range(4*(m+1)+1))
    old=endpoint(m,4*m+1,R)*g(m,4*m+1)
    tails=[endpoint(m+1,4*m+j,V) for j in range(1,5)]
    assert S1-S0 == old+sum(tails)
    T4=R[4*m]/p
    Q=360*m*m+274*m+49
    c=F((2*p-1)**2*(3*m+1)*Q,
        9*(4*m+1)*(4*p-1)*(2*m+1)*(8*m+3))
    assert old/p == a(m)*T4*c
    assert residue(c,p)==p-2
    assert residue(old/p,p)==residue(-2*a(m)*T4,p)
    jets=[new_tail_unit(m,p,j) for j in range(1,5)]
    assert jets==[residue(t/(p*p),p) for t in tails]
    left=residue((S1-S0)/p,p,2)
    right=(residue(a(m)*T4*c,p,2)+p*sum(jets))%(p*p)
    assert left==right
    assert left%p != 0
    assert (residue(S1/p,p,2)-residue(S0/p,p,2))%(p*p)==left
    return (p,m,residue(a(m)*T4*c,p,2),jets,left,
            residue(S0/p,p,2),residue(S1/p,p,2))


if __name__=='__main__':
    sample=(13,19,31,37,43,61,67,73,79,97,103,127,211)
    for p in sample:
        print(check(p))
    print('PASS:',len(sample),'distinct original-endpoint rank boundaries')
