#!/usr/bin/env python3
"""Exact Fraction checks for S23 n=3 sharp-value rigidity and candidate witness.

These are finite symbolic identity checks.  The all-real implication is proved in
PROOF.md via TV triangle equality and a two-sided tangent argument.
"""
from fractions import Fraction as F
from math import comb, factorial

z0=F(1,4)
d=F(5211,21952)
hist=[(i,j,3-i-j) for i in range(4) for j in range(4-i)]
assert len(hist)==10
mult=[factorial(3)//(factorial(a)*factorial(b)*factorial(c)) for a,b,c in hist]
assert sum(mult)==27
A=[j for j,h in enumerate(hist) if h[2]>0]
C=hist.index((0,3,0))
B=[j for j in range(10) if j not in A and j!=C]
assert len(A)==6 and len(B)==3 and C==3

def q(a,z,b):
    return [F(m)*a**h[0]*z**h[1]*b**h[2] for m,h in zip(mult,hist)]
def tv(x,y):return sum((abs(a-b) for a,b in zip(x,y)),F(0))/2
Qminus=q(F(5,7),z0,F(1,28))
Qplus=q(F(1,2),z0,F(1,4))
assert sum(Qminus)==sum(Qplus)==1
assert tv(Qminus,Qplus)==2*d
assert all(Qminus[j]<=Qplus[j] for j in A)
assert all(Qminus[j]>=Qplus[j] for j in B)
assert Qminus[C]==Qplus[C]==z0**3
Aminus=sum(Qminus[j] for j in A)
Aplus=sum(Qplus[j] for j in A)
assert Aminus==F(2269,21952)
assert Aplus==F(37,64)
mid=(Aminus+Aplus)/2
assert mid==F(935,2744)
assert mid-Aminus==d

# Bernstein input weights and derivatives at z=1/4.
w=[F(comb(3,k))*z0**(3-k)*(1-z0)**k for k in range(4)]
wp=[F(3,16),F(15,16),F(9,16),-F(27,16)]
assert w==[F(1,64),F(9,64),F(27,64),F(27,64)]
A_tangent=F(2187,5488) # derivative of 1-(1-z/7)^3 at z0
assert A_tangent==F(3,7)*(1-z0/7)**2
assert F(81,686)==F(6,49)*(1-z0/7)

# Equalities for an exact minimax kernel:
# q0+9q1+27q2+27q3=1, 3q0+15q1+9q2-27q3=3.
# Subtracting three times the first forces 12q1+72q2+108q3=0.
# With qk>=0, q1=q2=q3=0 and q0=1. First row is deterministic 111.
assert [3*64*w[k]-16*wp[k] for k in range(4)]==[F(0),F(12),F(72),F(108)]
# Remaining 3x9 stochastic rows = 24 affine degrees; two independent
# event-A value/tangent equations leave affine dimension 22.
assert F(64)*mid==F(7480,343)
assert F(16)*A_tangent==F(2187,343)
# With u=K[1,A],v=K[2,A], t=K[3,A],
# the two independent equations imply u=3t-919/12348,
# v=30839/37044-2t.
tmin=F(919,37044)
tmax=F(13267,37044)
for t in [tmin,F(1,10),tmax]:
    u=3*t-F(919,12348)
    v=F(30839,37044)-2*t
    assert 0<=u<=1 and 0<=v<=1 and 0<=t<=1
    assert 9*u+27*v+27*t==F(7480,343)
    assert 15*u+9*v-27*t==F(2187,343)
assert F(1,10)>tmin and F(1,10)<tmax

# Previously published candidate K, in lexicographically ordered
# histogram columns (h0,h1,h2) above. Denominator = 10^14.
D=10**14
K=[
[0,0,0,100000000000000,0,0,0,0,0,0],
[0,0,0,0,0,0,1747112991682,0,98252887008318,0],
[121269627318,444444444444,11084232590318,0,22195343701318,12471322964682,16568032896677,31974633557918,10312735866,5130407481459],
[5375704166,0,26622927530,0,26878520682,0,5071818328318,2418691424318,32373716247318,60076896847668],
]
assert all(len(row)==10 and min(row)>=0 and sum(row)==D for row in K)
assert K[0][C]==D and all(K[k][C]==0 for k in [1,2,3])
G=[F(sum(row[j] for j in A),D) for row in K]
assert G[0]==G[1]==0

def g(zz):
    return sum((F(comb(3,k))*zz**(3-k)*(1-zz)**k*G[k] for k in range(4)),F(0))
def amin(zz):return 1-(1-zz/7)**3
assert g(z0)-mid==F(4567,1097600000000000000)
gp=sum((wp[k]*G[k] for k in range(4)),F(0))
assert gp-A_tangent==F(4031654829417,54880000000000000)

# A rational cross-fiber witness: z != z0, c=7/8,
# a=1-8z/7 remains lawful.  TV dominates A-event discrepancy.
zstar=z0+F(1,77000)
astar=1-F(8,7)*zstar
cstar=F(7,8)
bstar=zstar/7
assert F(1,2)<=astar<=F(7,8)
assert F(1,2)<=cstar<=F(7,8)
assert (1-astar)*cstar==zstar
wm=[F(comb(3,k))*zstar**(3-k)*(1-zstar)**k for k in range(4)]
M=[sum((wm[k]*F(K[k][j],D) for k in range(4)),F(0)) for j in range(10)]
Q=q(astar,zstar,bstar)
assert sum(M)==sum(Q)==1
lower=g(zstar)-amin(zstar)
assert lower==sum((M[j]-Q[j] for j in A),F(0))
excess=lower-d
assert excess==F(3744518316297327234357,7829540950000000000000000000000)
assert tv(M,Q)>=lower>d
assert excess>F(47,10**11) and excess<F(49,10**11)
print("PASS_S23_N3_SHARP_FACE_TANGENCY_RIGIDITY_20261107")
print("fiber_radius",d,"fiber_diameter",2*d)
print("A_mid",mid,"A_prime_top",A_tangent)
print("necessary_111_row",[1,0,0,0],"kernel_face_dimensions",22)
print("A_aggregate_u", "3t-919/12348", "v", "30839/37044-2t", "t_interval",tmin,tmax)
print("candidate_tangent_defect",gp-A_tangent)
print("cross_fiber_z",zstar,"a",astar,"c",cstar)
print("candidate_event_lower_excess_over_d",excess)
print("candidate_event_lower_excess_decimal",float(excess))
print("candidate_full_tv_excess_decimal",float(tv(M,Q)-d))
