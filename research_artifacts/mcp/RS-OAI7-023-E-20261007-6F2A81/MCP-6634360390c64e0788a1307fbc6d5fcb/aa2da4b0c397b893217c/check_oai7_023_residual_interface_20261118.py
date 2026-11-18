from fractions import Fraction as Q

def add(z,t): return (z[0]+t[0], z[1]+t[1])
def mul(c,z): return (c*z[0], c*z[1])
def weighted(w, v):
    out=(Q(0),Q(0))
    for coeff,z in zip(w,v): out=add(out,mul(Q(coeff),z))
    return out

a=(Q(3,5),Q(4,5))
abar=(Q(3,5),Q(-4,5))
v=(a,abar); vp=(abar,a)
assert add(*v)==add(*vp)==(Q(6,5),Q(0))
assert all(z[0]*z[0]+z[1]*z[1]==1 for z in v+vp)
assert weighted((1,2),v)==(Q(9,5),Q(-4,5))
assert weighted((1,2),vp)==(Q(9,5),Q(4,5))
assert weighted((1,2),v)!=weighted((1,2),vp)
e=(a,(-a[0],-a[1]))
assert weighted((1,1),e)==(Q(0),Q(0))
assert weighted((1,2),e)!=(Q(0),Q(0))
print("PASS labelled Gaussian rational positive-weight witness")