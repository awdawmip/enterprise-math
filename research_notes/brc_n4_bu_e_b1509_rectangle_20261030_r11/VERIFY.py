#!/usr/bin/env python3
"""Exact new BRC N=4 BU E-optimal open rectangle above b=3/20.
Requires the specifically inherited, author-side observable L0/L3 lower-bound lemmas.
Only Fractions and exact SymPy; all 16 Q/P source leaves reconstructed below.
"""
from fractions import Fraction as F
from collections import defaultdict
import sympy as S

a,b,u=S.symbols('a b u', real=True)
k=S.Rational(343,1000)
d=(1-a)/3
D=b-d
C=(7-a-21*b)/(4*a+12*b+2)
E=S.factor(D*C/4)
H=S.factor(b*(2*a-7*b)/(8*(a+2*b)))
L0=(4*a-14*b-3*a*u-(a+3*b)*u*u)/(2*(23-2*u))
L3=u*(a-(a+3*b)*u)/(2*(7-2*u))
G=5*a*a+8*a*b-21*b*b-2*b-5
N0=7566202*a*a+33042212*a*b-12022649*a+31030818*b*b-92451947*b+13016500
f1=353*a+1059*b-500
f2=1186*a+12558*b-3157
checks={
    'E_source_formula':S.cancel(E-(a+3*b-1)*(7-a-21*b)/(12*(4*a+12*b+2))),
    'capacity_vs_delta':S.cancel(E-d-G/(8*(2*a+6*b+1))),
    'L0_exact_numerator':S.cancel((L0.subs(u,k)-E)-N0/(44628000*(2*a+6*b+1))),
    'L3_exact_factor':S.cancel((L3.subs(u,k)-E)-f1*f2/(5412000*(2*a+6*b+1))),
    'L3_at_C':S.cancel(L3.subs(u,C)-E),
    'switch_comparator':S.cancel(E-H-(1-a)*(a*a+38*a*b-7*a+105*b*b-14*b)/
                                 (24*(a+2*b)*(2*a+6*b+1))),
    'L0_derivative':S.cancel(S.diff(L0,u) -
       (a*(2*u*u-46*u-61)+b*(6*u*u-138*u-28))/(2*(2*u-23)**2)),
    'L3_derivative':S.cancel(S.diff(L3,u) -
       (a*(2*u*u-14*u+7)+b*(6*u*u-42*u))/(2*(2*u-7)**2)),
}
assert all(x==0 for x in checks.values()),checks

# Entire closed rational parameter rectangle: a in [0.9619,0.9621],
# b in [0.15085,0.15095]. Derivative bounds certify whole continuum.
loA,hiA=F(9619,10000),F(9621,10000)
loB,hiB=F(15085,100000),F(15095,100000)
def ev(expr,aa,bb):return S.cancel(expr.subs({a:S.Rational(aa),b:S.Rational(bb)}))
assert ev(S.diff(N0,a),loA,loB)==S.Rational(37588140439,5000)>0
assert ev(S.diff(N0,b),hiA,hiB)==-S.Rational(256469154403,5000)<0
assert ev(N0,loA,hiB)==S.Rational(13503997881,8000000)>0
assert ev(f1,hiA,hiB)==-S.Rational(10453,20000)<0
assert ev(f2,hiA,hiB)==-S.Rational(1203193,10000)<0
assert ev(S.diff(G,a),loA,loB)>0 and ev(S.diff(G,b),hiA,loB)<0
assert ev(G,loA,hiB)==S.Rational(595563,80000000)>0
# C falls with a,b on this box; 0<k<C<1 and D>0.
Ca=S.factor(S.diff(C,a));Cb=S.factor(S.diff(C,b))
assert all(ev(expr,aa,bb)<0 for expr in (Ca,Cb) for aa in (loA,hiA) for bb in (loB,hiB))
assert ev(C,hiA,hiB)==S.Rational(57359,153196)>k
assert ev(C,loA,loB)==S.Rational(19135,51052)<1
assert loB-(1-loA)/3==F(2763,20000)>0
assert hiB<F(1) and hiA<F(1)
# Strict non-overlap: beyond predecessor b<=3/20, below a>=193/200
# latest T-switch box, and below exact high-rho b/a region.
rho=(S.sqrt(5889)-25)/329
assert loB>F(3,20) and hiA<F(193,200)
assert S.simplify(rho-S.Rational(hiB)/S.Rational(loA))>0

# The exact full source-labelled sixteen-leaf dual-law tree.
q2={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
ratios={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
        'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaves=[(cat,j,l,q2[cat]/4,q2[cat]/4*ratios[cat][j])
        for cat in ('AU','AV','BU','BV') for j in range(2) for l in range(2)]
assert len(leaves)==16 and all(row[3]>0 and row[4]>0 for row in leaves)
assert sum(row[3] for row in leaves)==sum(row[4] for row in leaves)==1

def observed(law,first,second,target=False):
    out=defaultdict(F)
    for cat,j,l,q,p in leaves:
        m=q if law=='Q' else p
        z=int(cat=='BU')
        x=first[cat[0]]; y=second[cat]
        out[(1,'Q',0)]+=m*(1-x)
        out[(2,'Q',0)]+=m*x*(1-y)
        out[(3,'Q' if z else 'P',z)]+=m*x*y
    assert sum(out.values())==1
    return out

def tv(x,y):return sum(abs(x.get(z,F(0))-y.get(z,F(0))) for z in set(x)|set(y))/2

cases=[(F(481,500),F(1509,10000)),(loA,loB),(loA,hiB),(hiA,loB),(hiA,hiB)]
for aa,bb in cases:
    dd=(1-aa)/3; BB=bb-dd
    cc=(7-aa-21*bb)/(4*aa+12*bb+2)
    UU=BB*(1+cc); VV=BB
    ee=BB*cc/4
    assert 0<BB<=bb<1 and 0<cc<1 and 0<UU<=1 and 0<VV<=BB
    ft={'A':aa,'B':bb}
    fg={'A':F(1),'B':BB}
    f2={'AU':F(1),'AV':F(0),'BU':F(0),'BV':F(0)}
    g2={'AU':cc,'AV':UU,'BU':cc,'BV':F(1)} # U/A=U as A=1, V/B=1
    assert g2['AU']==g2['BU']
    for law in ('Q','P'):
        Fobs=observed(law,ft,f2,True)
        Gobs=observed(law,fg,g2)
        assert tv(Fobs,Gobs)==ee,(aa,bb,law,tv(Fobs,Gobs),ee)
        if aa==F(481,500) and bb==F(1509,10000):
            keys=((1,'Q',0),(2,'Q',0),(3,'P',0),(3,'Q',1))
            signed=tuple(Fobs.get(key,F(0))-Gobs.get(key,F(0)) for key in keys)
            expected=((dd,ee-dd,F(0),-ee) if law=='Q' else (F(0),F(0),ee,-ee))
            assert signed==expected,(law,signed,expected)
            print('ANCHOR_FULL_SIGNED',law,tuple(str(z) for z in signed))
    print('FULL_16LEAF_TV_CASE',str(aa),str(bb),str(ee))

AA,BB=F(481,500),F(1509,10000)
Eanchor=ev(E,AA,BB)
Hanchor=ev(H,AA,BB)
assert Eanchor==S.Rational(118981577,9190560000)
assert Eanchor-Hanchor==-S.Rational(5289809,1161502972800)<0
print('SOURCE_LEAVES',len(leaves),'P_Q_TOTALS',sum(row[4] for row in leaves),sum(row[3] for row in leaves))
print('SYMBOLIC_IDENTITIES',len(checks))
print('GLOBAL_BOX_N0_MIN',ev(N0,loA,hiB),'GLOBAL_BOX_G_MIN',ev(G,loA,hiB))
print('ANCHOR',f'a={AA}',f'b={BB}',f'E={Eanchor}',f'H={Hanchor}',f'H_minus_E={Hanchor-Eanchor}')
print('PASS_BRC_N4_BU_E_OPTIMAL_B1509_NEW_RECTANGLE_20261030')
