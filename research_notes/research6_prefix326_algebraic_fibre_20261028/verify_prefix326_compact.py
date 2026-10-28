"""PREFIX-326 exact fixed-Q0 auxiliary source-labelled BRC verifier.
Run: python verify_prefix326_compact.py (requires sympy).
Theorem scope is static S7-3; native X6/Detector/time bridge remains open.
"""
import sympy as s
I=s.I
x,y,u,v,w,t=s.symbols('x y u v w t',real=True)
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],
            [-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
a=[x+I*y,u+I*v,w]
Q=[128,80,74,200,85]
# Exactly 9 ordered source/source pairs in each of 5 Port reads.
f=[]
for j in range(5):
    paths=[s.expand(A[j,k]*a[k]) for k in range(3)]
    pairs=[s.expand(paths[k]*s.conjugate(paths[h]))
           for k in range(3) for h in range(3)]
    mass=s.expand(sum(pairs))
    assert len(pairs)==9 and s.simplify(s.im(mass))==0
    f.append(s.expand(s.re(mass)-Q[j]))
G=s.groebner(f,x,y,u,v,w,order='grevlex')
assert G.is_zero_dimensional
H=G.fglm('lex')
L=[p.as_expr() for p in H.polys]
assert len(L)==6
assert all(H.reduce(p)[1]==0 for p in f)
assert all(G.reduce(p)[1]==0 for p in L)
F=(5951717425889645*t**4-228788223822434608*t**3
   +4023748873308624459*t**2-20488030744357515722*t
   +31325392094413629826)
Qw=s.expand(F.subs(t,w*w))
assert s.Poly(L[-1],w).monic()==s.Poly((w*w-1)*Qw,w).monic()
# F has no rational root: irreducibility via the finite field F_13.
F13=s.Poly(F,t,modulus=13)
assert F13.degree()==4 and F13.is_irreducible
assert s.Poly(F,t).count_roots(-s.oo,0)==0
assert s.Poly(F,t).count_roots(0,s.oo)==2
assert s.Poly(F,t).count_roots(s.Rational(333,100),s.Rational(335,100))==1
assert s.Poly(F,t).count_roots(s.Rational(352,100),s.Rational(353,100))==1
# At the two positive algebraic roots t!=1 the lex basis gives a
# unique x,y,u,v. Verify ALL original BRC relations in Q[w]/F(w^2).
P=s.Poly(Qw,w,domain=s.QQ)
def mod(z): return s.Poly(s.cancel(z),w,domain=s.QQ).rem(P).as_expr()
X,Y,U=(mod(s.solve(L[i],variable)[0])
       for i,variable in enumerate((x,y,u)))
V=s.solve(L[4],v)[0]
num,den=s.cancel(V).as_numer_denom()
V=mod(num*s.invert(den,Qw,w))
for eq in f:
    assert s.Poly(eq.subs({x:X,y:Y,u:U,v:V},simultaneous=True),w,
                  domain=s.QQ).rem(P).is_zero
# At t=w^2=1, w>=0 fixes w=1, and only b_-/b_+ remain.
assert [s.solve(L[i].subs(w,1),variable)[0]
        for i,variable in enumerate((x,y,u))]==[-2,0,0]
assert s.Poly(L[3].subs({w:1,x:-2,y:0,u:0}),v).monic().as_expr()==v*v-4
for sign in (-1,1):
    assert all(eq.subs({x:-2,y:0,u:0,v:2*sign,w:1})==0 for eq in f)
print('PASS: 45 ordered BRC pairs; 5 exact masses; 6 lex equations;')
print('F irreducible mod 13; two extra real algebraic orbits;')
print('FOUR complex phase orbits, exactly TWO Q(i)-phase orbits.')
