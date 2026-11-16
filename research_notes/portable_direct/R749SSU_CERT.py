#!/usr/bin/env python3
"""Exact R749SSU effective inversion certificate (Python 3 + SymPy)."""
import json
from pathlib import Path
import sympy as s
x,e,d=s.symbols('x e d')
W=(1,1,2,3,6); M=100
ways=[0]*(M+1);ways[0]=1
for w in W:
    for i in range(w,M+1):ways[i]+=ways[i-w]
C=[0]*(M+1);T=[0]*(M+1)
for i in range(1,M+1):
    C[i]=C[i-1]+ways[i-1]
    T[i]=T[i-1]+C[i-1]
assert C[6]==41
S=18*x**4+54*x**3-345*x**2+2070*x-16315
L=[s.Rational(455,36),-s.Rational(295,36),-s.Rational(25,36),s.Rational(185,36),-s.Rational(25,36),-s.Rational(295,36)]
Kph=[];forced=[]
for r in range(6):
    qs=[r+6*k for k in range(1,9)]
    c=s.Poly(s.interpolate([(n,C[n]) for n in qs[:6]],x),x)
    t=s.Poly(s.interpolate([(n,T[n]) for n in qs[:7]],x),x)
    assert (c.degree(),t.degree())==(5,6)
    assert all(c.eval(n)==C[n] and t.eval(n)==T[n] for n in qs)
    den=c.as_expr()+d
    num=s.Poly(s.expand(x**3*(t.as_expr()+e)-S*den/108),x)
    assert num.degree()==5 and num.LC()/c.LC()==L[r]
    v=s.Poly(s.expand(num.as_expr()-L[r]*den),x)
    assert v.degree()<=4
    a=s.Poly(v.as_expr().subs({e:0,d:0}),x)
    b=s.Poly(s.diff(v.as_expr(),e),x)
    f=s.Poly(s.diff(v.as_expr(),d),x)
    assert s.expand(v.as_expr()-a.as_expr()-e*b.as_expr()-d*f.as_expr())==0
    B=sum((abs(a.nth(k))+2*abs(b.nth(k))+2*abs(f.nth(k)))/s.Integer(6)**(4-k) for k in range(5))
    Kph.append(s.factor(B*s.Rational(4320*41,39)))
    solutions=s.solve([v.nth(4),v.nth(3)],[e,d],dict=True)
    assert len(solutions)==1 and solutions[0][e]<-2
    forced.append(str(solutions[0][e]))
assert max(Kph)==s.Rational(41724295135,2047032)
K=20383
assert all(k<K for k in Kph)
def observation(n,ee,dd):
    return s.cancel(n**3*(s.Integer(T[n])+ee)/(s.Integer(C[n])+dd)-S.subs(x,n)/108)
def inverse(n,y0,y1):
    X0=(y0+S.subs(x,n)/108)/n**3
    X1=(y1+S.subs(x,n+6)/108)/(n+6)**3
    assert X0!=X1
    dd=s.cancel((T[n+6]-T[n]-X1*C[n+6]+X0*C[n])/(X1-X0))
    ee=s.cancel(X0*(C[n]+dd)-T[n])
    return ee,dd
samples=[]
for n,ee,dd in [(6,s.Rational(1,3),s.Rational(-1,2)),(7,s.Integer(2),s.Integer(-2)),(12,s.Integer(0),s.Integer(1))]:
    y=[observation(n+6*j,ee,dd) for j in range(11)]
    delta=max(y)-min(y)
    assert delta>0 and n<=s.floor(2*K/delta)
    assert inverse(n,y[0],y[1])==(ee,dd)
    samples.append({'q':n,'e':str(ee),'d':str(dd),'delta':str(delta),'bound':str(s.floor(2*K/delta))})
data={'unit':'R749SSU','status':'PASS','class':'AUTHOR_EXACT_NOT_REVIEWED','scientific_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389','K':K,'phase_bounds':[str(k) for k in Kph],'max_exact_bound':str(max(Kph)),'constant_identity_forced_e':forced,'theorem':'Delta>0 and q<=floor(40766/Delta) for every admissible 11-read vector','samples':samples,'proof_dependencies':'R749SST global 11-read uniqueness and all-phase quasi-polynomial identities; R749SSJ known-q two-read calibration'}
Path(__file__).with_name('R749SSU_RESULTS.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print('PASS', 'K=',K, 'max=',max(Kph), 'samples=',samples)
