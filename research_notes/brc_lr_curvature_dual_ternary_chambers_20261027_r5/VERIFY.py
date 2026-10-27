"""Exact rational certificates for BRC affine-curvature dual and signed hinge chambers.
External finite two-measure trees only; no native X6 physical inference.
"""
from fractions import Fraction as F
from itertools import combinations, product

def tv(a,b):
    return sum((abs(x-y) for x,y in zip(a,b)), F(0))/2

def triple_witness(y, f):
    if len(y)<3: return F(0), None
    data=[]
    for i,j,k in combinations(range(len(y)),3):
        score=f[j] - ((y[k]-y[j])*f[i]+(y[j]-y[i])*f[k])/(y[k]-y[i])
        data.append((abs(score),(i,j,k),score))
    s,idx,val=max(data,key=lambda t:t[0])
    return s,(idx,val)

def affine_primal(y,f):
    """Minimum residual oscillation via exact pair-line crossing candidates."""
    if len(y)<=1: return F(0),F(0)
    all_b=[(f[j]-f[i])/(y[j]-y[i]) for i,j in combinations(range(len(y)),2)]
    r=[]
    for b in all_b:
        residual=[fi-b*yi for fi,yi in zip(f,y)]
        r.append((max(residual)-min(residual),b))
    return min(r,key=lambda t:t[0])

def hinge(a,b,y): return [min(a*v,b) for v in y]

def tent(a,b):
    low=min(a/2,F(3)*a/2)
    high=max(a/2,F(3)*a/2)
    return max(F(0), min(b-low,high-b)/2)

y3=[F(1,2),F(1),F(3,2)]
ka3=[F(1,4),F(1,2),F(1,4)]
kb3=[F(1,8),F(3,4),F(1,8)]
assert tv(ka3,kb3)==F(1,4)
assert all(sum(k)==1 and sum(a*b for a,b in zip(k,y3))==1 for k in (ka3,kb3))
for a,b,u,v in product((F(-5,4),F(-1),F(-3,4),F(0),F(1,4),F(1),F(5,4)),repeat=4):
    f=[min(a*yi,b)+F(3)*(u*yi+v) for yi in y3]
    rho, dual=triple_witness(y3,f)
    po, beta=affine_primal(y3,f)
    assert rho==po==tent(a,b)
    assert sum((p-q)*z for p,q,z in zip(ka3,kb3,f))==-rho/F(4)
print('3point signed four-coefficient exhaustive grid: 7^4=2401 PASS')

r=F(3,4)
a_top=[F(1,2),F(1,2),F(0)]
a_bottom=[F(3,4),F(0),F(1,4)]
base=[F(3,5),F(3,10),F(1,10)]
assert all(sum(k)==1 and sum(a*b for a,b in zip(k,y3))==r for k in (a_top,a_bottom,base))
assert tv(a_top,a_bottom)==F(1,2)
f_fixed=hinge(F(1),F(1),y3)
assert triple_witness(y3,f_fixed)[0]==F(1,4)
assert abs(sum((p-q)*f for p,q,f in zip(a_top,a_bottom,f_fixed)))==F(1,8)
for eps in (F(1,8),F(1,3)):
    K=[(1-eps)*a+eps*b for a,b in zip(a_top,base)]
    L=[(1-eps)*a+eps*b for a,b in zip(a_bottom,base)]
    assert min(K+L)>0
    assert tv(K,L)==(1-eps)/2
    assert abs(sum((p-q)*f for p,q,f in zip(K,L,f_fixed)))==tv(K,L)/4
print('3point fixed mean r=3/4: sharp TV radius gamma=1/2, sharp value width=1/8 PASS')

y4=[F(1,2),F(3,4),F(5,4),F(3,2)]
f4=hinge(F(1),F(1),y4)
rho4, triple=triple_witness(y4,f4)
primal4,slope4=affine_primal(y4,f4)
assert (rho4,primal4)==(F(1,8),F(1,8))
assert slope4==F(1,2)
res=[fi-slope4*yi for fi,yi in zip(f4,y4)]
assert res==[F(1,4),F(3,8),F(3,8),F(1,4)]
inner=[F(0),F(1,2),F(1,2),F(0)]
outer=[F(1,2),F(0),F(0),F(1,2)]
uniform=[F(1,4)]*4
for eps in [F(1,2),F(1,8),F(1,64),F(3,4)]:
    kp=[(1-eps)*x+eps*u for x,u in zip(inner,uniform)]
    km=[(1-eps)*x+eps*u for x,u in zip(outer,uniform)]
    assert all(z>0 for z in kp+km)
    for kk in (kp,km):
        assert sum(kk)==1 and sum(z*yr for z,yr in zip(kk,y4))==1
    difference=sum((a-b)*ff for a,b,ff in zip(kp,km,f4))
    assert tv(kp,km)==1-eps
    assert difference==(1-eps)/8 == tv(kp,km)*rho4
    if eps==F(1,8):
        assert kp==[F(1,32),F(15,32),F(15,32),F(1,32)]
        assert km==[F(15,32),F(1,32),F(1,32),F(15,32)]
        assert difference==F(7,64) and tv(kp,km)==F(7,8)
        Q=[F(1,2)*x for x in kp+km]
        P=[F(1,2)*yr*x for kernel in (kp,km) for yr,x in zip(y4,kernel)]
        assert len(Q)==len(P)==8 and min(P+Q)>0
        assert sum(P)==sum(Q)==1
        assert [pp/qq for pp,qq in zip(P,Q)]==y4+y4
        assert sum(k*f for k,f in zip(kp,f4))==F(111,128)
        assert sum(k*f for k,f in zip(km,f4))==F(97,128)
print('4point primal slope=',slope4,'dual triple=',triple[0], 'rho=',rho4)
print('8leaf strictly positive Q/P tree: TV=7/8, Bayes-continuation-value gap=7/64, equality PASS')

checks=0
for y in (y3,y4,[F(-2),F(-1),F(0),F(1),F(3)]):
    for fs in product((-1,0,1,2),repeat=len(y)):
        ff=[F(z) for z in fs]
        d,_=triple_witness(y,ff)
        p,_=affine_primal(y,ff)
        assert d==p,(y,ff,d,p)
        checks+=1
print('Independent rational finite primal/dual comparisons=',checks,'PASS')
print('ALL EXACT CHECKS PASSED')
