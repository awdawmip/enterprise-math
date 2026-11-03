"""Exact rational K3 common-terminal-label clock-plane certificate.
Independent computation from the four-observer formulas, no floating point.
Proves no continuum statement by sampling: the analytic argument is in RESEARCH.md.
"""
from fractions import Fraction as F
from itertools import product, combinations

ALPHA = (F(1, 2), F(2, 3), F(1, 2), F(3, 4))
C = (F(1, 8), F(1, 6), F(1, 16), F(3, 32))
FULL_UP = ((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0))
LR_UP = ((0,0,0),(0,1,1),(1,0,0),(1,1,0))
STAGES = ((0,0,0),(1,0,0),(1,1,0),(1,1,1))
COUNT = 0

def equal(a,b):
    global COUNT
    COUNT += 1
    assert a == b, (COUNT, a, b)

def d2(x,y):
    return (x[0]*y[0] + x[1]*y[1])

def dot(a,b):
    return sum((a[i]*b[i] for i in range(len(a))),F(0))

def carriers(corner):
    x,y,i=corner
    return (C[0],F(1-x,6),F(y,16),F(3*i,32))

def stage_vectors(r,v):
    return tuple(((F(0),F(0)),(F(1),F(1,2)),(F(2),F(3,4)),
                  (F(2)+F(2,3)*r[s],F(3,4)+v[s]/6)) for s in range(4))

def clock_obs(sv, corner, k4):
    cs = carriers(corner)
    return tuple(3+sum((cs[s]*sv[s][k4[s]][j] for s in range(4)),F(0)) for j in range(2))

def points(r,v):
    sv=stage_vectors(r,v)
    full=[(clock_obs(sv,cr,k4),(cr,k4)) for cr in FULL_UP for k4 in product(range(4),repeat=4)]
    lr=[(clock_obs(sv,cr,(k,)*4),(cr,(k,)*4)) for cr in LR_UP for k in range(4)]
    return sv,full,lr

def forms(sv):
    return [tuple(sum((carriers(cr)[s]*sv[s][k][j] for s in range(4)),F(0)) for j in range(2)) for cr in LR_UP for k in range(4)]

def h_formula(sv,n):
    full=3*sum(n)+sum((C[s]*max(dot(n,p) for p in sv[s]) for s in range(4)),F(0))
    lr=3*sum(n)+max(dot(n,p) for p in forms(sv))
    return (full,lr)

def candidate_normals(sv):
    lr=forms(sv)
    directions=set()
    for src in sv:
        for p,q in combinations(src,2):
            dx,dy=(p[0]-q[0],p[1]-q[1])
            if dx or dy:
                directions.add((dy,-dx));directions.add((-dy,dx))
    for p,q in combinations(lr,2):
        dx,dy=(p[0]-q[0],p[1]-q[1])
        if dx or dy:
            directions.add((dy,-dx));directions.add((-dy,dx))
    directions.update(((F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1))))
    return sorted({(a/(abs(a)+abs(b)),b/(abs(a)+abs(b))) for a,b in directions})

def cross(o,p,q):
    return (p[0]-o[0])*(q[1]-o[1])-(p[1]-o[1])*(q[0]-o[0])

def hull(points):
    p=sorted(set(points))
    if len(p)<3:return p
    lower=[]
    for x in p:
        while len(lower)>1 and cross(lower[-2],lower[-1],x)<=0:lower.pop()
        lower.append(x)
    upper=[]
    for x in p[::-1]:
        while len(upper)>1 and cross(upper[-2],upper[-1],x)<=0:upper.pop()
        upper.append(x)
    return lower[:-1]+upper[:-1]

def point_in_polygon(poly,p):
    return all(cross(poly[j],poly[(j+1)%len(poly)],p)>=0 for j in range(len(poly)))

def obs4(corner,k4,p,q,r,v):
    x,y,i=map(F,corner)
    d=y/16+F(3)*i/32
    cs=carriers(corner)
    M=[cs[s]*STAGES[k4[s]][0] for s in range(4)]
    S=[F(2,3)*M[s]*STAGES[k4[s]][1] for s in range(4)]
    U=[S[s]*STAGES[k4[s]][2] for s in range(4)]
    return (F(107,128)-F(21)*x/128+d/4-sum(S)/2+sum((p[s]*S[s]/8 for s in range(4)),F(0)),
            F(13,64)+F(3)*x/64-d/2+sum(S)/8+sum((q[s]*S[s]/32 for s in range(4)),F(0)),
            3+sum(M)+F(3,2)*sum(S)+sum((r[s]*U[s] for s in range(4)),F(0)),
            3+sum(M)/2+F(3,8)*sum(S)+sum((v[s]*U[s]/4 for s in range(4)),F(0)))

def all4(p,q,r,v):
    full=[(obs4(cr,k4,p,q,r,v),(cr,k4)) for cr in FULL_UP for k4 in product(range(4),repeat=4)]
    lr=[(obs4(cr,(k,)*4,p,q,r,v),(cr,(k,)*4)) for cr in LR_UP for k in range(4)]
    return full,lr

def test_clock(r,v):
    sv,full,lr=points(r,v)
    rays=candidate_normals(sv)
    for n in rays:
        hf,hl=h_formula(sv,n)
        equal(hf,max(dot(n,p) for p,_ in full))
        equal(hl,max(dot(n,p) for p,_ in lr))
    return sv,full,lr,rays

q=lambda *s:tuple(F(t) for t in s)
R=q('4/5','4/5','1/5','1/5');V=tuple(t/2 for t in R)
P=q('1/4','1/2','3/4','1/2');Q=q('3/4','1/2','1/4','1/2')
sv,full,lr,rays=test_clock(R,V)
clock_poly=hull([p for p,_ in lr]);full_poly=hull([p for p,_ in full])
equal(clock_poly, full_poly)
for p,_ in full:equal(point_in_polygon(clock_poly,p),True)
for n in rays:equal(h_formula(sv,n)[0],h_formula(sv,n)[1])

# Crosscheck the exact formula for all signed clock directions on other kernels.
varied=q('1/5','1/2','1/5','1/2');variedv=q('4/5','9/10','4/5','9/10')
for rr,vv in ((R,V),(varied,variedv),(q('1/2','1/2','1/2','1/2'),q('3/4','3/4','3/4','3/4'))):
    _,full_points,lr_points,_,=test_clock(rr,vv)
    equal(len(full_points),1536);equal(len(lr_points),16)

# Test distinct continuous-family inputs (the all-real theorem is proved separately).
family_models=0
family_rays=0
for large,small,k in ((F(3,4),F(1,4),F(1,3)),(F(4,5),F(1,5),F(1,2)),
                      (F(2,3),F(1,3),F(1)),(F(3,5),F(2,5),F(3,4)),
                      (F(1,2),F(1,2),F(1,4))):
    rr=(large,large,small,small);vv=tuple(k*t for t in rr)
    assert all(F(0)<a<F(1) for a in rr+vv)
    stage=stage_vectors(rr,vv);ns=candidate_normals(stage)
    for n in ns: equal(h_formula(stage,n)[0],h_formula(stage,n)[1])
    family_models+=1;family_rays+=len(ns)

# Same physical FULL history point simultaneously separates two mixed directions.
f4,l4=all4(P,Q,R,V)
w=obs4((0,1,1),(3,3,1,1),P,Q,R,V)
normals4=((F(8),F(0),F(28,9),-F(56,9)),
          (F(0),-F(32),F(4),-F(8)))
expected=(( -F(1597,720),-F(821,360),F(1,16)),
          (-F(3803,240),-F(3823,240),F(1,12)))
gaps=[]
for n,(ef,el,eg) in zip(normals4,expected):
    hf=max(dot(n,p) for p,_ in f4);hl=max(dot(n,p) for p,_ in l4)
    equal(hf,ef);equal(hl,el);equal(hf-hl,eg);equal(dot(n,w),hf)
    gaps.append(eg/sum(map(abs,n)))
equal(w,(F(907,1152),F(235,1536),F(5609,1440),F(9551,2880)))
equal(gaps[0],F(3,832));equal(gaps[1],F(1,528))

print('clock_analytic_formulas=FULL_4_stage_max/LR_16_corner_stage_max')
print('clock_family=(r_C=r_I=R, r_BJ=r_IJ=L, v_s=k*r_s; 0<L<=R<1, 0<k<=1)')
print('clock_equality_candidate_r', R, 'v',V)
print('clock_hull_vertices', len(clock_poly), 'polygon',clock_poly)
print('clock_full_deterministic_checked',len(full),'clock_LR_deterministic_checked',len(lr))
print('clock_normal_fan_exact_rays',len(rays))
print('other_family_models',family_models,'family_rays',family_rays)
print('mixed_full_witness',w,'stages',(3,3,1,1))
for n,(hf,hl,g) in zip(normals4,expected):print('mixed_normal',n,'h_FULL',hf,'h_LR',hl,'gap',g,'distance_lower',g/sum(map(abs,n)))
print('assertions',COUNT)
print('PASS_EXACT_R5_K3_FULL_CLOCK_PLANE_EQUAL_NONUNIFORM_FAMILY')
