#!/usr/bin/env python3
"""Exact symbolic weights; no prime is instantiated."""
import json
import sympy as S
from pathlib import Path

x, s, a = S.symbols('x s a')
Aw, At, Ae, Bw, Bt, Be = S.symbols('Aw At Ae Bw Bt Be')
Cw, Ct, Ce, Dw, Dt, De, Fw, Ft, Fe = S.symbols('Cw Ct Ce Dw Dt De Fw Ft Fe')
zs = (1+s)/(1-s)
aa = 4*(x+1)**2-(3*x-1)*(x-1)**2
bb = 3*(3*x-1)*(x-1)**2
dd = (x*x-1)**3
alpha = -(3*x-1)*aa/(9*dd)
beta = -(3*x-1)*(aa+3*bb)/(9*dd)
chi = -(aa+3*bb)/(9*dd)
rows = {}
for name, f in [('alpha', alpha), ('beta', beta), ('chi', chi)]:
    rows[name+'_mobius'] = str(S.factor(f.subs(x,zs)))

# NF(1)=A*, NF(-1)=B*, NF(CM)=C*, NF(1/2)=D*, NF(-1/2)=F*.
plus = [-(u+v)/2 for u,v in [(Aw,Bw),(At,Bt),(Ae,Be)]]
minus = [(u-v)/2 for u,v in [(Aw,Bw),(At,Bt),(Ae,Be)]]
rp = -32*(plus[0]+plus[1])/9-16*plus[2]/9
rm = 64*minus[0]/9-512*minus[1]/9+128*minus[2]/9
n0 = -(rp+rm)/2
n1 = -(rp-rm)/2

def value(z, ss, vals):
    xx = (1+ss)/(1-ss) if z is None else z
    if vals is None:
        iw = it = ie = 0
    else:
        iw,it,ie = [(f-u)/(1-ss)-(v-u)/2 for f,u,v in zip(vals,[Aw,At,Ae],[Bw,Bt,Be])]
    return (alpha*iw+beta*it+chi*ie+(n0+n1*x)/dd).subs(x,xx)

zcm = (1+a)/(1-a)
lamb = 12*value(None,-a,[Cw,Ct,Ce])-zcm*value(0,None,None)
lamb -= (3-zcm)*value(3,S.Rational(1,2),[Dw,Dt,De])
lamb -= (zcm-S.Rational(1,3))*value(S.Rational(1,3),-S.Rational(1,2),[Fw,Ft,Fe])

def red(expr):
    num,den = S.fraction(S.cancel(expr))
    q = a*a-S.Rational(1,2)
    num = S.rem(num,q,a)
    den = S.rem(den,q,a)
    inv = S.invert(den,q,a)
    return S.factor(S.rem(S.expand(num*inv),q,a))

for var in [Aw,At,Ae,Bw,Bt,Be,Cw,Ct,Ce,Dw,Dt,De,Fw,Ft,Fe]:
    rows['Lambda_weight_'+str(var)] = str(red(S.diff(lamb,var)))
rows['Lambda_constant'] = str(red(lamb.subs({v:0 for v in [Aw,At,Ae,Bw,Bt,Be,Cw,Ct,Ce,Dw,Dt,De,Fw,Ft,Fe]})))
out = Path(__file__).with_name('TRANSFORMED_OBSERVER_WEIGHTS.json')
out.write_text(json.dumps(rows, indent=2)+'\n')
print(json.dumps(rows,indent=2))
