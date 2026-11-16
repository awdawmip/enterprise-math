#!/usr/bin/env python3
"""Exact, self-contained R749SSS certificate (Python 3, SymPy)."""
import sympy as s
q,e,d,E,D,z=s.symbols('q e d E D z')
a=[0]*91;a[0]=1
for w in (1,1,2,3,6):
    for k in range(w,91):a[k]+=a[k-w]
C=[0]*91;T=[0]*91
for k in range(1,91):C[k]=C[k-1]+a[k-1];T[k]=T[k-1]+C[k-1]
for k in range(1,25):
    c=t=0
    for f in range((k-1)//6+1):
        for g in range((k-1-6*f)//3+1):
            for h in range((k-1-6*f-3*g)//2+1):
                u=k-1-6*f-3*g-2*h
                c+=(u+1)*(u+2)//2;t+=u*(u+1)*(u+2)//6
    assert(c,t)==(C[k],T[k])
S=lambda x:18*x**4+54*x**3-345*x**2+2070*x-16315
P={}
for r in (2,4):
    x=[r+6*k for k in range(1,8)]
    cp=s.Poly(s.interpolate([(v,C[v]) for v in x[:6]],q),q)
    tp=s.Poly(s.interpolate([(v,T[v]) for v in x],q),q)
    assert cp.degree()==5 and tp.degree()==6
    assert all(cp.eval(v)==C[v] and tp.eval(v)==T[v] for v in x)
    P[r]=(cp,tp)
# Exact extension to all residue integers follows from the generating functions
# z/((1-z)^3(1-z^2)(1-z^3)(1-z^6)) and
# z^2/((1-z)^4(1-z^2)(1-z^3)(1-z^6)).
v=sum(z**k for k in range(6))
assert s.degree(z*v**3*(1+z**2+z**4)*(1+z**3),z)==23
assert s.degree(z**2*v**4*(1+z**2+z**4)*(1+z**3),z)==29
def jet(r):
    cp,tp=P[r];den=s.Poly(cp.as_expr()+d,q)
    num=s.Poly(s.expand(q**3*(tp.as_expr()+e)-S(q)*den.as_expr()/108),q)
    assert num.degree()==den.degree()==5
    aa=[num.nth(5-i)/den.nth(5) for i in range(6)]
    bb=[den.nth(5-i)/den.nth(5) for i in range(6)]
    out=[]
    for k in range(6):
        out.append(s.factor(aa[k]-sum(bb[j]*out[k-j] for j in range(1,min(k,5)+1))))
    return out
v2,v4=jet(2),jet(4)
def shifted(k):
    if k==0:return v4[0]
    return sum(v4[j]*s.binomial(k-1,k-j)*(-2)**(k-j) for j in range(1,k+1))
delta=[s.factor(v2[k]-shifted(k).subs({e:E,d:D})) for k in range(6)]
assert delta[0]==0
sol=s.solve(delta[1:5],[d,e,D,E],dict=True)
assert len(sol)==1
sol=sol[0]
assert sol=={d:-s.Rational(656227,472068),e:s.Rational(69402481,101966688),
            D:-s.Rational(755303,472068),E:s.Rational(194725627,101966688)}
assert all(-2<sol[t]<2 for t in (e,d,E,D))
assert all(s.factor(delta[k].subs(sol))==0 for k in range(5))
fifth=s.factor(delta[5].subs(sol))
assert fifth==s.Rational(55842420440,39339)
def read(r,x,ee,dd):
    cp,tp=P[r]
    return x**3*(tp.as_expr().subs(q,x)+ee)/(cp.as_expr().subs(q,x)+dd)-S(x)/108
F=s.factor(read(2,q,sol[e],sol[d])-read(4,q+2,sol[E],sol[D]))
num,den=(s.Poly(p,q) for p in s.fraction(s.together(F)))
assert (num.degree(),den.degree())==(5,10)
coefs=s.Poly(s.expand(num.as_expr().subs(q,z+8)/40),z).all_coeffs()
assert coefs==[6102180493581,378167765492115,9429198074047290,
  115759280836964670,687635127000756764,1568096750641526440]
assert all(t>0 for t in coefs)
assert s.factor(num.LC()/den.LC())==fifth
assert C[8]==98 and C[10]==203
for k in (8,14,20,32,62,122,602):assert F.subs(q,k)>0
print('PASS: unique fifth-order jet alias, admissible exact errors, all q=6n+2>=8 positive')
print('errors', {str(k):str(v) for k,v in sol.items()})
print('leading constant',fifth)
