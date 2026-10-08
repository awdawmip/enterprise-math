#!/usr/bin/env python3
"""Driver certificate audit; no author or parent code imports.

Checks frozen rational-point and integer-root certificates against equations,
including a chord polynomial identity for the entire recorded odd orbit.
Uniform infinitude is checked separately in the review argument.
"""
from fractions import Fraction as Q
from math import gcd, isqrt, lcm
from pathlib import Path
import json

A, C = 1945, 265

def sq(x):
    x = Q(x)
    if x < 0:
        return None
    p, q = isqrt(x.numerator), isqrt(x.denominator)
    return Q(p, q) if p*p == x.numerator and q*q == x.denominator else None

def multiply_linear_factors(roots):
    cs = [Q(1)]
    for root in roots:
        out = [Q(0)]*(len(cs)+1)
        for i, coefficient in enumerate(cs):
            out[i] -= root*coefficient
            out[i+1] += coefficient
        cs = out
    return cs

def curve(p):
    x,y = p
    return y*y == x*(x-A)*(x-C)

def chord_certificate(p,q,r):
    # r is the asserted group sum. Compare all polynomial coefficients,
    # not a shared point-addition implementation.
    xp,yp = p; xq,yq = q; xr,yr = r
    if p == q:
        m = (3*xp*xp - 2*(A+C)*xp + A*C)/(2*yp)
    else:
        assert xp != xq
        m = (yq-yp)/(xq-xp)
    b = yp-m*xp
    assert m*xr+b == -yr
    curve_minus_line = [-b*b, Q(A*C)-2*m*b, -Q(A+C)-m*m, Q(1)]
    assert curve_minus_line == multiply_linear_factors([xp,xq,xr])
    for e in (0,A,C):
        assert (xp-e)*(xq-e)*(xr-e) == (m*e+b)**2

def recover_grid(datum):
    H, T = datum[:3], datum[3:]
    assert H[0]+H[2] == 2*H[1] and H[2] > H[1] > H[0]
    assert T[0]+T[2] == 2*T[1] and T[2] > T[1] > T[0]
    roots={}; disc={}
    for i in range(3):
        for j in range(3):
            if (i,j)==(1,1):
                continue
            delta2=H[i]*H[i]-4*T[j]
            assert delta2>=0
            delta=isqrt(delta2)
            assert delta*delta == delta2 and (H[i]-delta)%2 == 0
            pair=((H[i]-delta)//2,(H[i]+delta)//2)
            assert sum(pair)==H[i] and pair[0]*pair[1]==T[j]
            roots[i,j]=pair;disc[i,j]=delta
    return roots,disc

def main():
    data=json.loads(Path('offdiag_checks.json').read_text())
    seed=(Q(9),Q(2112))
    twice=tuple(map(Q,data['nontorsion_certificate']['double']))
    assert curve(seed) and curve(twice)
    chord_certificate(seed,seed,twice)
    assert 2112%11==0 and (A*A*C*C*(A-C)**2)%11==3
    assert twice[0].denominator%121==0
    assert sq(twice[0]) is not None and sq(A-twice[0]) is None
    previous=None;previous_n=None;seen=set();results=[]
    for row in data['rows']:
        n=row['n'];point=tuple(map(Q,row['point']));assert curve(point)
        if previous is None:
            assert n==1 and point==seed
        else:
            assert n==previous_n+2
            chord_certificate(previous,twice,point)
        previous,previous_n=point,n
        d,mu,nu=map(Q,[row['d'],row['mu'],row['nu']])
        assert 0<point[0]<C and d>0 and mu>0 and nu>0
        assert d*d==point[0] and d*d+mu*mu==A and d*d+nu*nu==C
        assert abs(point[1])==d*mu*nu
        h,t=Q(row['h']),Q(row['t'])
        assert h*d==132 and 4*t==(h-d)**2-841
        datum=row['datum'];D=row['D'];roots,disc=recover_grid(datum)
        assert datum[:3]==[D*(h-d),D*h,D*(h+d)]
        assert datum[3:]==[D*D*(t-210),D*D*t,D*D*(t+210)]
        assert [disc[0,j] for j in range(3)]==[41*D,29*D,D]
        assert [disc[2,j] for j in range(3)]==[47*D,37*D,23*D]
        assert disc[1,0]==D*mu and disc[1,2]==D*nu
        flatten=[z for pair in roots.values() for z in pair]
        assert gcd(*flatten)==1
        rational_roots=[Q(z,D) for z in flatten]
        assert lcm(*(z.denominator for z in rational_roots))==D
        if D>1:
            assert any(((D-1)*z).denominator>1 for z in rational_roots)
        assert roots == {tuple(map(int,k.strip('()').split(','))):tuple(v) for k,v in row['roots'].items()}
        assert Q(d,29) not in seen;seen.add(Q(d,29))
        swapped=[-x for x in reversed(datum[:3])]+datum[3:]
        _,swdisc=recover_grid(swapped)
        assert swdisc[0,1]==37*D and swdisc[2,1]==29*D
        assert swapped[1] == -datum[1] != datum[1]
        results.append({'n':n,'D_digits':len(str(D)),'recovered_root_gcd':gcd(*flatten),'signs':[0 if x==0 else 1 if x>0 else -1 for x in datum[3:]]})
    # Independent complete fixed-core zero-product candidates from the signed
    # equations h-d=+/-sqrt(841+4t), d*h=132.
    boundaries=[]
    for target_t in (210,0,-210):
        v=sq(841+4*target_t);assert v is not None
        roots=set()
        for sign in (-1,1):
            b=sign*v
            rad=sq(b*b+528);assert rad is not None
            for d in ((-b+rad)/2,(-b-rad)/2):
                if d>0:roots.add(d)
        admissible=[]
        for d in sorted(roots):
            if sq(A-d*d) is not None and sq(C-d*d) is not None:
                admissible.append(str(d))
        boundaries.append({'t':target_t,'all_positive_candidates':list(map(str,sorted(roots))),'admissible':admissible})
    assert [x for row in boundaries for x in row['admissible']]==['3']
    report={'scope':'INDEPENDENT_DRIVER_CERTIFICATE_CHECK_NOT_CROSS_BRANCH_AUDIT','author_code_imported':False,'inherited_code_imported':False,'rows':results,'boundaries':boundaries,'negative_controls':['Even multiple does not satisfy negative-factor square cut','D-1 fails denominator clearing when D>1','Factor swap changes h sign and ordered factors'],'all_passed':True}
    Path('independent_certificate_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    main()
