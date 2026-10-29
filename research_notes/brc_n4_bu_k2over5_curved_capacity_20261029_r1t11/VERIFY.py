#!/usr/bin/env python3
"""Exact author-side BRC N4 BU variable-splice certificate checker.

The universal argument is in PROOF.md.  This script verifies algebra,
endpoint signs and six rational 16-positive-leaf P/Q witnesses, not a
machine-formal proof or an independent research review.
"""
from collections import defaultdict
from fractions import Fraction as F
import sympy as S

a, b, u, A, B, U, V = S.symbols('a b u A B U V', real=True)
k = S.Rational(2, 5)
amin = S.Rational(9607, 10000)
bmax = S.Rational(27, 200)
delta = (1-a)/3
G = 5*a*a+8*a*b-21*b*b-2*b-5
alpha = (S.sqrt(121*b*b+10*b+25)-4*b)/5
C = (7-a-21*b)/(4*a+12*b+2)
Bstar = b-delta
E = S.factor(Bstar*C/4)
L0 = lambda x:(4*a-14*b-3*a*x-(a+3*b)*x*x)/(2*(23-2*x))
L3 = lambda x:x*(a-(a+3*b)*x)/(2*(7-2*x))
N0 = 713*a*a+3128*a*b-1216*a+2967*b*b-9218*b+1295
f1, f2 = 13*a+129*b-31, 23*a+69*b-35
checks = []
def eq(label, actual, want=0):
    residue = S.factor(S.cancel(actual-want))
    assert residue == 0, (label, residue)
    checks.append(label)
def less(label, actual, target):
    assert actual < target,(label,actual,target)
    checks.append(label)
def more(label, actual, target):
    assert actual > target,(label,actual,target)
    checks.append(label)

eq('G-alpha', G.subs(a,alpha))
eq('G-above-capacity-line', G.subs(a,1-3*b/5),-24*b*b)
eq('E-minus-delta', E-delta, G/(8*(2*a+6*b+1)))
eq('L3(C)', L3(C), E)
eq('C-min', C.subs({a:1,b:bmax}), S.Rational(211,508))
eq('k-Cmin', S.Rational(211,508)-k, S.Rational(39,2540))
eq('L0-k', L0(k)-E, N0/(4440*(2*a+6*b+1)))
eq('L3-k', L3(k)-E, f1*f2/(3720*(2*a+6*b+1)))
eq('G-amin-bmax', G.subs({a:amin,b:bmax}),-S.Rational(8931,20000000))
eq('Gb-at-max', S.diff(G,b).subs({a:amin,b:bmax}),S.Rational(39,2500))
eq('N0-corner',N0.subs({a:amin,b:bmax}),S.Rational(17619237,100000000))
eq('N0b-max',S.diff(N0,b).subs({a:1,b:bmax}),-S.Rational(528891,100))
eq('N0a-min',S.diff(N0,a).subs({a:amin,b:bmax}),S.Rational(2881191,5000))
eq('f1-max',f1.subs({a:1,b:bmax}),-S.Rational(117,200))
eq('f2-max',f2.subs({a:1,b:bmax}),-S.Rational(537,200))
# The L0 derivative numerator is strictly negative for a,b > 0 and 0 <= u <= 2/5.
der0=S.factor(S.diff(L0(u),u))
eq('L0-derivative',der0, (a*(2*u*u-46*u-61)+b*(6*u*u-138*u-28))/(2*(23-2*u)**2))
# The derivative of L3 has strictly decreasing numerator on [0,1], so L3 has no interior minimum.
der3=S.factor(S.diff(L3(u),u))
eq('L3-derivative',der3,(7*a-14*(a+3*b)*u+2*(a+3*b)*u*u)/(2*(7-2*u)**2))
# C is decreasing in both a and b on this rectangle.
eq('C-derivative-a',S.diff(C,a),-(30-72*b)/(4*a+12*b+2)**2)
eq('C-derivative-b',S.diff(C,b),-(72*a+126)/(4*a+12*b+2)**2)
# Event differences, exact attainment for both positive mass laws.
s = (A-a+B-b)/2
t = (A-a+3*(B-b))/4
H = B*u/4
rQ = a/6-A*u/6-U/3-V/4
rP = a/6-A*u/6-U/12-V/2
DQ = (s,H-s-rQ,rQ,-H)
DP = (t,H-t-rP,rP,-H)
eq('P-middle-two-event',DP[1]+DP[2],H-t)
eq('P-first-three-event',sum(DP[:3]),H)
selection = {A:1,B:Bstar,u:C,U:Bstar*(1+C),V:Bstar}
for law,atoms,want in [('Q',DQ,(delta,E-delta,0,-E)),('P',DP,(0,0,E,-E))]:
    for idx in range(4): eq(f'attainment-{law}-{idx}',atoms[idx].subs(selection,simultaneous=True),want[idx])

base = {'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
ratio = {'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
         'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
leaves = [(branch,base[branch]/4,base[branch]*ratio[branch][i]/4)
          for branch in base for i in (0,1) for z in (0,1)]
assert len(leaves)==16 and all(q>0 and p>0 for _,q,p in leaves)
assert sum(q for _,q,_ in leaves)==sum(p for _,_,p in leaves)==1

def observe(law,aa,bb,AA,BB,cc,UU,VV,target):
    out=defaultdict(F)
    for branch, qmass, pmass in leaves:
        mass=qmass if law=='Q' else pmass
        one=(aa if branch[0]=='A' else bb) if target else (AA if branch[0]=='A' else BB)
        two=(F(1) if branch=='AU' else F(0)) if target else {'AU':cc,'BU':cc,'AV':UU/AA,'BV':VV/BB}[branch]
        assert 0<=one<=1 and 0<=two<=1
        out[(1,'Q',0)] += mass*(1-one)
        out[(2,'Q',0)] += mass*one*(1-two)
        out[(3,'Q' if (branch=='BU' and not target) else 'P',int(branch=='BU'))] += mass*one*two
    assert sum(out.values())==1
    return out

def tv(p,q):
    return sum(abs(p.get(key,F(0))-q.get(key,F(0))) for key in p.keys()|q.keys())/2

points = [(F(999,1000),F(1,100)),(F(99,100),F(1,20)),
          (F(97,100),F(1,10)),(F(961,1000),F(129,1000)),
          (F(961,1000),F(27,200)),(F(1),F(27,200))]
for aa,bb in points:
    assert 0<bb<=F(27,200)
    assert 5*aa*aa+8*aa*bb-21*bb*bb-2*bb-5>=0
    d=(1-aa)/3; bs=bb-d
    cc=(7-aa-21*bb)/(4*aa+12*bb+2)
    ee=bs*cc/4
    uu=bs*(1+cc)
    assert F(0)<bs<=bb and F(2,5)<=cc<F(1) and F(0)<uu<=1 and ee>=d
    for law in 'PQ':
        target=observe(law,aa,bb,F(1),bs,cc,uu,bs,True)
        competitor=observe(law,aa,bb,F(1),bs,cc,uu,bs,False)
        assert tv(target,competitor)==ee,(law,aa,bb,tv(target,competitor),ee)
    print('RATIONAL_16LEAF_WITNESS',str(aa),str(bb),'C',str(cc),'P_TV=Q_TV',str(ee))

# Witness strictly after old b_sharp and above the capacity boundary a=alpha(b).
aa,bb=F(961,1000),F(129,1000)
assert 5*aa*aa+8*aa*bb-21*bb*bb-2*bb-5==F(237,125000)
assert (7-aa-21*bb)/(4*aa+12*bb+2)==F(555,1232)
assert (bb-(1-aa)/3)*F(555,1232)/4==F(3219,246400)
q=lambda x:24045*x*x-26924*x+3040
assert q(F(127,1000))>0 and q(F(128,1000))<0
print('FORMAL_SCOPE author-side exact symbolic checks=',len(checks))
print('CHECKED 6 full-16-leaf rational witness pairs under both laws')
print('PASS_EXACT_BRC_N4_BU_K2P5_CURVED_CAPACITY_EXTENSION_20261029')
