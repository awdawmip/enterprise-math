#!/usr/bin/env python3
"""R749SSV exact SymPy positivity certificate; five labeled sources, frozen a72226e2."""
import sympy as s
x,e,d,z=s.symbols('x e d z')
ways=[1]+[0]*100
for w in (1,1,2,3,6):
    for n in range(w,101): ways[n]+=ways[n-w]
C=[0]*101; T=[0]*101
for n in range(1,101):
    C[n]=C[n-1]+ways[n-1]; T[n]=T[n-1]+C[n-1]
S=18*x**4+54*x**3-345*x**2+2070*x-16315
L=[s.Rational(i,36) for i in (455,-295,-25,185,-25,-295)]
K=[s.Rational(a,b) for a,b in ((7655,3),(26740,9),(25805,9),(8060,3),(24445,9),(25940,9))]

def pos(p,origin):
    co=s.Poly(s.expand(p).subs(x,x+origin),x).all_coeffs()
    assert co and all(v>0 for v in co), (origin,co)
    return min(co)

env=[]; step=[]
for r in range(6):
    origin=6+r; ns=[r+6*k for k in range(1,9)]
    c=s.interpolate([(n,C[n]) for n in ns[:6]],x)
    t=s.interpolate([(n,T[n]) for n in ns[:7]],x)
    assert all(c.subs(x,n)==C[n] and t.subs(x,n)==T[n] for n in ns)
    V=s.expand(x**3*(t+e)-(S/108+L[r])*(c+d))
    assert s.degree(V,x)<=4
    assert pos(c-2,origin)>0
    a=s.limit(x*V.subs({e:0,d:-2})/(c-2),x,s.oo)
    b=s.limit(x*V.subs({e:0,d:2})/(c+2),x,s.oo)
    assert a==K[r] and abs(b)<=a
    for ee in (-2,2):
        for dd in (-2,2):
            for sign in (-1,1):
                env.append(pos(K[r]*(c+dd)+sign*x*V.subs({e:ee,d:dd}),origin))
        for sign in (-1,1):
            dd=4*z-2
            D0=c+dd; D1=c.subs(x,x+6)+dd
            V0=V.subs({e:ee,d:dd}); V1=V.subs(x,x+6).subs({e:ee,d:dd})
            P=s.Poly(s.expand(6*K[r]*D0*D1+sign*x*x*(V1*D0-V0*D1)),z)
            assert P.degree()<=2
            A,B,G=P.nth(2),P.nth(1),P.nth(0)
            for bern in (G,G+B/2,G+B+A): step.append(pos(bern,origin))
assert len(env)==48 and len(step)==72
assert max(K)==s.Rational(26740,9)
assert min(env)==s.Rational(667,1296) and min(step)==s.Rational(1,2160)
print('PASS', 'phase_K=',list(map(str,K)),'global_K=',max(K),
      '11_read_numerator=',60*max(K),'envelope=',len(env),
      'Bernstein=',len(step),'min_coefficients=',min(env),min(step))
