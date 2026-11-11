#!/usr/bin/env python3
"""R5 exact: open two-simplex of endpoints requiring three six-arc atoms."""
from fractions import Fraction as F
from itertools import combinations
R=(2,10,15,20,25,30,38)
PORTS=(1,2,3,5)
V=tuple((i,j) for j in PORTS for i in range(7))
IX={pair:k for k,pair in enumerate(V)}
A=[[int(i==k) for i,j in V] for k in range(7)]
A += [[int(j==p) for i,j in V] for p in PORTS]
A += [[R[i]*int(j==p) for i,j in V] for p in PORTS]
C=tuple(map(F,('10022571/135903376,74268405/475661816,0,0,0,0,10022571/475661816,'
 '0,122039541/1902647264,196521/67951688,0,0,0,26530335/1902647264,'
 '0,0,11485487/67951688,377644447/2548188300,5499155/67951688,0,831435/33975844,'
 '0,6092151/1902647264,0,0,680265/67951688,2161731/33975844,27135015/1902647264').split(',')))
b=tuple(sum((row[k]*C[k] for k in range(28)),F(0)) for row in A)
def step(x,j,row,t):
    h=[F(0)]*28
    for i,v in row.items():
        h[IX[(i,3)]]=F(v)
        h[IX[(i,j)]]=-F(v)
    assert all(sum(a*v for a,v in zip(ar,h))==0 for ar in A)
    y=tuple(a+t*v for a,v in zip(x,h))
    assert min(y)>=0
    assert all(sum((ar[k]*y[k] for k in range(28)),F(0))==bk for ar,bk in zip(A,b))
    return y
def mask(x):return tuple(i for i in range(7) if x[IX[(i,3)]]>0)
def avg(xs):return tuple(sum((x[k] for x in xs),F(0))/len(xs) for k in range(28))
assert mask(C)==(2,3,4,6)
C1=step(C,5,{2:-13,4:23,6:-10},F(1,10000))
piv=(16,1,17,18,0,8,26,27,5,20,13,22,2)
allowed=[k for k,(i,j) in enumerate(V) if j!=3 or i in (2,3,4,6)]
free=[k for k in allowed if k not in piv]
T=F(1,800)
aug=[[F(A[r][k]) for k in piv]+[b[r]-T*sum(A[r][k] for k in free)] for r in range(15)]
for col in range(13):
    pivot=next(r for r in range(col,15) if aug[r][col])
    aug[col],aug[pivot]=aug[pivot],aug[col]
    v=aug[col][col]
    aug[col]=[a/v for a in aug[col]]
    for r in range(15):
        if r!=col:
            v=aug[r][col]
            if v:aug[r]=[a-v*c for a,c in zip(aug[r],aug[col])]
assert all(not any(row[:13]) and row[-1]==0 for row in aug[13:])
w=[F(0)]*28
for k in free:w[k]=T
for i,p in enumerate(piv):w[p]=aug[i][-1]
assert all(w[k]>0 for k in allowed)
Z=tuple(F(999,1000)*x+F(1,1000)*y for x,y in zip(C1,w))
assert all(Z[k]>0 for k in allowed)
assert mask(Z)==(2,3,4,6)
c=Z[IX[(6,3)]]
end=[]
for m in (2,3,4):
    t=c/F(30-R[m])
    y=step(Z,5,{m:-8,5:38-R[m],6:R[m]-30},t)
    assert mask(y)==(2,3,4,5)
    allow_B=[k for k,(i,j) in enumerate(V) if j!=3 or i in (2,3,4,5)]
    assert all(y[k]>0 for k in allow_B)
    end.append(y)
M=avg(end)
assert mask(M)==(2,3,4,5)
x=Z
for m in (2,3,4):
    x=step(x,5,{m:-8,5:38-R[m],6:R[m]-30},c/F(3*(30-R[m])))
    assert len(mask(x))<=5
assert x==M
D=tuple((M[IX[(i,3)]]-Z[IX[(i,3)]])/c for i in range(7))
assert D==tuple(map(F,('0','0','-8/45','-4/15','-8/15','89/45','-1')))
print('EXACT_DELTA_OVER_C',*[str(v) for v in D])
print('EXACT_SOURCE3_INITIAL_MASK',mask(Z))
print('EXACT_SOURCE3_TERMINAL_MASK',mask(M))
# Two triple-supported atoms covering five nonzero source-3 targets must
# intersect at one target. Their two unique labels satisfy a moment cut.
S=(2,3,4,5,6);d={i:45*D[i] for i in S}
assert all(d[i].denominator==1 and d[i]!=0 for i in S)
values=[]
for r in S:
    for p,q in combinations((i for i in S if i!=r),2):
        v=int(d[p]*(R[p]-R[r])+d[q]*(R[q]-R[r]))
        assert v!=0
        values.append((r,p,q,v))
assert len(values)==30
print('TWO_ATOM_PAIR_CUT_COUNT',len(values),
      'MIN_ABS_INTEGER_CUT',min(abs(v) for *_,v in values))
# All 30 cuts are affine in barycentric lambda. Certify a uniform relative
# open neighborhood by |delta L| <= norm_inf(delta lambda)*sum|coefficients|.
unit={}
for m in (2,3,4):
    d0={i:F(0) for i in S}
    d0[m]=-F(8,30-R[m]);d0[5]=F(38-R[m],30-R[m]);d0[6]=-F(1)
    unit[m]=d0
radii=[]
for r,p,q,v in values:
    coef=[unit[m][p]*(R[p]-R[r])+unit[m][q]*(R[q]-R[r]) for m in (2,3,4)]
    bary=sum(coef,F(0))/3
    assert bary==F(v,45)
    bound=sum(map(abs,coef),F(0))
    radii.append(abs(bary)/bound)
assert min(radii)==F(1,6)
print('MAX_UNIFORM_PAIR_CUT_CERT_RADIUS_INF',str(min(radii)))
print('RATIONAL_BARYCENTRIC_ENDPOINT_MIN_ATOMS',3)
print('PASS_R5_EXACT_OPEN_2_SIMPLEX_GENERIC_THREE_ATOM_END_POINT_RIGIDITY')


# Exact complete distance stratification on the full closed barycentric triangle.
# A cut can vanish at a strictly positive lambda iff its 3 coefficients have
# opposite signs, since all three weights are positive and sum to one.
interior_cuts=[]
for r,p,q,v in values:
    a=tuple(unit[m][p]*(R[p]-R[r])+unit[m][q]*(R[q]-R[r]) for m in (2,3,4))
    assert any(a)
    if min(a)<0<max(a):interior_cuts.append((r,p,q,a))
assert interior_cuts==[
    (3,2,4,(F(8,3),F(0),F(-8))),
    (3,5,6,(F(-8,3),F(0),F(8)))
]
# Their shared zero line is lambda_2=3*lambda_4; on it, the endpoint
# decomposes into the single exit Z -> Y_3 followed by one 234 atom.
P=step(Z,5,{3:-4,5:9,6:-5},c/F(5))
assert P==end[1] and mask(P)==(2,3,4,5)
allowed_B=[k for k,(i,j) in enumerate(V) if j!=3 or i in (2,3,4,5)]
assert all(P[k]>0 for k in allowed_B)
# Both sides depend affinely on t. Check t=0 and t=1/4 exactly, thereby
# certifying equality for every rational/real 0 <= t <= 1/4.
for t in (F(0),F(1,4)):
    weighted=tuple(3*t*end[0][k]+(1-4*t)*end[1][k]+t*end[2][k] for k in range(28))
    via_two=step(P,5,{2:-1,3:2,4:-1},F(8,5)*c*t)
    assert weighted==via_two
# Every interior t keeps the terminal B-face state strictly positive;
# the segment Y_3 -> Y(lambda) is nonnegative by convexity.
for t in (F(1,1000),F(1,20),F(1,8),F(249,1000)):
    weighted=tuple(3*t*end[0][k]+(1-4*t)*end[1][k]+t*end[2][k] for k in range(28))
    via_two=step(P,5,{2:-1,3:2,4:-1},F(8,5)*c*t)
    assert via_two==weighted and mask(via_two)==(2,3,4,5)
print('STRICT_INTERIOR_ZERO_CUTS',[(r,p,q) for r,p,q,_ in interior_cuts])
print('EXCEPTIONAL_TWO_ATOM_LINE','lambda2=3*lambda4','0<lambda4<1/4')
print('EXCEPTIONAL_TWO_ATOM_FIRST_STATE_B_INTERIOR',all(P[k]>0 for k in allowed_B))
print('EXACT_ATOMIC_DISTANCE_STRATA','vertices=1;open_edges=2;interior_exceptional_line=2;other_interior=3')
print('PASS_R5_EXACT_COMPLETE_C_TO_B_SIMPLEX_DISTANCE_STRATIFICATION')


# R5 hidden-fiber continuation: exact legal distance 15 despite an unchanged
# complete source-3 row. The initial Z and B-interior endpoint end[1] above
# are reused at their original frozen science revision.
from math import factorial
base=tuple((x+y)/2 for x,y in zip(Z,end[1]))
h0={0:23,2:-36,6:13}
h1={1:23,2:-28,6:5}
pos_min=min(z for z in base if z>0)
tau=pos_min/F(3700)
X=step(step(base,5,h0,tau),5,h1,tau)
assert all(z>0 for z in X)

# Port-local K (sum w=sum Rw=0) has coordinates w[1:6]. Use a
# rational 5-element triple-vector basis on targets (0,i,6).
cs={1:(12,8,1,13,8),2:(3,13,7,4,2),5:(-15,-21,-8,-17,-10)}
assert all(sum(cs[j][i] for j in (1,2,5))==0 for i in range(5))
def atom(j,one):
    row={0:R[one]-R[6],one:R[6]-R[0],6:R[0]-R[one]}
    h=[F(0)]*28
    for i,v in row.items():
        h[IX[(i,3)]]=F(v)
        h[IX[(i,j)]]=-F(v)
    assert all(sum(a*v for a,v in zip(ar,h))==0 for ar in A)
    return tuple(h)
moves=[]
for j in (1,2,5):
    for i,c_i in enumerate(cs[j],1):
        moves.append((j,i,-F(c_i,36),atom(j,i)))
assert len(moves)==15
budget=max(sum(abs(t*h[k]) for _,_,t,h in moves) for k in range(28))
eps=min(X)/(2*budget)
states=[X]
for j,i,t,h in moves:
    y=tuple(v+eps*t*w for v,w in zip(states[-1],h))
    assert min(y)>=min(X)/2
    assert all(sum((ar[k]*y[k] for k in range(28)),F(0))==rhs
               for ar,rhs in zip(A,b))
    states.append(y)
Y=states[-1]
assert Y!=X
assert all(z>0 for z in Y)
assert all(Y[IX[(i,3)]]==X[IX[(i,3)]] for i in range(7))
for j in (1,2,5):
    assert tuple((Y[IX[(i,j)]]-X[IX[(i,j)]])/eps for i in range(1,6))==cs[j]

# Exhaustive rank-four dictionary normals over a large exact prime.
# Integer 4x4 minors obey 4! * 36^4 < PRIME; hence rank-four modular
# detection exactly matches rational rank-four detection.
PRIME=2147483647
assert factorial(4)*36**4<PRIME
directions=[]
for aa,bb,cc in combinations(range(7),3):
    v=[0]*7
    v[aa]=R[bb]-R[cc]
    v[bb]=R[cc]-R[aa]
    v[cc]=R[aa]-R[bb]
    assert sum(v)==0 and sum(R[i]*v[i] for i in range(7))==0
    directions.append(tuple(v[1:6]))
assert len(directions)==35
def normal_mod(rows):
    mat=[[z%PRIME for z in row] for row in rows]
    piv=[]
    for col in range(5):
        ip=next((k for k in range(len(piv),4) if mat[k][col]),None)
        if ip is None: continue
        rr=len(piv)
        mat[ip],mat[rr]=mat[rr],mat[ip]
        inv=pow(mat[rr][col],-1,PRIME)
        mat[rr]=[(z*inv)%PRIME for z in mat[rr]]
        for k in range(4):
            if k!=rr and mat[k][col]:
                t=mat[k][col]
                mat[k]=[(z-t*w)%PRIME for z,w in zip(mat[k],mat[rr])]
        piv.append(col)
        if len(piv)==4: break
    if len(piv)<4: return None
    free=next(k for k in range(5) if k not in piv)
    normal=[0]*5
    normal[free]=1
    for k,col in enumerate(piv):
        normal[col]=(-mat[k][free])%PRIME
    return tuple(normal)
normals=set()
rank4=ranklower=0
for group in combinations(directions,4):
    n=normal_mod(group)
    if n is None:ranklower+=1
    else:normals.add(n);rank4+=1
assert rank4==46198 and ranklower==6162 and len(normals)==3468
for j,cj in cs.items():
    assert all(sum(n[k]*cj[k] for k in range(5))%PRIME for n in normals), j

print('SOURCE3_SAME_ALL_SEVEN_TARGETS',True)
print('EXACT_POSITIVE_FULL_INTERIOR_BASE',all(z>0 for z in X))
print('EXACT_ALL_16_STATES_POSITIVE',all(min(x)>0 for x in states))
print('FOUR_DIRECTION_SETS',rank4+ranklower)
print('RANK4_SETS',rank4,'RANK_LT4_SETS',ranklower)
print('DISTINCT_RANK4_HYPERPLANE_NORMALS',len(normals))
print('PRIME',PRIME,'FOUR_MINOR_ABS_BOUND',factorial(4)*36**4)
print('PORT_COORDINATES',cs)
print('EPSILON',eps)
print('MIN_INITIAL_MASS',min(X))
print('MIN_INTERMEDIATE_MASS',min(min(x) for x in states))
print('EXACT_LEGAL_ATOMIC_DISTANCE',15)
print('PASS_R5_EXACT_HIDDEN_FIBER_SHARP_FIFTEEN_ATOMS')
