#!/usr/bin/env python3
"""Stage355-B: exact Fraction certificates for TV floor and r3=0 exclusion.

No external packages; all numerical and coverage claims are rational.
No formal proof/admission or P000 native interpretation is implied.
Run: python REPRO_STAGE355B.py [--write | --check].
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import csv
import sys

assert __debug__, "Do not disable mathematical assertions (-O is disallowed)."
HERE = Path(__file__).resolve().parent
W = (1, 3, 3, 1)
M = (61, 21, 9, 9)
B_FLOOR = F(3779, 10**6)
B_CAP = F(299, 50000)  # 0.00598
R3_STRIP_RADIUS = F(1, 2000)  # 0.0005
E_MAX = F(11, 5000)
B_STAR_UPPER = F('0.00377914')
Q = (F(29, 125), F(349, 625))


def poly_add(a,b):
    return tuple(a[i]+b[i] for i in range(4))

# z^k(1-z)^(3-k), in the ordinary power basis 0..3.
PK = (
    (F(1),F(-3),F(3),F(-1)),
    (F(0),F(1),F(-2),F(1)),
    (F(0),F(0),F(1),F(-1)),
    (F(0),F(0),F(0),F(1)),
)

PS = []
for subset in range(16):
    p = (F(0),)*4
    m = 0
    for k in range(4):
        if subset & (1 << k):
            p = poly_add(p, tuple(W[k]*u for u in PK[k]))
            m += W[k]*M[k]
    PS.append((p,F(m)))
assert tuple(sum(W[k]*PK[k][j] for k in range(4)) for j in range(4))==(F(1),F(0),F(0),F(0))
assert sum(W[k]*M[k] for k in range(4))==160


def peval(p,z):
    return ((p[3]*z+p[2])*z+p[1])*z+p[0]


def bezier_cubic(p,l,h):
    """Four exact degree-3 Bernstein coefficients on [l,h]."""
    pl,ph=peval(p,l),peval(p,h)
    dp_l=p[1]+2*p[2]*l+3*p[3]*l*l
    dp_h=p[1]+2*p[2]*h+3*p[3]*h*h
    z=(h-l)/3
    return pl,pl+z*dp_l,ph-z*dp_h,ph


def B_low(xl,xh,yl,yh):
    # b = (5/16) max_S sum_{k in S} W[k]*r_k, because sum W*r = 0.
    return max(F(5,16)*((4*min(bezier_cubic(p,xl,xh))
                           +min(bezier_cubic(p,yl,yh)))/5 -m/160)
               for p,m in PS)


def D_low(a,l,h):
    # D3(a,z) = max_S [P_S(a)-P_S(z)].
    return max(peval(p,a)-max(bezier_cubic(p,l,h)) for p,m in PS)


def C_low(xl,xh,yl,yh):
    return (63*D_low(F(1,4),xl,xh)+D_low(F(3,4),xl,xh)
            +9*D_low(F(1,4),yl,yh)+7*D_low(F(3,4),yl,yh))/256


def pwords(z):
    return tuple(peval(PK[k],z) for k in range(4))


def residuals(x,y):
    bx,by=pwords(x),pwords(y)
    return tuple((4*bx[k]+by[k])/5-F(M[k],160) for k in range(4))


def bvalue(x,y):
    return F(5,32)*sum(W[k]*abs(v) for k,v in enumerate(residuals(x,y)))


def dvalue(a,z):
    pa,pz=pwords(a),pwords(z)
    return F(1,2)*sum(W[k]*abs(pa[k]-pz[k]) for k in range(4))


def cvalue(x,y):
    return (63*dvalue(F(1,4),x)+dvalue(F(3,4),x)
            +9*dvalue(F(1,4),y)+7*dvalue(F(3,4),y))/256


def r3_corner(x,y):
    return (4*x**3+y**3)/5-F(9,160)


def split(rect,kind):
    xl,xh,yl,yh=rect
    # Factor 4 for b-floor, factor 2 for r3-stratum.
    slope = 4 if kind=='floor' else 2
    if slope*(xh-xl)>=(yh-yl):
        xm=(xl+xh)/2
        return ((xl,xm,yl,yh),(xm,xh,yl,yh))
    ym=(yl+yh)/2
    return ((xl,xh,yl,ym),(xl,xh,ym,yh))


def classify(rect,kind):
    xl,xh,yl,yh=rect
    if kind=='floor':
        return 'TV_FLOOR' if B_low(*rect)>=B_FLOOR else None
    radius = R3_STRIP_RADIUS if kind == 'strip' else F(0)
    if r3_corner(xl,yl)>radius or r3_corner(xh,yh)<-radius:
        return 'NO_R3_STRIP' if kind == 'strip' else 'NO_R3_ZERO'
    blo=B_low(*rect)
    if blo > B_CAP:
        return 'B_OVER_CAP'
    if blo > bvalue(*Q) and C_low(*rect)>cvalue(*Q):
        return 'Q_STRICT_DOMINATES'
    return None


def make_tree(kind):
    stack=[((F(0),F(1),F(0),F(1)),0)]
    out=[]
    while stack:
        rect,dep=stack.pop()
        label=classify(rect,kind)
        if label:
            out.append((*rect,label,dep))
        else:
            assert dep<80, (kind, rect, dep)
            left,right=split(rect,kind)
            stack.append((right,dep+1))
            stack.append((left,dep+1))
        assert len(stack)+len(out)<10000, "Unexpected nontermination."
    return out


def csvname(kind):
    return HERE/('CERTIFICATE_STAGE355B_B_FLOOR.csv' if kind=='floor'
                 else ('CERTIFICATE_STAGE355B_R3_DOMINATION.csv' if kind=='r3'
                 else 'CERTIFICATE_STAGE355B_R3_STRIP.csv'))


def save_cert(kind,rows):
    with csvname(kind).open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f,lineterminator='\n')
        w.writerow(['xl','xh','yl','yh','reason','depth'])
        for xl,xh,yl,yh,why,dep in rows:
            w.writerow([str(xl),str(xh),str(yl),str(yh),why,dep])


def load_cert(kind):
    with csvname(kind).open(newline='',encoding='utf-8') as f:
        data=list(csv.DictReader(f))
    return [(*(F(r[k]) for k in ('xl','xh','yl','yh')),r['reason'],int(r['depth']))
            for r in data]


def verify_coverage(rows,kind):
    assert rows
    area=F(0)
    for xl,xh,yl,yh,why,dep in rows:
        assert F(0)<=xl<xh<=1 and F(0)<=yl<yh<=1
        assert why==classify((xl,xh,yl,yh),kind), (kind,why,(xl,xh,yl,yh))
        area+=(xh-xl)*(yh-yl)
    assert area==1, (kind,'area',area)
    # Pairwise disjoint interiors + area one + closed rectangles proves full coverage.
    for i,(al,ah,bl,bh,*_) in enumerate(rows):
        for cl,ch,dl,dh,*_ in rows[i+1:]:
            assert ah<=cl or ch<=al or bh<=dl or dh<=bl, (kind,'overlap')
    return Counter(row[4] for row in rows),max(row[5] for row in rows)


def check_star():
    """Independent isolator of r0=r1=0 in the selected s>t chamber."""
    slo,shi=F('0.768916059144'),F('0.768916059145')
    tlo,thi=F('0.444491142719'),F('0.444491142727')
    def polynomial(s):
        return (F(41,16)-4*s*s)**3-(F(61,32)-4*s**3)**2
    assert polynomial(slo)<0<polynomial(shi)
    assert 0<tlo<thi<slo
    assert tlo*tlo < F(41,16)-4*shi*shi
    assert thi*thi > F(41,16)-4*slo*slo
    # s -> 4s^3+t(s)^3 is strictly increasing because
    # derivative = 12s(s-t)>0 in this isolating chamber.
    xlo,xhi=1-shi,1-slo
    ylo,yhi=1-thi,1-tlo
    def r2(x,y):
        return (4*x*x*(1-x)+y*y*(1-y))/5-F(9,160)
    assert 0<xlo<xhi<F(2,3) and 0<ylo<yhi<F(2,3)
    assert r2(xlo,ylo)>0
    # Since r0=r1=0 and sum W*r=0, r3=-3r2<0;
    # beta_*= (5/32)*(3r2+|-3r2|) = (15/16)r2.
    blo=F(15,16)*r2(xlo,ylo)
    bhi=F(15,16)*r2(xhi,yhi)
    assert blo < bhi < B_STAR_UPPER
    assert B_FLOOR<=blo # newly proved global b-floor consistency
    assert 2*B_STAR_UPPER+E_MAX-B_FLOOR < B_CAP
    return blo,bhi


def main():
    write = '--write' in sys.argv
    check = '--check' in sys.argv
    assert write ^ check, 'Select precisely one mode: --write or --check.'
    blo,bhi=check_star()
    w_b,w_c=bvalue(*Q),cvalue(*Q)
    assert w_b < F('0.00409') and w_c < F('0.03259')
    assert w_b > B_FLOOR
    summaries={}
    for kind in ('floor','r3','strip'):
        rows=make_tree(kind)
        if write: save_cert(kind,rows)
        stored=load_cert(kind)
        assert rows==stored, f'Nonmatching {kind} file'
        count,depth=verify_coverage(stored,kind)
        summaries[kind]=(len(stored),depth,dict(sorted(count.items())))
    print('STAGE355B_GLOBAL_TV_FLOOR_AND_R3_STRATUM_STRICT_DOMINATION_EXACT_PASS')
    print('world: external source-labeled Bernoulli auxiliary model; q=(x,y) in [0,1]^2')
    print('global_b_floor:',B_FLOOR,'decimal',float(B_FLOOR))
    print('star_b_interval:',str(blo),'< beta_star <',str(bhi))
    print('star_beta_upper:',B_STAR_UPPER)
    print('budget_max:',E_MAX,'per_source_b_cap:',B_CAP)
    print('r3_domination_witness: x=',Q[0],'y=',Q[1])
    print('witness_b:',w_b,'decimal',float(w_b))
    print('witness_c:',w_c,'decimal',float(w_c))
    for kind in ('floor','r3','strip'):
        n,d,ct=summaries[kind]
        print(f'certificate_{kind}: leaves={n};max_depth={d};classes={ct};exact_area=1;strict_overlap=0')
    print('theorem: for every 0<=E<=11/5000, no unrestricted global minimizer contains |r3|<=1/2000 in either source')
    print('dependency: no Stage336/342/346 global bound; P000 native X6 transfer NOT established')
    print('author_side_status: EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED')

if __name__=='__main__':
    main()
