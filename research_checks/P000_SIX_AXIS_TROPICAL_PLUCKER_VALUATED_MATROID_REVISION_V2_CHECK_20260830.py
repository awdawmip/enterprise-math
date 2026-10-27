#!/usr/bin/env python3
from itertools import product, permutations
from collections import Counter

LABELS = ("AB","AC","AD","BC","BD","CD")
EDGES = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
EDGE_INDEX = {e:i for i,e in enumerate(EDGES)}
COMP = (5,4,3,2,1,0)
PAIR_BLOCKS = ((0,5),(1,4),(2,3))

checks = 0
def check(cond, msg):
    global checks
    if not cond:
        raise AssertionError(msg)
    checks += 1

def pair_sums_from_weights(w):
    return (w[0]+w[5], w[1]+w[4], w[2]+w[3])

def delta_from_sums(s):
    a,b,c = sorted(s)
    return b-a

def delta_from_weights(w):
    return delta_from_sums(pair_sums_from_weights(w))

def raw_weights(x):
    return tuple(x)

def abs_weights(x):
    return tuple(abs(v) for v in x)

def vp(n,p):
    if n == 0:
        raise ValueError("W_VP finite valuation domain is Z\\{0}; zero is outside the theorem domain")
    n=abs(n); c=0
    while n%p==0:
        n//=p; c+=1
    return c

def vp_weights(x,p):
    if any(v == 0 for v in x):
        raise ValueError("W_VP requires all six coordinates nonzero")
    return tuple(vp(v,p) for v in x)

def Q(x):
    return x[0]*x[5]-x[1]*x[4]+x[2]*x[3]

def pair_products(x):
    return (x[0]*x[5], x[1]*x[4], x[2]*x[3])

def q_orb(x):
    t=pair_products(x); S=sum(t)
    return tuple(sorted(S-2*z for z in t))

def rho(x):
    return ((x[0]-x[5])%2,(x[1]-x[4])%2,(x[2]-x[3])%2,sum(x)%3)

def rho_orb(x):
    r=rho(x)
    return (tuple(sorted(r[:3])), r[3])

def johnson_coarse(x):
    s=pair_sums_from_weights(x)
    d=(x[0]-x[5],x[1]-x[4],x[2]-x[3])
    total=sum(x)
    p0_scaled=sum(z*z for z in d) # = 2 ||P0 x||^2
    pm2_scaled=3*sum(z*z for z in s)-sum(s)**2 # = 6 ||Pm2 x||^2
    return (total,p0_scaled,pm2_scaled)

def edge_action(vertex_perm):
    out=[None]*6
    for i,(a,b) in enumerate(EDGES):
        e=tuple(sorted((vertex_perm[a],vertex_perm[b])))
        out[i]=EDGE_INDEX[e]
    return tuple(out)

def apply_edge_perm(x, act):
    y=[None]*6
    for old,new in enumerate(act):
        y[new]=x[old]
    return tuple(y)

S4_ACTIONS=[edge_action(p) for p in permutations(range(4))]
check(len(set(S4_ACTIONS))==24, "carrier S4 edge action must be faithful")

block_of={}
for j,block in enumerate(PAIR_BLOCKS):
    block_of[frozenset(block)]=j
induced=[]
for act in S4_ACTIONS:
    bperm=[]
    for block in PAIR_BLOCKS:
        image=frozenset(act[i] for i in block)
        bperm.append(block_of[image])
    induced.append(tuple(bperm))
check(len(set(induced))==6, "S4 must induce full S3 on complementary pairs")
check(sum(1 for p in induced if p==(0,1,2))==4, "kernel on pair blocks must be V4/order 4")

def stabilizer_size(pattern):
    n=0
    for bp in induced:
        y=[None]*3
        for old,new in enumerate(bp):
            y[new]=pattern[old]
        if tuple(y)==tuple(pattern):
            n+=1
    return n
check(stabilizer_size((0,1,2))==4, "all-distinct pair-sum stabilizer")
check(stabilizer_size((0,0,1))==8, "two-equal pair-sum stabilizer")
check(stabilizer_size((0,0,0))==24, "triple-tie pair-sum stabilizer")

sample=(-2,-1,0,2,1,3)
s=pair_sums_from_weights(sample)
check(delta_from_sums(s)==sum(s)-max(s)-2*min(s), "exact defect formula")
for wf in (raw_weights, abs_weights):
    d0=delta_from_weights(wf(sample))
    for act in S4_ACTIONS:
        check(delta_from_weights(wf(apply_edge_perm(sample,act)))==d0, "S4 invariance")
    check(delta_from_weights(wf(tuple(sample[i] for i in COMP)))==d0, "complement invariance")

def raw_census(B):
    cnt=Counter()
    for x in product(range(-B,B+1), repeat=6):
        d=delta_from_weights(x)
        cnt["total"]+=1
        cnt["surv" if d==0 else "nonsurv"]+=1
    return cnt

def raw_formula(B):
    q=2*B+1
    triple=q*q*(q*q+1)//2
    two_min=q*q*(q-1)*(4*q*q+q+3)//4
    surv=q*q*(4*q**3-q*q+2*q-1)//4
    all_distinct=q**6-triple-2*two_min
    return dict(total=q**6, triple=triple, two_min=two_min, surv=surv, all_distinct=all_distinct)

for B, expected_surv in ((1,234),(2,3025)):
    c=raw_census(B); f=raw_formula(B)
    check(c["surv"]==expected_surv, f"raw census B={B}")
    check(c["surv"]==f["surv"], f"raw formula B={B}")
    check(c["total"]==f["total"], f"raw total B={B}")
    check(f["triple"]+f["two_min"]==f["surv"], f"raw strata B={B}")
    check(f["triple"]+2*f["two_min"]+f["all_distinct"]==f["total"], f"raw partition B={B}")

def abs_census(B):
    cnt=Counter()
    for x in product(range(-B,B+1), repeat=6):
        d=delta_from_weights(abs_weights(x))
        cnt["total"]+=1
        cnt["surv" if d==0 else "nonsurv"]+=1
    return cnt
check(abs_census(1)["surv"]==345, "abs census B=1")
check(abs_census(2)["surv"]==5257, "abs census B=2")

def vp_census(vals,p):
    cnt=Counter()
    for x in product(vals, repeat=6):
        d=delta_from_weights(vp_weights(x,p))
        cnt["total"]+=1
        cnt["surv" if d==0 else "nonsurv"]+=1
    return cnt
check(vp_census((-2,-1,1,2),2)["surv"]==1984, "v2 census")
check(vp_census((-4,-3,-2,-1,1,2,3,4),3)["surv"]==176320, "v3 census")

xa=(-2,-2,0,2,1,1)
xb=(-2,-1,-1,2,2,0)
check(johnson_coarse(xa)==johnson_coarse(xb)==(0,22,18), "matched Johnson coarse invariants")
check(q_orb(xa)==q_orb(xb)==(-4,0,0), "matched Q_orb")
check(rho_orb(xa)==rho_orb(xb)==((0,1,1),0), "matched rho orbit")
check(delta_from_weights(xa)==0 and delta_from_weights(xb)==3, "delta separates matched controls")

x0=(0,0,0,0,0,0)
xe=(1,0,0,0,0,0)
x1=(1,1,1,1,1,1)
check(delta_from_weights(x0)==delta_from_weights(xe)==delta_from_weights(x1)==0, "same-delta controls")
check(rho(x0)!=rho(xe), "same delta different rho")
check(q_orb(x0)!=q_orb(x1), "same delta different Q_orb")

# Exact W_VP theorem domain:
# D_p = {(x_AB,...,x_CD) in Z^6 : every coordinate is nonzero}.
# For x in D_p, all three pair products are nonzero and alpha_i are finite naturals.
vals3=(-4,-3,-2,-1,1,2,3,4)
for x in product(vals3, repeat=6):
    w=vp_weights(x,3)
    alpha=pair_sums_from_weights(w)
    d=delta_from_sums(alpha)
    qv=Q(x)
    if d>0:
        check(qv!=0, "unique finite minimum forbids Q=0")
        check(vp(qv,3)==min(alpha), "unique-min finite valuation law")
    if qv==0:
        check(d==0, "Q=0 forces tropical tie on finite nonzero domain")

# Independent smaller p=2 regression of the same implication.
vals2=(-2,-1,1,2)
for x in product(vals2, repeat=6):
    w=vp_weights(x,2)
    alpha=pair_sums_from_weights(w)
    d=delta_from_sums(alpha)
    qv=Q(x)
    if d>0:
        check(qv!=0, "p=2 unique finite minimum forbids Q=0")
        check(vp(qv,2)==min(alpha), "p=2 unique-min finite valuation law")
    if qv==0:
        check(d==0, "p=2 Q=0 forces tropical tie on finite nonzero domain")

# Boundary contract: any zero coordinate is OUTSIDE W_VP and must fail closed.
for i in range(6):
    z=[1]*6
    z[i]=0
    try:
        vp_weights(tuple(z),3)
    except ValueError:
        check(True, f"zero-coordinate boundary excluded at slot {i}")
    else:
        check(False, f"zero-coordinate boundary must be excluded at slot {i}")

# All-zero and partially-zero points are explicitly not assigned delta_T under W_VP.
for z in ((0,0,0,0,0,0),(0,1,1,1,1,1),(1,1,0,1,1,1)):
    try:
        vp_weights(z,2)
    except ValueError:
        check(True, "partially/all-zero W_VP boundary excluded")
    else:
        check(False, "zero-containing point entered finite W_VP domain")

z0=(1,1,1,3,4,1)
z1=(1,1,1,3,1,1)
z2=(1,1,1,3,2,1)
vw=vp_weights(z0,3)
check(vp_weights(z1,3)==vw and vp_weights(z2,3)==vw==(0,0,0,1,0,0), "same valuation vector")
check(delta_from_weights(vw)==0, "valuation matched controls are tropical")
check(Q(z0)==0 and Q(z1)==3 and Q(z2)==2, "Q residue separation")
check(vp(Q(z1),3)==1 and vp(Q(z2),3)==0, "Q valuation residue separation")

print(f"LOCAL_DETERMINISTIC_PASS checks={checks}")
