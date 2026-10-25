#!/usr/bin/env python3
"""C271 self-contained author exact checker: all 595 C254 two-box hulls.
Only standard-library Fraction. The C195/H168 auxiliary, NOT native GF(2)-BRC.
"""
from fractions import Fraction as F
NUM=(0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 3, 3, 1, 6, 2, 3, 6, 1, 6, 3, 2, 7, 3, 4, 8, 1, 21, 9, 6, 4, 10, 14, 5, 11, 2, 9, 12, 13, 14, 3, 7, 15, 17, 14, 5, 6, 13, 15, 17, 10, 11, 13, 16, 18, 22, 28, 36, 46, 63, 96, 152, 246, 528, 1971, 1)
DEN=(1, 2057, 539, 289, 136, 93, 68, 51, 39, 31, 27, 21, 17, 15, 13, 11, 10, 9, 8, 7, 13, 6, 11, 5, 14, 13, 4, 23, 7, 10, 19, 3, 17, 8, 5, 17, 7, 9, 17, 2, 41, 17, 11, 7, 17, 23, 8, 17, 3, 13, 17, 18, 19, 4, 9, 19, 21, 17, 6, 7, 15, 17, 19, 11, 12, 14, 17, 19, 23, 29, 37, 47, 64, 97, 153, 247, 529, 1972, 1)
BOX_DATA="4/543,43/62,4/5,9/11,9/613,57/79,38/47,121/147;3/407,5/7,60/77,4/5,7/477,18/25,53/67,9/11;3/407,5/7,18/23,4/5,6/409,31/43,87/109,4/5;3/407,5/7,4/5,81/101,7/477,31/43,21/26,76/93;2/271,7/10,60/77,4/5,6/409,42/59,11/14,4/5;2/271,7/10,4/5,13/16,6/409,27/38,4/5,58/71;2/271,12/17,26/33,4/5,3/233,12/17,59/74,4/5;1/135,16/23,18/23,9/11,3/205,5/7,4/5,9/11;1/135,7/10,26/33,4/5,3/283,7/10,27/34,4/5;1/135,7/10,4/5,49/61,2/137,7/10,4/5,31/38;1/135,12/17,4/5,57/71,3/205,12/17,4/5,30/37;1/127,16/23,18/23,4/5,1/106,16/23,4/5,13/16;3/371,7/10,15/19,4/5,2/171,17/24,53/67,4/5;1/123,34/49,15/19,4/5,1/69,7/10,59/74,4/5;1/123,26/37,48/61,4/5,1/78,27/38,15/19,4/5;1/119,19/27,4/5,17/21,3/205,12/17,4/5,69/85;1/119,12/17,18/23,13/16,3/205,12/17,11/14,9/11;1/119,12/17,15/19,13/16,1/74,12/17,15/19,22/27;1/119,5/7,60/77,19/24,1/69,28/39,34/43,41/51;1/119,5/7,18/23,17/21,3/205,5/7,59/74,9/11;1/117,19/27,4/5,21/26,1/85,22/31,4/5,17/21;1/105,7/10,53/68,9/11,3/205,18/25,53/67,23/28;1/105,12/17,4/5,13/16,1/74,42/59,21/26,9/11;1/104,34/49,18/23,4/5,1/69,7/10,34/43,4/5;1/104,34/49,4/5,41/51,1/69,30/43,4/5,22/27;1/103,7/10,27/34,4/5,2/155,22/31,87/109,4/5;1/103,12/17,18/23,21/26,1/86,12/17,18/23,13/16;2/189,7/10,32/41,4/5,3/205,19/27,37/47,4/5;1/93,16/23,18/23,13/16,2/137,7/10,15/19,9/11;1/93,12/17,18/23,19/24,6/409,27/38,15/19,4/5;1/93,12/17,18/23,21/26,1/69,12/17,11/14,17/21;1/93,12/17,19/24,13/16,1/69,12/17,27/34,13/16;1/89,12/17,15/19,21/26,1/69,12/17,15/19,13/16;1/88,12/17,26/33,4/5,3/232,29/41,72/91,4/5;1/77,7/10,26/33,4/5,6/409,12/17,63/79,4/5"
U=tuple(F(a,b) for a,b in zip(NUM,DEN))
Q=2**128; H=2**166; A=F(6912*50000**2,17**2)
Z=F(141421356237309504880,10**20)
I=(5,50,55,56)
J=tuple(k for k in range(79) if k not in I)
assert len(U)==79 and all(U[k]<U[k+1] for k in range(78))
assert U[54]==F(7,9) and U[55]==F(15,19) and U[56]==F(17,21)
assert U[56]-U[54] == F(2,63) < Z-U[56]
D=[]
for item in BOX_DATA.split(';'):
    z=tuple(map(F,item.split(',')))
    assert len(z)==8
    l,h=z[:4],z[4:]
    assert all(U[p-1]<l[d]<=h[d]<U[p+1] for d,p in enumerate(I))
    assert l[2]<l[3] and h[2]<h[3]
    D.append((l,h))
assert len(D)==35
basic_delta=[h[2]-l[3] for l,h in D]
assert [k for k,g in enumerate(basic_delta) if g>0]==[3]
assert [k for k,g in enumerate(basic_delta) if g==0]==[11]
assert basic_delta[3]==F(15,2626)


# C274 addendum: global collision collar, exact 128-interval proof.
# Author research only; no Source claim and no native BRC/X6 transfer.
from itertools import combinations
import json

A_MIN=min(lo[0] for lo,hi in D)
B_MIN=min(lo[1] for lo,hi in D)
EPS_MAX=F(1,3077)
assert A_MIN==F(4,543) and B_MIN==F(43,62)
assert U[54]==F(7,9) and U[55]==F(15,19) and U[56]==F(17,21)
assert 54 in J and 55 not in J and 56 not in J
assert Z+U[54]-2*U[56]>0
assert all(A_MIN<=lo[0]<=hi[0]<U[55] and
           B_MIN<=lo[1]<=hi[1]<U[55] for lo,hi in D)



# C275 author-exact extension to the pinned C271/C274 input.
# No native X6/BRC correspondence, task CLAIM, or independent review is claimed.
from fractions import Fraction as F
from itertools import combinations
import json
P = [
    (F(1,93),F(12,17),F(27,34),F(101,125)),
    (F(1,100),F(703,1000),F(27,34),F(101,125)),
]
EPS=F(1,10000)
def admissible(v):
    return all(U[k-1]<v[i]<U[k+1] for i,k in enumerate(I)) and v[0]<v[1]<v[2]<v[3]<Z
def active(k,v):
    x=v[I.index(k)]
    out=F(Q)*A/H/((2-x*x)*(3-x*x))**3
    for j in J:out*=(Z-U[j])/abs(x-U[j])
    for h,y in zip(I,v):
        if h!=k:out*=(Z-y)/abs(x-y)
    return out
def fixed_data():
    exact,unfloored={},{}
    for j in J:
        u=U[j]
        mass=F(Q)*A/H/((2-u*u)*(3-u*u))**3
        for r in range(len(U)):
            if r!=j:mass*=(Z-U[r])/abs(u-U[r])
        assert mass>1
        unfloored[j]=mass
        exact[j]=mass.numerator//mass.denominator
    assert all(exact[j]>0 for j in J)
    return exact,unfloored
def multiplier(j,v):
    f=F(1)
    for k,p in zip(I,v):
        f*=(Z-p)/(Z-U[k])*abs(U[j]-U[k])/abs(U[j]-p)
    return f
def direct(v,weights):
    return sum((weights[j]*multiplier(j,v) for j in J),F(0))+sum((active(k,v) for k in I),F(0))
def independent_unfloored(v):
    # Cancel original active-node factors before computing the fixed branches.
    total=F(0)
    for j in J:
        u=U[j]
        term=F(Q)*A/H/((2-u*u)*(3-u*u))**3
        for r in J:
            if r!=j:term*=(Z-U[r])/abs(u-U[r])
        for p in v:term*=(Z-p)/abs(u-p)
        total+=term
    for k in I:total+=active(k,v)
    return total
def classify():
    out={}
    for i,j in combinations(range(35),2):
        lo=tuple(min(D[i][0][k],D[j][0][k]) for k in range(4))
        hi=tuple(max(D[i][1][k],D[j][1][k]) for k in range(4))
        gap=hi[2]-lo[3]
        out[(i,j)]=(lo,hi,'safe' if gap<0 else 'touch' if gap==0 else 'cross')
    return out
def inside(v,lo,hi):
    return all(lo[k]<=v[k]<=hi[k] for k in range(4))
def positive_point(lo,hi):
    a=(lo[0]+hi[0])/2;b=(lo[1]+hi[1])/2;t=(hi[2]+lo[3])/2
    return(a,b,t-EPS/2,t+EPS/2)
def certify():
    original,continuous=fixed_data()
    vals=[]
    for v in P:
        assert admissible(v) and U[55]<v[2]<v[3]<U[56]
        exact=direct(v,original)
        upper=direct(v,continuous)
        assert upper==independent_unfloored(v)
        assert 0<exact<=upper and 1000*upper<999*Q
        vals.append((exact,upper))
    h=classify()
    assert len(h)==595
    assert [sum(q[2]==name for q in h.values()) for name in ['safe','touch','cross']]==[363,124,108]
    covered=[]; remaining=[]; count_by_witness=[{'touch':0,'cross':0},{'touch':0,'cross':0}]
    high_count=0; min_mass=None;min_mass_pair=None
    for pair,(lo,hi,kind) in h.items():
        if kind=='safe':continue
        z=positive_point(lo,hi)
        assert admissible(z) and inside(z,lo,hi)
        assert U[55]<z[2]<z[3]<U[56]
        mass=active(55,z)+active(56,z)
        assert mass>3*Q
        high_count+=1
        if min_mass is None or mass<min_mass:min_mass=mass;min_mass_pair=pair
        ids=[i for i,w in enumerate(P) if inside(w,lo,hi)]
        for i in ids:count_by_witness[i][kind]+=1
        if ids:covered.append((pair,kind,ids))
        else:remaining.append((pair,kind))
    assert high_count==232
    assert len(covered)==187 and len(remaining)==45
    assert [sum(x[1]==k for x in covered) for k in ['touch','cross']]==[111,76]
    assert [sum(x[1]==k for x in remaining) for k in ['touch','cross']]==[13,32]
    assert count_by_witness==[{'touch':108,'cross':76},{'touch':96,'cross':52}]
    # The threshold equality follows by IVT on the straight segment joining
    # a negative rational witness and each corresponding positive rational one:
    # all box inequalities and strict order inequalities are convex.
    result={
      'status':'C275_AUTHOR_EXACT_MIXED_SIGN_HULLS_PASS',
      'original_nodes':79,'original_basic_boxes':35,
      'total_hulls':595,'safe':363,'touch':124,'cross':108,
      'collision_hulls_with_positive_witness':high_count,
      'positive_epsilon':str(EPS),
      'positive_bound':'M55+M56>3*2^128',
      'positive_min_ratio_exact':str(min_mass/Q),
      'positive_min_hull':list(min_mass_pair),
      'negative_witnesses':[{'coordinates':[str(t) for t in P[i]],
         'F_over_Q_exact':str(vals[i][0]/Q),
         'unfloored_upper_over_Q_exact':str(vals[i][1]/Q),
         'upper_bound':'F<999/1000*2^128',
         'hull_counts':count_by_witness[i]} for i in range(2)],
      'mixed_hulls_count':187,'mixed_touch':111,'mixed_cross':76,
      'mixed_hull_ids':[list(x[0]) for x in covered],
      'remaining_count':45,'remaining_touch':13,'remaining_cross':32,
      'remaining_hull_ids':[list(x[0]) for x in remaining],
      'formal_Source_claim':False,'independent_Driver_admission':False,
      'native_GF2_BRC_X6_transfer':False
    }
    return result
if __name__=='__main__':
    report=certify()
    print('C275_EXACT_PASS mixed=187 touch=111 cross=76 remaining=45 positive=232')
    print(json.dumps(report,ensure_ascii=False,indent=2))

# C289 reader compatibility aliases only. No change in mathematical content.
# C275 original names -> C284-C289 source interface names.
valid = admissible
moving_mass = active
floor_fixed_masses = fixed_data
fixed_multiplier = multiplier
original_F = direct
hulls = classify
high_point = positive_point
WITNESSES = P
