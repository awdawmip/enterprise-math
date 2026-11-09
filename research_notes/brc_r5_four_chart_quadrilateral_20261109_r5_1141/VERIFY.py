#!/usr/bin/env python3
"""Exact R5 four-chart 14-edge region and 16-edge coupling quadrilateral.
Standard library Fraction, exhaustive finite vertex enumeration, affine certificate.
"""
from fractions import Fraction as F
from itertools import combinations
def Q(s): return tuple(map(F,s.split()))
R=Q('1/10 1/2 3/4 1 5/4 3/2 19/10')
X0=Q('999/1000 1/6 999/1000 1/20 29/240 11/160 1/120')
X1=Q('1 1/10 1 27/800 1/100 27/400 1/100')
Y0=Q('871/1000 9/40 5/6 273/4000 21/100 143/1000 9/400')
Y1=Q('4673/6400 1311/6400 4673/6400 38759/512000 47301/256000 103999/512000 1311/64000')
SA=((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(5,2),(3,3),(1,5),(2,5),(4,5),(5,5),(6,5))
SB=((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(3,3),(0,5),(1,5),(3,5),(4,5),(5,5),(6,5))
U=tuple(sorted(set(SA)|set(SB)))
assert len(U)==16

def masses(f):
    g,a,b,u,v,w,z=f
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
        F(13,40)*a+b/80-u,(g-a)/2,
        1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
        (g-b)/2,F(3,40)*a+F(21,80)*b-w,
        u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(f):
    g,a,b,u,v,w,z=f
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)
def model(p):
    g,a,u,v,w,z,G,A,B=p
    x=(g,a,g,u,v,w,z);P,Q=times(x)
    U0=-F(17,40)*A-F(19,80)*B-G/2-P+F(3,2)*Q-F(1,2)
    W0=-F(7,40)*A-F(39,80)*B-G/2+P-Q/2-F(1,2)
    return x,(G,A,B,U0,A/10+F(9,40)*B,W0,A/10)
def slacks(f):
    g,a,b,u,v,w,z=f
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def operator(support):
    return ([[F(i==a) for a,b in support] for i in range(7)]+
            [[F(j==b) for a,b in support] for j in range(7)]+
            [[R[a] if j==b else F(0) for a,b in support] for j in range(7)])
def target(x,y):
    nu=masses(x);mu=masses(y)
    return tuple(mu+nu+tuple(R[i]*nu[i] for i in range(7)))
def solve(A,b):
    n=len(A[0]);M=[list(map(F,row))+[F(t)] for row,t in zip(A,b)]
    piv=0
    for k in range(n):
        j=next((i for i in range(piv,len(M)) if M[i][k]),None)
        assert j is not None,('rank',k)
        M[piv],M[j]=M[j],M[piv]
        d=M[piv][k];M[piv]=[v/d for v in M[piv]]
        for i in range(len(M)):
            if i!=piv and M[i][k]:
                c=M[i][k];M[i]=[v-c*w for v,w in zip(M[i],M[piv])]
        piv+=1
    assert all(all(v==0 for v in row[:n]) and row[-1]==0 for row in M[n:])
    sol=tuple(M[i][-1] for i in range(n))
    assert tuple(sum(row[j]*sol[j] for j in range(n)) for row in A)==tuple(b)
    return sol
def rank(A):
    M=[list(map(F,row)) for row in A];j=0
    for col in range(len(M[0])):
        p=next((i for i in range(j,len(M)) if M[i][col]),None)
        if p is None:continue
        M[j],M[p]=M[p],M[j];d=M[j][col];M[j]=[v/d for v in M[j]]
        for i in range(j+1,len(M)):
            if M[i][col]:
                c=M[i][col];M[i]=[v-c*w for v,w in zip(M[i],M[j])]
        j+=1
        if j==len(M):break
    return j
def det(A):
    M=[list(map(F,row)) for row in A];n=len(M);d=F(1)
    assert all(len(row)==n for row in M)
    for j in range(n):
        p=next((i for i in range(j,n) if M[i][j]),None)
        if p is None:return F(0)
        if j!=p:M[j],M[p]=M[p],M[j];d=-d
        v=M[j][j];d*=v
        for i in range(j+1,n):
            if M[i][j]:
                c=M[i][j]/v
                for k in range(j+1,n):M[i][k]-=c*M[j][k]
                M[i][j]=F(0)
    return d

xh=tuple((a+b)/2 for a,b in zip(X0,X1))
yh=tuple((a+b)/2 for a,b in zip(Y0,Y1))
p0=tuple(xh[i] for i in (0,1,3,4,5,6))+tuple(yh[i] for i in (0,1,2))
assert model(p0)==(xh,yh)
assert p0==Q('1999/2000 2/15 67/1600 157/2400 109/1600 11/1200 51237/64000 2751/12800 30019/38400')
AU=operator(U)
assert rank(AU)==14
k1={(0,2):-F(5,13),(0,5):F(5,13),(2,2):F(18,13),
    (2,5):-F(18,13),(3,2):-F(1),(3,5):F(1)}
k2={(0,2):-F(15,13),(0,5):F(15,13),(2,2):F(28,13),
    (2,5):-F(28,13),(5,2):-F(1),(5,5):F(1)}
K1=tuple(k1.get(edge,F(0)) for edge in U)
K2=tuple(k2.get(edge,F(0)) for edge in U)
assert all(sum(row[i]*K1[i] for i in range(16))==0 for row in AU)
assert all(sum(row[i]*K2[i] for i in range(16))==0 for row in AU)
assert K1[U.index((3,5))]==1 and K2[U.index((5,2))]==-1
b0=target(xh,yh)
w0=solve(operator(SA),b0)
reference=tuple(dict(zip(SA,w0)).get(e,F(0)) for e in U)
assert min(w0)>0
vertices={}
for i,j in combinations(range(16),2):
    a,b,c,d=K1[i],K2[i],K1[j],K2[j]
    delta=a*d-b*c
    if delta==0:continue
    s=(-reference[i]*d+b*reference[j])/delta
    t=(-a*reference[j]+c*reference[i])/delta
    e=tuple(reference[k]+s*K1[k]+t*K2[k] for k in range(16))
    if all(v>=0 for v in e):vertices[(s,t)]=e
assert len(vertices)==4
zero_sets={frozenset(U[i] for i,v in enumerate(e) if not v) for e in vertices.values()}
expected={frozenset(v) for v in (
    ((0,5),(3,5)),((3,5),(5,2)),((2,5),(5,2)),((0,5),(2,5)))}
assert zero_sets==expected
assert all(sum(v>0 for v in e)==14 for e in vertices.values())
print('PASS_EXACT_16_EDGE_RANK',rank(AU),'NULLITY',16-rank(AU))
for (s,t),e in sorted(vertices.items()):
    print('VERTEX',s,t,'POSITIVE',sum(v>0 for v in e),
          'ZERO_EDGES',str(tuple(U[i] for i,v in enumerate(e) if not v)))
print('PASS_EXHAUSTIVE_120_CANDIDATE_PAIRS_FOUR_VERTICES')
supports=tuple(tuple(edge for edge in U if edge not in zz)
               for zz in sorted(expected,key=lambda a:tuple(sorted(a))))
assert len(supports)==4
p_basis=[p0]
for j in range(9):
    q=list(p0);q[j]+=1;p_basis.append(tuple(q))
for p in p_basis:
    x,y=model(p)
    assert times(x)==times(y)
    assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    assert sum(masses(x))==sum(masses(y))==F(1)
    assert sum(r*m for r,m in zip(R,masses(x)))==sum(r*m for r,m in zip(R,masses(y)))==F(1)
values={}
for chart,s in enumerate(supports):
    A=operator(s);sol=[solve(A,target(*model(p))) for p in p_basis]
    assert all(v>0 for v in sol[0])
    values.update({('chart'+str(chart),edge):
                   (sol[0][i],tuple(sol[j+1][i]-sol[0][i] for j in range(9)))
                   for i,edge in enumerate(s)})
    print('PASS_14_EDGE_CHART',chart,'MISSING',
          str(tuple(e for e in U if e not in s)),'MIN_EDGE',min(sol[0]))
for side,idx in [('source',0),('target',1)]:
    ls=[slacks(model(p)[idx]) for p in p_basis]
    values.update({(side,i):
                   (ls[0][i],tuple(ls[j+1][i]-ls[0][i] for j in range(9)))
                   for i in range(13)})
ratios=[]
for name,(v,gradient) in values.items():
    L=sum(abs(z) for z in gradient)
    if v==0:assert L==0,('non-permanent zero',name)
    elif L>0:ratios.append((v/L,name,v,L))
    else:assert v>0
rho,name,v,L=min(ratios,key=lambda q:q[0])
assert rho==F(5194221,10938329600)
assert name==('chart2',(3,5))
assert v==F(1731407,691200000)
assert L==F(854557,162000)
assert rho>F(1,2500)
print('PASS_FULL_NINE_PARAMETER_COMMON_BOX_RADIUS',F(1,2500))
print('EXACT_SHARP_CENTRAL_SLACK_OVER_L1',rho,
      'LIMITING',name,'SLACK',v,'L1',L)
def phi(p):
    x,y=model(p)
    return masses(y)[:5]+masses(x)[:3]
phis=[phi(p) for p in p_basis]
cols=[tuple(phis[j+1][i]-phis[0][i] for i in range(8))
      for j in (0,1,2,3,4,6,7,8)]
d=det(tuple(zip(*cols)))
assert d==-F(1111424393,139968000000)
print('PASS_OBSERVER_EIGHT_DIMENSIONAL_MINOR',d)
print('THEOREM_FOUR_DISTINCT_14_EDGE_CHARTS_OVER_COMMON_9D_PHYSICAL_BOX')

# Stronger atlas theorem: quadrilateral combinatorics remain unchanged
# throughout the nine-dimensional closed physical box.
ref_basis=[]
for p in p_basis:
    sw=solve(operator(SA),target(*model(p)))
    ref_basis.append(tuple(dict(zip(SA,sw)).get(edge,F(0)) for edge in U))
def two_active_candidate(ref,i,j):
    a,b,c,d=K1[i],K2[i],K1[j],K2[j]
    denominator=a*d-b*c
    if denominator==0:return None
    s=(-ref[i]*d+b*ref[j])/denominator
    t=(-a*ref[j]+c*ref[i])/denominator
    return tuple(ref[k]+s*K1[k]+t*K2[k] for k in range(16))
valid=invalid=0
negative_radii=[]
for i,j in combinations(range(16),2):
    candidates=[two_active_candidate(v,i,j) for v in ref_basis]
    if candidates[0] is None:continue
    v0=candidates[0]
    if all(v>=0 for v in v0):
        assert frozenset(U[k] for k,z in enumerate(v0) if not z) in expected
        valid+=1
    else:
        negatives=[]
        for k,z in enumerate(v0):
            if z>=0:continue
            grad_l1=sum(abs(v[k]-z) for v in candidates[1:])
            if grad_l1==0:negatives.append(F(1000000))
            else:negatives.append(-z/grad_l1)
        witness_radius=max(negatives)
        assert witness_radius>F(1,2500),('unstable infeasible pair',U[i],U[j])
        negative_radii.append(witness_radius)
        invalid+=1
assert valid==4 and invalid==20
assert min(negative_radii)==F(5194221,10938329600)
print('PASS_STABLE_QUADRILATERAL_OVER_ALL_REAL_BOX','radius',F(1,2500),
      'four_valid_pairs',valid,'twenty_excluded_pairs',invalid,
      'minimal_infeasibility_radius',min(negative_radii))

# Global exact criterion on the fixed union, beyond the local 9D box.
# After solving on SA, nonnegativity of the 16-edge affine kernel slice
# reduces to nine one-variable linear inequalities and 8 fixed edge signs.
VARIABLE={(0,2),(0,5),(2,2),(2,5),(3,2),(3,5),(5,2),(5,5)}
assert len(VARIABLE)==8 and len(set(U)-VARIABLE)==8

def strip_certificate(p):
    particular=solve(operator(SA),target(*model(p)))
    ref=dict(zip(SA,particular))
    if any(ref[edge]<0 for edge in set(U)-VARIABLE):return None
    a,b,c,d,e,f=(ref[(0,2)],ref[(2,2)],ref[(3,2)],
                  ref[(2,5)],ref[(5,2)],ref[(5,5)])
    if c<0:return None
    # Each pair lower <= upper gives an affine half-line on s.
    lowers=((F(0),-f),(-F(1,3),F(0)),(-F(9,14),-F(13,28)*b))
    uppers=((F(0),e),(-F(1,3),F(13,15)*a),(-F(9,14),F(13,28)*d))
    s_low=F(0);s_high=c
    for low_slope,low_const in lowers:
        for up_slope,up_const in uppers:
            slope=low_slope-up_slope;rhs=up_const-low_const
            if slope>0:s_high=min(s_high,rhs/slope)
            elif slope<0:s_low=max(s_low,rhs/slope)
            elif rhs<0:return None
    if s_low>s_high:return None
    s=s_low
    t=max(slope*s+constant for slope,constant in lowers)
    assert t<=min(slope*s+constant for slope,constant in uppers)
    coupling={edge:ref.get(edge,F(0))+s*k1.get(edge,F(0))+
              t*k2.get(edge,F(0)) for edge in U}
    assert all(v>=0 for v in coupling.values())
    assert sum(v>0 for v in coupling.values())<=14
    assert all(sum(coupling[edge]*row[j] for j,edge in enumerate(U))==rhs
               for row,rhs in zip(AU,target(*model(p))))
    return s,t,coupling

center_cert=strip_certificate(p0)
assert center_cert is not None
p1=tuple(X1[i] for i in (0,1,3,4,5,6))+tuple(Y1[i] for i in (0,1,2))
ref1=dict(zip(SA,solve(operator(SA),target(*model(p1)))))
assert ref1[(5,5)]==-F(83405933,3456000000)
end_cert=strip_certificate(p1)
assert end_cert is not None
print('PASS_GLOBAL_16_EDGE_STRIP_CRITERION_AT_SEAM',
      'edges',sum(w>0 for w in center_cert[2].values()),'s',center_cert[0],'t',center_cert[1])
print('PASS_GLOBAL_16_EDGE_STRIP_CRITERION_OUTSIDE_BOX',
      'old_SA_negative',ref1[(5,5)],'edges',sum(w>0 for w in end_cert[2].values()),
      's',end_cert[0],'t',end_cert[1])
print('THEOREM_S_RESTRICTED_FEASIBILITY_REDUCES_TO_NINE_LINEAR_INEQUALITIES_IN_ONE_SCALAR_AND_14_EDGE_EXTRACTION')

# Exact physical witness outside the fixed S union: the four-chart atlas is not
# globally sufficient, even though the full 49-edge Blackwell problem is feasible.
# No floating point is used in this published certificate or validation.
p5=tuple(X0[i] for i in (0,1,3,4,5,6))+(F(1),F(2002911,10904720),F(26095487,40892700))
x5,y5=model(p5)
W13={
 (0,0):F(33553,432000),
 (0,1):F(3997,624000),
 (0,2):F(309035731,15310226880),
 (2,1):F(3997,390000),
 (2,2):F(283041195263,765511344000),
 (2,3):F(8294919533,294427440000),
 (3,3):F(4095218743,29442744000),
 (4,2):F(309035731,11777097600),
 (4,3):F(8294919533,294427440000),
 (4,5):F(172449787,1363090000),
 (5,5):F(219439,545236000),
 (6,5):F(172449787,2180944000),
 (6,6):F(38053,432000)
}
assert len(W13)==13 and all(t>0 for t in W13.values())
assert all(v>=0 for v in slacks(x5)+slacks(y5))
assert x5[0]==x5[2] and y5[6]==y5[1]/10
assert y5[4]-y5[6]==F(9,40)*y5[2]
assert times(x5)==times(y5)==(F(17609,6000),F(33857,12000))
assert all(sum(W13.get((i,j),F(0)) for j in range(7))==masses(y5)[i] for i in range(7))
assert all(sum(W13.get((i,j),F(0)) for i in range(7))==masses(x5)[j] for j in range(7))
assert all(sum(R[i]*W13.get((i,j),F(0)) for i in range(7))==R[j]*masses(x5)[j] for j in range(7))
assert sum(W13.values())==1
# Every coupling supported in S has E[3,3]=M_3(x) (source-column 3
# has no other edge). Its target row 3 then needs M_3(y)>=M_3(x).
obstruction=masses(y5)[3]-masses(x5)[3]
assert obstruction==-F(8294919533,147213720000)<0
assert strip_certificate(p5) is None
print('PASS_EXACT_NON_S_PHYSICAL_13_EDGE_BLACKWELL_CERTIFICATE',
      'min_edge',min(W13.values()),'P',times(x5)[0],'Q',times(x5)[1])
print('PASS_S_RESTRICTED_NO_GO_VIA_ROW3_SOURCE3',
      'M3_target_minus_M3_source',obstruction)
print('COUNTEREXAMPLE_FOUR_CHART_S_ATLAS_NOT_GLOBAL_FOR_PHYSICALLY_LAWFUL_PAIRS')

# Exact finite obstruction to extending this 13-edge witness support into a
# full-dimensional 9-parameter affine 14-edge chart by adding just one edge.
base13=tuple(W13)
assert rank(operator(base13))==13
B=[target(*model(p)) for p in p_basis]
assert rank([list(r) for r in zip(*B)])==9
support_extensions={}
for extra in ((i,j) for i in range(7) for j in range(7)):
    if extra in W13:continue
    A14=operator(base13+(extra,))
    m=rank(A14)
    augmented=[row+[b[i] for b in B] for i,row in enumerate(A14)]
    mr=rank(augmented)
    support_extensions[(m,mr)]=support_extensions.get((m,mr),0)+1
assert support_extensions=={(13,15):4,(14,15):13,(14,16):19}
print('PASS_EXACT_36_POSSIBLE_ONE_EDGE_EXTENSIONS_INSUFFICIENT_FOR_FULL_9D_CHART',
      'rank_counts',sorted(support_extensions.items()))
print('SCOPED_NO_GO_AUGMENTING_THIS_SPECIFIC_13_EDGE_SUPPORT_BY_ONLY_ONE_EDGE_FOR_A_9D_OPEN_CHART')
