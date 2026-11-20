"""EC49FUX: exact finite-n sandwich and minimax dual cross-check.
Standard library only; independent rational checks on declared widths/sample counts.
"""
from fractions import Fraction as Q
from math import comb

E = Q(31597745, 1653649)
beta = Q(3, 637)
u0 = Q(21829245984, 45529434409)
uE = Q(21829245984, 45529434409 - 456083905*E)

def params(x):
    t0 = (1-x)*(1-beta*x)
    te = (1-x)*(1-beta*x+beta*E*x)
    p0,pe = 1-t0,1-te
    q0,qe = 1-u0*t0,1-uE*te
    assert 0 < pe < p0 < qe < q0 < 1
    return p0,pe,q0,qe

def mass(n,p):
    return [Q(comb(n,k))*p**k*(1-p)**(n-k) for k in range(n+1)]

def bayes(n,p,q):
    a,b=mass(n,p),mass(n,q)
    return sum(min(v,w) for v,w in zip(a,b))/2

def composite_minimax(n,p0,pe,q0,qe):
    a0,ae=mass(n,p0),mass(n,pe)
    b0,be=mass(n,q0),mass(n,qe)
    d0=[v-w for v,w in zip(b0,a0)]
    de=[v-w for v,w in zip(be,ae)]
    roots={Q(0),Q(1)}
    for v,w in zip(d0,de):
        if v != w:
            lam = v/(v-w)
            if 0 < lam < 1: roots.add(lam)
    val=lambda lam: sum(max(Q(0),(1-lam)*v+lam*w) for v,w in zip(d0,de))
    best=min((val(lam),lam) for lam in roots)
    return (1-best[0])/2,best[1]

def main():
    gap = (1-uE)-beta-uE*beta*(E-1)
    assert gap == Q(1822277955590,5180265550733) > 0
    count=0
    for n in [2,5,15,30]:
        for x in [Q(1,100),Q(3,20),Q(7,20),Q(3,5),Q(19,20)]:
            p0,pe,q0,qe = params(x)
            b=bayes(n,p0,qe)
            v,lam=composite_minimax(n,p0,pe,q0,qe)
            assert b/2 <= v <= b
            assert v >= bayes(n,p0,q0)
            assert v >= bayes(n,pe,qe)
            assert Q(0) <= lam <= Q(1)
            count+=1
            if n in (15,30) and x == Q(7,20):
                print(f'n={n} x={x} B_cross≈{float(b):.9g} V≈{float(v):.9g} lambda≈{float(lam):.9g}')
    print('PASS: '+str(count)+' exact rational minimax dual and cross-sandwich checks')

if __name__=='__main__': main()
