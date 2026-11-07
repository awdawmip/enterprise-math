"""Exact author-side checks for R5 ratio-balanced pure-time hull classification.
All arithmetic is rational. No random tests, no numerical solver.
"""
from fractions import Fraction as F
from itertools import product

C = F(2, 3)
ALPHA = (F(1,2), F(2,3), F(1,2), F(3,4))
WEIGHT = (F(1,8), F(1,6), F(1,16), F(3,32))
SUBSETS = ((), (0,), (0,1), (0,2), (0,1,2,3))

assert sum(WEIGHT) == F(43,96)

def observer(x, y, j, z, t, a, bb, p, q):
    """FULL physical P/Q observer; j is a raw binary upstream history control."""
    i = (1-x)*j
    w = (F(1,4), (1-x)*F(1,4), y*F(1,8), i*F(1,8))
    Q = [w[s]*ALPHA[s]*z[s] for s in range(4)]
    S = [C*Q[s]*t[s] for s in range(4)]
    d = y*F(1,16) + i*F(3,32)
    return (F(107,128)-F(21,128)*x+d/4-sum(p[s]*S[s] for s in range(4)),
            F(13,64)+F(3,64)*x-d/2+sum(q[s]*S[s] for s in range(4))/4,
            3+sum(Q)+sum((1+a[s])*S[s] for s in range(4)),
            3+sum(Q)/2+sum((1+bb[s])*S[s] for s in range(4))/4)

def obs_full(a, bb, p, q):
    for (x,y,j) in product((0,1),repeat=3):
        for tail in product((0,1),repeat=8):
            yield observer(x,y,j,tail[:4],tail[4:],a,bb,p,q)

def obs_lr(a,bb,p,q):
    for (x,y,z,t) in product((0,1),repeat=4):
        yield observer(x,y,y,(z,)*4,(t,)*4,a,bb,p,q)

def time_support_formula(a, rho, n2, n3):
    base = 3*(n2+n3)
    h = n2+n3/2
    f = n2+rho*n3/4
    if f<=0:
        v = base + sum(WEIGHT)*max(F(0),h)
        return v,v
    coeff = tuple(h+C*(1+a[s])*f for s in range(4))
    full = base+sum(WEIGHT[s]*max(F(0),coeff[s]) for s in range(4))
    lr = base+max(F(0), *(sum(WEIGHT[s]*coeff[s] for s in subset) for subset in SUBSETS if subset))
    return full,lr

def exact_support(points,n2,n3):
    return max(n2*v[2]+n3*v[3] for v in points)

def inv_normal(rho,threshold):
    f=F(1)
    h=-C*(1+threshold)
    n3=(h-f)/(F(1,2)-rho/4)
    n2=f-rho*n3/4
    return n2,n3

def time_criterion(a):
    return a[0]>=max(a[1],a[2]) and a[3]==min(a[1],a[2])

CASES = (
 ("uniform",F(1), (F(1,4),)*4),
 ("path_I", F(1), (F(3,4), F(1,2), F(1,4), F(1,4))),
 ("path_BJ",F(1), (F(3,4), F(1,4), F(1,2), F(1,4))),
 ("C_violation",F(1), (F(1,4), F(1,2), F(1,4), F(1,4))),
 ("IJ_violation",F(1), (F(3,4), F(1,2), F(1,2), F(1,4))),
 ("rho_4_5",F(4,5),(F(3,4), F(1,2), F(3,8), F(3,8))),
 ("rho_6_5",F(6,5),(F(1,2), F(1,3), F(1,4), F(1,4))),
)
NORMALS = tuple((F(u),F(v)) for u,v in product(range(-3,4),repeat=2) if u or v)
checks=0
for name,rho,a in CASES:
    bb=tuple(rho*(1+v)-1 for v in a)
    p=q=(F(1,2),)*4
    assert all(0<v<1 for v in a+bb+p+q)
    assert all((1+bb[s])/(1+a[s])==rho for s in range(4))
    full=tuple(obs_full(a,bb,p,q));lr=tuple(obs_lr(a,bb,p,q))
    assert len(full)==2048 and len(lr)==16
    for n2,n3 in NORMALS:
        calculated = time_support_formula(a,rho,n2,n3)
        observed = exact_support(full,n2,n3),exact_support(lr,n2,n3)
        assert calculated == observed, (name, n2,n3,calculated,observed)
        checks+=1
    # For each interval of distinct a-values test one discriminating threshold.
    levels=sorted(set(a));thresholds=[levels[0]-F(1,8)]
    thresholds += [(u+v)/2 for u,v in zip(levels,levels[1:])]
    thresholds += [levels[-1]+F(1,8)]
    gaps=[]
    for threshold in thresholds:
        n2,n3=inv_normal(rho,threshold)
        gap=time_support_formula(a,rho,n2,n3)
        gaps.append(gap[0]-gap[1]);assert gap[0]>=gap[1]
        checks+=1
    assert (all(v==0 for v in gaps))==time_criterion(a), (name,gaps)
    print("CASE",name,"rho",rho,"criterion",time_criterion(a),"threshold_gaps",','.join(map(str,gaps)))

# Explicit strict-positive ratio-balanced counterexample and actual FULL witness.
a=(F(1,4),F(1,2),F(1,4),F(1,4));bb=a;p=q=(F(1,2),)*4
n2,n3=inv_normal(F(1),F(3,8))
assert (n2,n3)==(F(35,12),F(-23,3))
full,lr=time_support_formula(a,F(1),n2,n3)
assert full==F(-1025,72) and lr==F(-4103,288)
assert full-lr==F(1,96)
witness=observer(0,0,0,(0,1,0,0),(0,1,0,0),a,bb,p,q)
assert witness==(F(899,1152),F(125,576),F(10,3),F(25,8)),witness
assert n2*witness[2]+n3*witness[3]==full
assert (full-lr)/(abs(n2)+abs(n3))==F(1,1016)
print("WITNESS","normal",(n2,n3),"FULL",full,"LR",lr,"gap",full-lr,
      "observer",witness,"Linf_lower",F(1,1016))
print("PASS_EXACT_R5_RATIO_BALANCED_TIME_PROJECTION_CLASSIFICATION")
print("TOTAL_EXACT_CHECKS",checks+8, "CASES",len(CASES), "FULL_CONFIGS_PER_CASE",2048,
      "LR_CONFIGS_PER_CASE",16,"SIGNED_NORMALS_PER_CASE",len(NORMALS))
