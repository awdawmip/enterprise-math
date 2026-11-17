"""Exact branch-level R5 Y-to-L merger checker; standard library only."""
from fractions import Fraction as F
from itertools import product
from math import gcd

Y, L = F(1, 8), F(1, 4)
M = 1 - 2*Y - F(3, 2)*L
H = Y + L/2
LOW, HIGH = F(1, 8), F(7, 8)
assert all(v > 0 for v in (Y, L, M, H))
assert sum((Y, L, M, H)) == 1
assert sum((Y/2, 3*L/4, M, 3*H/2)) == 1
assert LOW > 0 and HIGH < 1


def observe(clones):
    """A_i=(x_i,u_i,v_direct_i,v_via_Y_i). Other origins stop at t=1."""
    ep = eq = tp = tq = F(0)
    def leaf(p, q, t, err):
        nonlocal ep, eq, tp, tq
        ep += p*err
        eq += q*err
        tp += p*t
        tq += q*t
    # B,C0,C1 total P/Q weights are 1/2 and 3/4 respectively.
    leaf(F(1, 2), F(3, 4), 1, LOW)
    for x, u, vd, vy in clones:
        p0, q0 = F(1, 4), F(1, 8)
        leaf(p0*(1-x), q0*(1-x), 1, LOW)
        py, qy = p0*x*Y/2, q0*x*Y
        leaf(py*(1-u), qy*(1-u), 2, LOW)
        leaf(py*u/4, qy*u/2, 3, HIGH)  # Y -> M
        pyl, qyl = py*u*F(3, 4), qy*u/2
        leaf(pyl*(1-vy), qyl*(1-vy), 3, LOW)
        leaf(pyl*vy, qyl*vy, 4, HIGH)
        pl, ql = p0*x*3*L/4, q0*x*L
        leaf(pl*(1-vd), ql*(1-vd), 3, LOW)
        leaf(pl*vd, ql*vd, 4, LOW)
        leaf(p0*x*M, q0*x*M, 3, LOW)
        leaf(p0*x*3*H/2, q0*x*H, 3, LOW)
    return (ep, eq, tp, tq)


def lr(x,u,v):
    return observe(((x,u,v,v), (x,u,v,v)))


def dot(a,b):
    return sum((s*t for s,t in zip(a,b)), F(0))


def determinant(rows):
    a = [list(row) for row in rows]
    ans = F(1)
    for j in range(4):
        pos = next((i for i in range(j,4) if a[i][j]), None)
        if pos is None: return F(0)
        if pos != j:
            a[j],a[pos] = a[pos],a[j]
            ans = -ans
        piv = a[j][j]
        ans *= piv
        for i in range(j+1,4):
            r = a[i][j]/piv
            for t in range(j,4): a[i][t] -= r*a[j][t]
    return ans

base=lr(F(0),F(0),F(0))
A=tuple(a-b for a,b in zip(lr(F(1),0,0),base))
B=tuple(a-b for a,b in zip(lr(F(1),1,0),lr(F(1),0,0)))
C=tuple(a-b for a,b in zip(lr(F(1),0,1),lr(F(1),0,0)))
D=tuple(a-b-c-d-e for a,b,c,d,e in zip(lr(F(1),1,1),base,A,B,C))
rows=tuple(zip(A,B,C,D))
rank_det=determinant(rows)
assert base==(LOW,LOW,1,1)
assert A==(0,0,F(31,32),F(15,32))
assert B==(F(3,512),F(3,256),F(1,32),F(1,32))
assert C==(0,0,F(3,32),F(1,16))
assert D==(F(9,512),F(3,256),F(3,128),F(1,64))
assert rank_det==F(153,67108864)

h=(42,107,45,-93)
hcols=tuple(dot(h,col) for col in (A,B,C,D))
assert hcols==(0,0,-F(51,32),F(51,32))
all_lr=[lr(*map(F,abc)) for abc in product((0,1),repeat=3)]
all_full=[observe((tuple(map(F,b[:4])),tuple(map(F,b[4:])))) for b in product((0,1),repeat=8)]
assert len(all_lr)==8 and len(all_full)==256
assert max(map(lambda o:dot(h,o),all_lr))==dot(h,base)==-F(235,8)
assert max(map(lambda o:dot(h,o),all_full))==-F(889,32)
assert max(map(lambda o:dot(h,o),all_full))-max(map(lambda o:dot(h,o),all_lr))==F(51,32)

midpoint=tuple((a+b)/2 for a,b in zip(lr(1,0,0),lr(1,1,1)))
actual_full=observe(((F(1),F(0),F(0),F(0)),(F(1),F(1),F(1),F(1))))
assert midpoint==actual_full==(F(35,256),F(35,256),F(523,256),F(195,128))

# Check every deterministic FULL time vector has an explicit real LR representative.
kappa=Y/(2*L)
for bits in product((0,1),repeat=8):
    ((x0,u0,vd0,vy0),(x1,u1,vd1,vy1))=(bits[:4],bits[4:])
    xx=F(x0+x1,2)
    aa=F(x0*u0+x1*u1,2)
    bb=F(x0*vd0+x1*vd1,2)
    cc=F(x0*u0*vy0+x1*u1*vy1,2)
    eff=bb+kappa*cc
    uu=aa/xx if xx else F(0)
    vv=eff/(xx+kappa*aa) if xx+kappa*aa else F(0)
    assert 0<=uu<=1 and 0<=vv<=1
    assert observe((tuple(map(F,bits[:4])),tuple(map(F,bits[4:]))))[2:] == lr(xx,uu,vv)[2:]

# Seedless LR monomials have p1*p4-p2*p3=0. Midpoint monomials
# (1,1/2,1/2,1/2) have residual 1/4. Verify the exact inverse
# and its infinity operator norm (max absolute row sum).
inverse = (
    (-F(256,51),F(128,17),F(64,17),-F(96,17)),
    (-F(256,3),F(128),F(0),F(0)),
    (F(3008,51),-F(5600,51),-F(480,17),F(992,17)),
    (F(256,3),-F(128,3),F(0),F(0)),
)
for i in range(4):
    for j in range(4):
        assert sum(inverse[i][k]*rows[k][j] for k in range(4))==int(i==j)
inv_norm=max(sum(abs(a) for a in row) for row in inverse)
assert inv_norm==F(13024,51)
# The residual is at most 4*||p-p_mid||_inf by product Lipschitzness,
# and ||p-p_mid||_inf <= ||inverse||_inf ||O-O_mid||_inf.
assert F(1,16)/inv_norm==F(51,208384)
print('Y,L,M,H =',*(str(t) for t in (Y,L,M,H)))
print('BASE =',base)
print('M_COLUMNS =',A,B,C,D)
print('DET =',rank_det)
print('H_COLUMNS =',hcols)
print('FULL_COUNT =',len(all_full),'LR_COUNT =',len(all_lr))
print('H_MAX_FULL =',max(dot(h,o) for o in all_full))
print('H_MAX_LR =',max(dot(h,o) for o in all_lr))
print('MIDPOINT_FULL =',midpoint)
print('LR_TIME_RECONSTRUCTION = PASS (all 256 FULL deterministic policies)')
print('LR_REAL_IMAGE_DISTANCE_INF_AT_LEAST =',F(51,208384))
print('PASS_EXACT_R5_YL_PATH_SENSITIVE_ERROR_HULL_OBSTRUCTION')
