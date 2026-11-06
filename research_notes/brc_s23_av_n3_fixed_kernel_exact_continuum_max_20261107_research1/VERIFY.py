#!/usr/bin/env python3
"""Exact self-contained certificate for a fixed S23 conditional AV 8x27 kernel.

Uses only Python standard-library integer/Fraction arithmetic.
No floating point values enter assertions.
"""
from fractions import Fraction as Q
from math import comb
from itertools import product

DEN=1_000_000
ROWS=[
 {13:1000000},
 {1:479665,12:520335},
 {9:296273,10:703727},
 {2:419643,15:48185,18:405725,21:112202,26:14245},
 {1:139862,4:683322,9:176816},
 {6:230562,9:106277,11:120245,12:56752,14:50073,15:71369,16:50073,17:25415,19:120245,22:50462,23:25415,24:70684,25:22428},
 {1:20822,3:400945,4:11265,5:119554,6:192951,7:125268,8:65023,20:64172},
 {0:747749,1:99382,3:52308,4:2315,6:2609,9:87375,10:3741,18:4521}
]
assert len(ROWS)==8 and all(sum(row.values())==DEN for row in ROWS)
FULL=list(product(range(3), repeat=3)); OBS=list(product(range(2), repeat=3))

# Polynomial coefficient dictionaries in a^i c^j; integer arithmetic.
def add(*ps):
    d={}
    for p in ps:
        for key,v in p.items():d[key]=d.get(key,0)+v
    return {k:v for k,v in d.items() if v}
def scale(p,k):return {m:k*v for m,v in p.items() if k*v}
def mul(p,q):
    d={}
    for (i,j),v in p.items():
        for (k,l),w in q.items():d[(i+k,j+l)]=d.get((i+k,j+l),0)+v*w
    return {k:v for k,v in d.items() if v}
def tensor_poly(p,index):
    d={(0,0):1}
    for k in index:d=mul(d,p[k])
    return d
A={(1,0):1}; ONE={(0,0):1}; OM_A=add(ONE,scale(A,-1)); C={(0,1):1}; OM_C=add(ONE,scale(C,-1))
Z=mul(OM_A,C); FULL_P=[A,Z,mul(OM_A,OM_C)]; OBS_P=[Z,add(ONE,scale(Z,-1))]
Fp=[tensor_poly(FULL_P,t) for t in FULL]
Op=[tensor_poly(OBS_P,t) for t in OBS]
G=[]
for j in range(27):
    G.append(add(scale(Fp[j],DEN), *[scale(Op[i],-ROWS[i].get(j,0)) for i in range(8)]))
assert not G[13]

def evalpoly(p,a,c):
    return sum(v*a**i*c**j for (i,j),v in p.items())

def bern(p,arange,crange,deg_a,deg_c):
    """Exact tensor Bernstein control coefficients on a rectangular box."""
    a0,a1=arange;c0,c1=crange
    da=a1-a0;dc=c1-c0
    power={}
    for (i,j),v in p.items():
        for u in range(i+1):
            for w in range(j+1):
                val=v*comb(i,u)*a0**(i-u)*da**u*comb(j,w)*c0**(j-w)*dc**w
                power[u,w]=power.get((u,w),0)+val
    return [[sum(power.get((u,w),0)*Q(comb(h,u),comb(deg_a,u))*Q(comb(k,w),comb(deg_c,w)) for u in range(h+1) for w in range(k+1)) for k in range(deg_c+1)] for h in range(deg_a+1)]

BOX_A=(Q(17,25),Q(73,100));BOX_C=(Q(17,20),Q(7,8))
point_a,point_c=Q(7,10),Q(43,50)
SIGNS=[(1 if evalpoly(g,point_a,point_c)>0 else -1 if evalpoly(g,point_a,point_c)<0 else 0) for g in G]
assert SIGNS==[1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
# Sign certificate ensures TV = (sum_j sign_j G_j)/(2 DEN) throughout BOX.
margin=min(sign*b for sign,g in zip(SIGNS,G) if sign for line in bern(g,BOX_A,BOX_C,3,3) for b in line)
assert margin==Q(2999060771571,1600000000)>0
P=add(*[scale(g,sign) for sign,g in zip(SIGNS,G) if sign])
Pdc={(i,j-1):j*v for (i,j),v in P.items() if j>=1}
dc_min=min(x for row in bern(Pdc,BOX_A,BOX_C,3,2) for x in row)
assert dc_min==Q(57424508055009,32000000)>0
# Polynomial for the c=7/8 boundary (all parameters exact).
edge={}
for (i,j),v in P.items():edge[i]=edge.get(i,Q(0))+v*Q(7,8)**j
assert [edge.get(i,0)/2/DEN for i in range(4)]==[
    Q(-152165297,512000000),Q(365908179,512000000),
    Q(611013165,512000000),Q(-821105487,512000000)]

def Tedge(x):return sum(edge.get(i,0)*x**i for i in range(4))/2/DEN

def Dedge(x):return sum(i*edge.get(i,0)*x**(i-1) for i in range(1,4))/2/DEN
assert Dedge(BOX_A[0])==Q(17653977,156250000)>0
assert Dedge(BOX_A[1])==Q(-547139421669,5120000000000)<0
assert all(2*edge[2]+6*edge[3]*x<0 for x in BOX_A)

# Global certificate: exact 257x257 grid, all 27 signed residuals per point.
N=256; D=8*N
GRID=[[0]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    anum=4*N+3*i
    for j in range(N+1):
        cnum=4*N+3*j
        pp=[anum*D,(D-anum)*cnum,(D-anum)*(D-cnum)]
        bb=[pp[1],D*D-pp[1]]
        full=[pp[s0]*pp[s1]*pp[s2]*DEN for s0,s1,s2 in FULL]
        obs=[bb[s0]*bb[s1]*bb[s2] for s0,s1,s2 in OBS]
        rec=[0]*27
        for u,row in enumerate(ROWS):
            for v,weight in row.items():rec[v]+=obs[u]*weight
        GRID[i][j]=sum(abs(x-y) for x,y in zip(full,rec))
base_den=2*DEN*D**6
out_max=-1;out_ij=None;inside_cells=0
for i in range(N):
    aa=Q(4*N+3*i,D);bb=Q(4*N+3*(i+1),D)
    for j in range(N):
        cc=Q(4*N+3*j,D);dd=Q(4*N+3*(j+1),D)
        if aa>=BOX_A[0] and bb<=BOX_A[1] and cc>=BOX_C[0] and dd<=BOX_C[1]:
            inside_cells+=1
        else:
            for u,v in ((i,j),(i+1,j),(i,j+1),(i+1,j+1)):
                if GRID[u][v]>out_max:
                    out_max,out_ij=GRID[u][v],(u,v)
out_edge=Q(out_max,base_den)
assert out_ij==(0,0) and out_edge==Q(15172039,64000000)
assert inside_cells==578
# Bilinear Peano remainder from earlier proven lemma for the whole AV box.
err=Q(3915,8192*N*N)
witness=Tedge(Q(35319,50000))
assert out_edge+err < witness
# Positive root of stationary quadratic unique on BOX_A; exact algebraic value.
assert edge[3]<0
print("KERNEL_ROWS=8; ROW_SUMS=1000000; RESIDUAL_COORDINATES=27")
print("BERNSTEIN_SIGN_MIN_G="+str(margin)+" (divide by 1000000 for residuals)")
print("BERNSTEIN_D_C_MIN_P="+str(dc_min)+" (divide by 2000000 for TV derivative)")
print("EDGE_TV_POLY_COEFFS="+str([edge.get(i,0)/2/DEN for i in range(4)]))
print("GRID_N=256; GRID_POINTS="+str((N+1)**2)+"; OUTSIDE_CELLS="+str(N*N-inside_cells))
print("OUTSIDE_GRID_MAX="+str(out_edge)+"; LOCATION="+str(out_ij))
print("OUTSIDE_CONTINUUM_CERT="+str(out_edge+err)+"; EDGE_RATIONAL_WITNESS="+str(witness))
print("RESULT: EXACT_GLOBAL_SUPREMUM_OF_FIXED_K = T(alpha,7/8), alpha unique root in [17/25,73/100] of -2463316461*x^2+1222026330*x+365908179=0")
print("PASS_S23_N3_FIXED_KERNEL_GLOBAL_BOUNDARY_BERNSTEIN_20261107")
