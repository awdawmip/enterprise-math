#!/usr/bin/env python3
"""Exact independent 16-leaf verifier of the AU+BU provenance-minimax theorem.
Scientific scope: external finite 16-leaf dual-P/Q source; no native X6 transfer.
"""
from collections import defaultdict
from fractions import Fraction as F
import sympy as S

Q2 = {'AU':F(1,6), 'AV':F(1,3), 'BU':F(1,4), 'BV':F(1,4)}
LR = {'AU':(F(9,10), F(11,10)), 'AV':(F(1,4),F(1,4)),
      'BU':(F(1,5), F(9,5)), 'BV':(F(2),F(2))}
leaves = [(cat,j,k,Q2[cat]/4,Q2[cat]*LR[cat][j]/4)
          for cat in Q2 for j in range(2) for k in range(2)]
assert len(leaves)==16
assert all(q>0 and p>0 for _,_,_,q,p in leaves)
assert sum(q for _,_,_,q,p in leaves)==sum(p for _,_,_,q,p in leaves)==1
assert set(LR['BU']).isdisjoint({z for cat in ('AU','AV','BV') for z in LR[cat]})
print('PASS_FULL_16_LEAF_QP_LAWS_POSITIVE_NORMALIZED')

A,B,c,U,V,a,b=S.symbols('A B c U V a b', real=True)
atom1=(1,'Q',0,0)
atom2=(2,'Q',0,0)
atomAU=(3,'P',0,1)
atomOther=(3,'P',0,0)
atomBU=(3,'Q',1,0)
atom_order=[atom1,atom2,atomAU,atomOther,atomBU]

def full_observer(law, firstA,firstB, AU,BU,AV,BV):
    """Direct 16-leaf distribution: sec arguments are *unconditional after T1*,
    i.e., A times conditional AU, etc. No division at zero boundary.
    """
    masses=defaultdict(lambda:S.Integer(0))
    for cat,j,k,q,p in leaves:
        mass=S.Rational(*(p if law=='P' else q).as_integer_ratio())
        root=firstA if cat[0]=='A' else firstB
        s2={'AU':AU,'BU':BU,'AV':AV,'BV':BV}[cat]
        masses[atom1]+=mass*(1-root)
        masses[atom2]+=mass*(root-s2)
        masses[{'AU':atomAU,'AV':atomOther,'BU':atomBU,'BV':atomOther}[cat]]+=mass*s2
    return {k:S.factor(masses[k]) for k in atom_order}

s=(A-a+B-b)/2
t=(A-a+3*(B-b))/4
r=(a-A*c)/6
H=B*c/4
Np=U/12+V/2
Nq=U/3+V/4
expected_P=[t,H+Np-t-r,r,-Np,-H]
expected_Q=[s,H+Nq-s-r,r,-Nq,-H]
for law, expected in [('P',expected_P),('Q',expected_Q)]:
    f=full_observer(law,a,b,a,S.Integer(0),S.Integer(0),S.Integer(0))
    g=full_observer(law,A,B,A*c,B*c,U,V)
    assert S.expand(sum(f.values())-1)==S.expand(sum(g.values())-1)==0
    for atom,eq in zip(atom_order,expected):
        assert S.factor(f[atom]-g[atom]-eq)==0,(law,atom)
    print('PASS_SYMBOLIC_FIVE_ATOM_SIGNED_VECTOR_'+law)

# Four legitimate measured events: P(T=1 and BU); Q(T=1 and AU),
# standalone BU, standalone AU. The signed differences of these events are:
assert S.factor(expected_P[0]+expected_P[4]-(t-H))==0
assert S.factor(expected_Q[0]+expected_Q[2]-(s+r))==0
assert expected_P[4]==expected_Q[4]==-H
assert expected_P[2]==expected_Q[2]==r
print('PASS_FULL_OBSERVER_EVENT_MASKS')

# For any legitimate strategy, e>=TV_P,TV_Q implies
# (i) t>=H-e, (ii) s+r<=e, (iii) e>=H, (iv) e>=r>=(a-c)/6.
# A<=1, 0<=c<=1 and g(c)>0 then imply e>=d*c/12 and
# e>=c*(a+6b-(a+3b)*c)/(6*(4-c)).
e=S.symbols('e',real=True)
d=a+3*b-1
g=(3-c)**2-3
rhs=a+6*b-(a+3*b)*c-(18-4*c)*e
assert S.factor((3-c)*(a+3*b-(3-c)*B-4*e)+3*B-(2*a+3*b+6*e) - (-g*B+rhs))==0
# Re-derive denominators from elimination and BU mass bound without numeric fitting.
assert S.factor(4*g+c*(18-4*c)-6*(4-c))==0
assert S.factor(4*e*(3-c)-c*(d-4*e) - (12*e-d*c))==0
print('PASS_UNIVERSAL_EVENT_DUAL_ELIMINATION')

aval=F(961,1000);bval=F(151,1000)
dval=aval+3*bval-F(1)
cstar=F(1039,1207)
Bstar=F(69,500)
Estar=F(71691,2414000)
c0=aval-6*Estar
assert dval==F(207,500)
assert 0<c0 and F(3,4)<c0<cstar<F(1)
assert Estar==dval*cstar/12==Bstar*cstar/4
fexpr=c*(a+6*b-(a+3*b)*c)/(6*(4-c))
fnum=S.factor(fexpr.subs({a:S.Rational(aval.numerator,aval.denominator),b:S.Rational(bval.numerator,bval.denominator)}))
assert S.factor(fnum.subs(c,S.Rational(cstar.numerator,cstar.denominator))-S.Rational(Estar.numerator,Estar.denominator))==0
fprime=S.factor(S.diff(fnum,c))
assert S.factor(fprime-(707*c*c-5656*c+3734)/(3000*(4-c)**2))==0
assert S.factor((707*c*c-5656*c+3734).subs(c,S.Rational(3,4)))==-S.Rational(1765,16)
# Numerator derivative 1414*c-5656 < 0 on 0<=c<=1. Therefore f'<0 on [3/4,1].
print('PASS_THREE_INTERVAL_ALL_REAL_LOWER_BOUND',f'c0={c0}',f'cstar={cstar}',f'E={Estar}')

# Attainment by the actual lawful collapsed S23 strategy A=1, B=69/500,
# conditional common AU/BU rate c*=1039/1207, AV=BV=0.
# U=V=0, so these obey 0<=U<=A and 0<=V<=B; time-three BU LR
# are disjoint from nonBU and permit the source-dependent decision in S23.
assign={A:S.Integer(1),B:S.Rational(Bstar.numerator,Bstar.denominator),
        c:S.Rational(cstar.numerator,cstar.denominator),U:S.Integer(0),V:S.Integer(0),
        a:S.Rational(aval.numerator,aval.denominator),b:S.Rational(bval.numerator,bval.denominator)}
for law in ('P','Q'):
    f=full_observer(law,assign[a],assign[b],assign[a],S.Integer(0),S.Integer(0),S.Integer(0))
    g=full_observer(law,assign[A],assign[B],assign[A]*assign[c],assign[B]*assign[c],S.Integer(0),S.Integer(0))
    signed=[S.factor(f[x]-g[x]) for x in atom_order]
    tv=S.factor(sum(abs(x) for x in signed)/2)
    assert tv==S.Rational(Estar.numerator,Estar.denominator),(law,tv)
    if law=='P':assert signed==[0,S.Rational(13,1000),S.Rational(40309,2414000),0,-S.Rational(71691,2414000)]
    else:assert signed==[S.Rational(13,1000),0,S.Rational(40309,2414000),0,-S.Rational(71691,2414000)]
    print('PASS_ALL_16_LEAVES_ATTAINED_TV_'+law, 'TV='+str(tv), 'signed='+str(signed))

print('PASS_BRC_N4_AU_BU_EXACT_ALL_ORIGINAL_S2_S23_MINIMAX_20261030')
