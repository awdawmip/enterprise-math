"""Exact cell and endpoint certification for all possible rival distance ties."""
from denom_scan import A,B,D,E,H,S,groups,pol
import sympy as sp
from itertools import product

def pne(x): return sp.Poly(x,D,domain=sp.QQ)
AA=pne(A.subs(E,0));BB=pne(B.subs(E,0));HH=pne(H)
def sign_at(f, root, l, u):
    if f.is_zero: return 0
    if l==u: return sp.sign(f.eval(l))
    if f.rem(root).is_zero:return 0
    # The irreducible root is unique in this interval. Refine until all
    # other real zeros of f are outside it and its sign is determined.
    while f.count_roots(l,u):
        l,u=root.refine_root(l,u,steps=8)
    return sp.sign(f.eval((l+u)/2))
def signs_data(sgn):
    bad=[]
    for a,b in product(range(6),repeat=2):
        if a==b:continue
        extremes=[]
        f=lambda i,k: AA*S[a][i]+BB-HH*S[k][i]
        for k in (a,b):
            candidate=0*HH
            for i in range(3):
                v=f(i,k)
                if sgn(v)<0:v=-v
                if sgn(v-candidate)>0:candidate=v
            extremes.append(candidate)
        if sgn(extremes[1]-extremes[0])<=0:bad.append((a,b))
    return set(bad)
zero=sp.Rational(0)
assert signs_data(lambda p:sp.sign(p.eval(zero)))==set()
for side in (-1,1):
    prev=sp.Rational(0)
    series=sorted([g for g in groups if side*(g[0]+g[1])>0],key=lambda g:side*(g[0]+g[1]))
    first=None
    for l,u,ps in series:
        # Equality status inside the entire cell is constant since every
        # nonidentical equality |true coord|=|rival coord| root was enumerated.
        midpoint=(prev+(l if side==1 else u))/2
        assert signs_data(lambda p:sp.sign(p.eval(midpoint)))==set()
        root=next(x for x,n in ps[0].factor_list()[1] if (l==u and x.eval(l)==0) or (l<u and x.count_roots(l,u)))
        endpoints=signs_data(lambda p:sign_at(p,root,l,u))
        if endpoints:
            first=(l,u,root,endpoints)
            print('side',side,'isolating bounds',l,u,'minimal factor',root.as_expr(),'first pairs',sorted(endpoints))
            break
        prev=u if side==1 else l
    assert first
    if side==-1:
        assert first[3]=={(1,0),(5,0)}
        assert sp.factor(first[2].as_expr()-(6*D**5-96*D**4+441*D**3-41*D**2+56*D+15))==0
    else:
        assert first[2].as_expr()==D**2+2*D-1
