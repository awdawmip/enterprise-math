#!/usr/bin/env python3
"""R5 exact derivative correction and robust 8D Hadamard support certificate.
Frozen seven-LR physical model from PR #1902 / PR #1923.
Center 4845-case support exclusion and dual inequalities are inherited, not rerun.
Requires sympy; arithmetic is exact rational.
"""
from fractions import Fraction as F
from sympy import Matrix, Rational

def Q(s): return tuple(F(v) for v in s.split())
r=Q("1/10 1/2 3/4 1 5/4 3/2 19/10")
def mass(x):
    g,a,b,u,v,w,z=x
    return (
        F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
        F(13,40)*a+b/80-u, (g-a)/2,
        1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
        (g-b)/2,F(3,40)*a+F(21,80)*b-w,
        u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)
def restrictions(p):
    x,y=p[:7],p[7:]
    return (x[0]-x[2],y[0]-1,y[6]-y[1]/10,
            *(a-b for a,b in zip(times(x),times(y))))
def slacks(x):
    g,a,b,u,v,w,z=x
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def both_slacks(p): return slacks(p[:7])+slacks(p[7:])
def rhs(p):
    mu,nu=mass(p[7:]),mass(p[:7])
    return mu+nu+tuple(r[j]*nu[j] for j in range(7))
def deficits(p):
    b=rhs(p);return tuple(b[7+j]-b[j] for j in (1,2,3,5))
def jac(fun):
    z=(F(0),)*14; f0=fun(z)
    return Matrix([[Rational(fun(tuple(F(i==j) for i in range(14)))[k]-f0[k])
                    for j in range(14)] for k in range(len(f0))])
Jc=jac(restrictions);Jb=jac(rhs);N=Jc.nullspace()
assert Jc.rank()==5 and len(N)==9
P=Matrix.hstack(*(N[i] for i in (0,1,2,4,5,6,7,8)))
B8=Jb*P
assert B8.rank()==8
X0=Q("999/1000 1/6 999/1000 1/20 29/240 11/160 1/120")
Y0=Q("1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200")
DY=Q("0 1 0 -1/4 -1/4 0 1/10")
H=F(17774559,17507527960)
p=(X0[:6]+(X0[6]+H/2,))+tuple(y+F(1,100000)*d for y,d in zip(Y0,DY))
assert restrictions(p)==(F(0),)*5
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in(0,6) or i==j)
SB=((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),(0,3),(1,3),
    (3,3),(4,3),(5,3),(4,5),(5,5),(6,5),(6,6))
I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
def edgecol(edge):
    i,j=edge;a=[F(0)]*21;a[i]=1;a[7+j]=1;a[14+j]=r[i];return Matrix(a)
CB=Matrix.hstack(*(edgecol(e) for e in SB))
A=CB[list(I),:]
assert A.det()==Rational(-299,1600)
b0=Matrix(rhs(p))
Ai=A.inv()
EB=Ai*b0[list(I),:]; DB=Ai*B8[list(I),:]
assert CB*EB==b0 and CB*DB==B8
def bound(M): return max(sum(abs(M[i,j]) for j in range(M.cols)) for i in range(M.rows))
assert min(EB)==Rational(23,4000000) and bound(DB)==Rational(535,52)
S=jac(both_slacks)*P;G=jac(deficits)*P
sl0=both_slacks(p)
assert [i for i,v in enumerate(sl0) if v==0]==[4,15,23]
assert all(all(S[i,k]==0 for k in range(8)) for i in (4,15,23))
assert min(v for v in sl0 if v>0)==Rational(7,2000000)
assert bound(S)==27 and bound(G)==Rational(17,2)
assert min(deficits(p))==Rational(654982477,81785400000)
T=Matrix([[B8[I[i],k]*(20 if I[i]>=14 else 1) for k in range(8)] for i in range(15)])
s=[sum(abs(T[i,k]) for k in range(8)) for i in range(15)]
assert max(s)==Rational(405,2)   # prior PR #1923 claimed 457/8
assert T[13,7]==-75
assert sum(v*v for v in s)==Rational(15396036457529,233280000)
assert sum(v*v for v in s)<260**2
D0=1148267016000000
U=D0*260*39**14
rho=Rational(1,10**40)
assert U<10**40
assert min(v for v in sl0 if v>0)>rho*bound(S)
assert min(EB)>rho*bound(DB)
assert min(deficits(p))>rho*bound(G)
# 10 mandatory-edge dual central bounds independently given in PR #1902/#1923
beta=Rational(18052765669,88328232000000)
delta_beta=Rational(585227,46800)
assert beta>rho*delta_beta
print("PASS physical rank 8; fixed 15-edge 21-row equations; lawful margins")
print("CORRECTED_SCALED_ROW_BOUND",max(s),"rather_than_457/8")
print("WITNESS_T[13,7]",T[13,7])
print("ROWSUM_SQUARED_NORM",sum(v*v for v in s),"< 67600")
print("CERTIFIED_U",U,"< 10^40")
print("CERTIFIED_8D_RADIUS",rho)
print("PASS new 8D all-real-point 15-edge certificate conditional on PR1902 center exclusions")



# NEW exact 5D quotient/separator certificate for sharp cube radius.
# All calculations below use exact SymPy Rationals/integers, no floating thresholds.
from itertools import combinations
from fractions import Fraction
from math import factorial

FSET=((0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6))
OTHER=tuple(e for e in D if e not in FSET)
assert len(D)==30 and len(OTHER)==20 and len(FSET)==10
C=Matrix.hstack(*(Matrix([edgecol(e)[i]*(20 if i>=14 else 1) for i in I]) for e in D))
FC=C[:,[D.index(e) for e in FSET]]
assert FC.rank()==10
L=Matrix.vstack(*(vec.T for vec in FC.T.nullspace()))
assert L.shape==(5,15) and L*FC==Matrix.zeros(5,10)
assert all(x.q==1 for x in L)  # the canonical SymPy nullspace basis is integral here
V=L*C[:,[D.index(e) for e in OTHER]]
hsc=Matrix([rhs(p)[i]*(20 if i>=14 else 1) for i in I])
q0=L*hsc
Q8=L*T
columns=[[int(V[i,j]) for i in range(5)] for j in range(20)]
unit=[[int(i==j) for i in range(5)] for j in range(5)]

def det4(rows):
    a=[list(map(int,row)) for row in rows]
    sign=1; old=1
    for k in range(3):
        if a[k][k]==0:
            pivot=next((i for i in range(k+1,4) if a[i][k]),None)
            if pivot is None:return 0
            a[k],a[pivot]=a[pivot],a[k];sign=-sign
        x=a[k][k]
        for i in range(k+1,4):
            for j in range(k+1,4):
                num=a[i][j]*x-a[i][k]*a[k][j]
                assert num%old==0
                a[i][j]=num//old
            a[i][k]=0
        old=x
    return sign*a[3][3]

def normal(vectors):
    assert len(vectors)==4
    return [(-1 if i%2 else 1)*det4([
        [vectors[k][j] for k in range(4)] for j in range(5) if j!=i
    ]) for i in range(5)]

def separator(vectors):
    w=normal(vectors)
    if any(w):return w
    for k in (3,2,1):
        for chosen in combinations(range(4),k):
            for axes in combinations(range(5),4-k):
                w=normal([vectors[i] for i in chosen]+[unit[j] for j in axes])
                if any(w) and sum(w[i]*q0[i] for i in range(5))!=0:
                    return w
    raise AssertionError("no separating witness")

PRIME=2**127-1
assert PRIME>factorial(14)*38**14
def rankmod(vecs):
    basis=[]
    for u in vecs:
        v=[x%PRIME for x in u]
        for pivot,b in basis:
            a=v[pivot]
            if a:v=[(v[i]-a*b[i])%PRIME for i in range(5)]
        pivot=next((i for i,x in enumerate(v) if x),None)
        if pivot is not None:
            inv=pow(v[pivot],-1,PRIME)
            basis.append((pivot,[(x*inv)%PRIME for x in v]))
    return len(basis)

ranks={}; minimum=None; witness=None
for subset in combinations(range(20),4):
    vecs=[columns[j] for j in subset]
    rk=rankmod(vecs)
    ranks[rk]=ranks.get(rk,0)+1
    w=separator(vecs)
    assert all(sum(w[i]*vec[i] for i in range(5))==0 for vec in vecs)
    numerator=abs(sum(w[i]*q0[i] for i in range(5)))
    assert numerator>0
    slope=sum(abs(sum(w[i]*Q8[i,k] for i in range(5))) for k in range(8))
    if slope:
        radius=numerator/slope
        if minimum is None or radius<minimum:
            minimum=radius
            witness=tuple(OTHER[j] for j in subset)
assert ranks=={4:3669,3:1143,2:33}
star=Rational(23,17050000)
assert minimum==star
print("PASS_4845_EXACT_COFAC_SEPARATORS",ranks)
print("EXACT_MIN_SUPPORT_SEPARATION_RADIUS",minimum,"witness",witness)

# Recheck ten original dual forcing certificates, for every point in the cube.
CERT={
 (0,0):{7:"1"},
 (0,1):{1:"-5/13",8:"15/13",15:"-20/13"},
 (0,2):{1:"-5/9",2:"-5/18",9:"10/9",16:"-10/9"},
 (2,2):{0:"-18/5",1:"-2",7:"18/5",8:"54/13",9:"4",15:"-72/13",16:"-4"},
 (3,3):{0:"-11/5",1:"1",2:"3",3:"5",4:"5",5:"5",6:"5",7:"11/5",8:"3",9:"3",12:"-5",13:"-5",15:"-8",16:"-8",17:"-4"},
 (4,3):{0:"-9/10",1:"3/2",2:"3",3:"4",4:"6",5:"6",6:"6",7:"9/10",8:"3/2",9:"3/2",12:"-6",13:"-6",15:"-6",16:"-6",17:"-4"},
 (4,5):{0:"2/5",1:"2",2:"3",3:"4",4:"5",5:"4",6:"4",7:"-2/5",12:"-4",13:"-4",15:"-4",16:"-4",17:"-4"},
 (5,5):{0:"2/5",1:"2",2:"3",3:"4",4:"5",5:"6",6:"5",7:"-2/5",12:"-5",13:"-5",15:"-4",16:"-4",17:"-4"},
 (6,5):{0:"2/13",1:"10/13",2:"15/13",3:"20/13",4:"25/13",5:"25/13",6:"38/13",7:"-2/13",12:"-25/13",13:"-38/13",15:"-20/13",16:"-20/13",17:"-20/13"},
 (6,6):{13:"1"}
}
values=[]
for e,sparse in CERT.items():
    y=Matrix([Rational(sparse.get(i,"0")) for i in range(21)])
    assert all((y.T*edgecol(f))[0]<=int(e==f) for f in D)
    beta=(y.T*Matrix(rhs(p)))[0]
    variation=y.T*B8
    denom=sum(abs(variation[k]) for k in range(8))
    assert beta>0
    if denom:values.append((beta/denom,e))
dual_radius=min(values)
assert dual_radius[0]==Rational(18052765669,423284426970000)
assert dual_radius[0]>star

# Exact physical / fixed-15-edge box margins, checking all 26 slacks and 15 weights.
slopes=lambda a:sum(abs(x) for x in a)
physical=min(sl0[i]/slopes(S[i,:]) for i in range(len(sl0))
             if sl0[i]>0 and slopes(S[i,:]))
coupling=min(EB[i]/slopes(DB[i,:]) for i in range(15) if slopes(DB[i,:]))
assert physical==coupling==star
print("PASS_SHARP_PHYSICAL_AND_15EDGE_RADII",physical,coupling)
print("PASS_DUAL_FORCING_RADIUS",dual_radius)

# Explicit real-box boundary point is legal and has exactly 14 positive coupling edges.
tb=Matrix([0,0,0,-star,star,0,0,-star])
pb=tuple(F(p[i])+sum(F(P[i,j]*tb[j]) for j in range(8)) for i in range(14))
Eb=EB+DB*tb
assert restrictions(pb)==(F(0),)*5
assert min(both_slacks(pb))>=0
assert CB*Eb==Matrix(rhs(pb))
assert min(Eb)==0 and sum(1 for v in Eb if v>0)==14
assert tuple(SB[i] for i in range(15) if Eb[i]==0)==((1,3),)
assert EB[SB.index((1,3))]==Rational(23,4000000)
assert list(DB[SB.index((1,3)),:])==[0,0,0,Rational(1,80),-1,0,0,Rational(13,4)]
print("PASS_SHARP_BOUNDARY_14EDGE_WITNESS",list(tb), "zeros", [(1,3)])
print("PROVED_UNIFORM_EXACT_15_FOR_ALL_8D_CUBES_WITH_RADIUS_LESS_THAN",star)
print("PROVED_MAXIMAL_UNIFORM_15_EDGE_CUBE_RADIUS_SUPREMUM",star)

# ---- New face-specific proof: pointwise exact-14 support on a 7D cube ----
H7=Matrix.zeros(8,7)
for col,j in enumerate((0,1,2,3,5,6,7)):
    H7[j,col]=1
H7[4,3]=Rational(1,80)
H7[4,6]=Rational(13,4)
assert H7.rank()==7
edge13=SB.index((1,3))
assert (DB[edge13,:]*H7)==Matrix.zeros(1,7)
assert EB[edge13]==Rational(23,4000000)
assert tuple(DB[edge13,k] for k in range(8)) == (
    0,0,0,Rational(1,80),-1,0,0,Rational(13,4))
qB=L*Matrix([rhs(pb)[i]*(20 if i>=14 else 1) for i in I])
Q7=Q8*H7
S7=jac(both_slacks)*P*H7
E7=DB*H7
sb=both_slacks(pb)
zero_slacks=tuple(i for i,v in enumerate(sb) if v==0)
assert zero_slacks==(4,15,19,23)
assert all(S7[i,k]==0 for i in zero_slacks for k in range(7))
assert sum(1 for v in Eb if v>0)==14
def margin(vals,derivatives):
    ratios=[]
    for i,v in enumerate(vals):
        denom=sum(abs(derivatives[i,k]) for k in range(7))
        if v>0 and denom: ratios.append((v/denom,i))
    return min(ratios)
physical_margin=margin(sb,S7)
coupling_margin=margin(Eb,E7)
assert physical_margin==(Rational(63,75872500),25)
assert coupling_margin==(Rational(50915668197609,1262603261375726875),12)
rank_counts={};covered=0;separation=None;min_triplet=None
for triple in combinations(range(20),3):
    M=V[:,list(triple)]
    rk=M.rank();rank_counts[rk]=rank_counts.get(rk,0)+1
    candidates=[w for w in M.T.nullspace() if (w.T*qB)[0]!=0]
    if not candidates: covered+=1
    for w in candidates:
        val=abs((w.T*qB)[0])
        slope=sum(abs((w.T*Q7[:,k])[0]) for k in range(7))
        if slope:
            radius=val/slope
            if separation is None or radius<separation:
                separation=radius;min_triplet=tuple(OTHER[j] for j in triple)
assert rank_counts=={3:1055,2:84,1:1} and covered==0
assert separation==Rational(49948501046391,841518836618948125)
epsilon=Rational(1,10000000)
assert epsilon<physical_margin[0] and epsilon<coupling_margin[0] and epsilon<separation
assert max(abs(tb[k])+epsilon*sum(abs(H7[k,j]) for j in range(7)) for k in range(8))<dual_radius[0]
print("PASS_7D_FACE_RANK",H7.rank(),"MU1_EQUALS_ZERO")
print("PASS_1140_ALL_13EDGE_SUPPORTS_EXCLUDED",rank_counts)
print("EXACT_13EDGE_SEPARATION_RADIUS",separation,min_triplet)
print("EXACT_PHYSICAL_MARGIN",physical_margin)
print("EXACT_14EDGE_MARGIN",coupling_margin)
print("PROVED_EVERY_REAL_POINT_7D_CUBE_EPS",epsilon,"MIN_SUPPORT_14")
