#!/usr/bin/env python3
"""Exact k=9/25 addendum; reuses already tested full BRC N4 BU 16-leaf harness."""
from pathlib import Path
import runpy
from fractions import Fraction as F
import sympy as S

prior=Path(__file__).resolve().parents[1]/'brc_n4_bu_capacity_variable_splice_20261029_r1t11'/'VERIFY.py'
if not prior.is_file():
    # In the published Enterprise Math repo, use the original committed verifier.
    prior=Path(__file__).resolve().parents[1]/'brc_n4_bu_k2over5_curved_capacity_20261029_r1t11'/'VERIFY.py'
p=runpy.run_path(str(prior))
a,b=p['a'],p['b']; G=p['G']; C=p['C']; E=p['E']; L0=p['L0']; L3=p['L3']
a0=S.Rational(9607,10000); bmax=S.Rational(73,500); k=S.Rational(9,25)
N=55781*a*a+243936*a*b-90472*a+229779*b*b-692766*b+97475
f1=61*a+633*b-157; f2=121*a+363*b-175
checks=[]
def eq(label,x,y=0):
    z=S.factor(S.cancel(x-y));assert z==0,(label,z);checks.append(label)
eq('new-L0-splice',L0(k)-E,N/(334200*(2*a+6*b+1)))
eq('new-L3-splice',L3(k)-E,f1*f2/(94200*(2*a+6*b+1)))
eq('G-b-maximum',G.subs({a:a0,b:(8*a0-2)/42}),-S.Rational(310557,700000000))
eq('N-corner',N.subs({a:a0,b:bmax}),S.Rational(1044937989,100000000))
eq('N_b-upper',S.diff(N,b).subs({a:1,b:bmax}),-S.Rational(95433633,250))
eq('N_a-lower',S.diff(N,a).subs({a:a0,b:bmax}),S.Rational(261601347,5000))
eq('factor-1-upper',f1.subs({a:1,b:bmax}),-S.Rational(1791,500))
eq('factor-2-upper',f2.subs({a:1,b:bmax}),-S.Rational(501,500))
eq('C-min',C.subs({a:1,b:bmax}),S.Rational(489,1292))
eq('C-min-minus-k',S.Rational(489,1292)-k,S.Rational(597,32300))

for aa,bb in [(F(961,1000),F(73,500)),(F(1),F(73,500)),(F(97,100),F(29,200))]:
    assert F(0)<bb<=F(73,500)
    assert 5*aa*aa+8*aa*bb-21*bb*bb-2*bb-5>=0
    d=(1-aa)/3; bs=bb-d; cc=(7-aa-21*bb)/(4*aa+12*bb+2); ee=bs*cc/4; uu=bs*(1+cc)
    assert F(0)<bs<=bb and F(9,25)<cc<F(1) and F(0)<uu<=F(1) and ee>=d
    for law in 'PQ':
        comp=p['observe'](law,aa,bb,F(1),bs,cc,uu,bs,False)
        target=p['observe'](law,aa,bb,F(1),bs,cc,uu,bs,True)
        assert p['tv'](comp,target)==ee
    print('NEW_16LEAF_WITNESS',str(aa),str(bb),'C',str(cc),'P_TV=Q_TV',str(ee))
assert G.subs({a:S.Rational(961,1000),b:S.Rational(73,500)})==S.Rational(417,1000000)
print('PASS_NEW_K9P25_EXACT_IDENTITIES',len(checks))
print('PASS_NEW_K9P25_THREE_16LEAF_TWO_LAW_WITNESSES')
print('PASS_BRC_N4_BU_CURVED_CAPACITY_UP_TO_73_OVER_500_20261029')
