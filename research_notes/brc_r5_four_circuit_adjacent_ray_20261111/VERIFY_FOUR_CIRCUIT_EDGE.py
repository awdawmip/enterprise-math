#!/usr/bin/env python3
"""Exact two-pivot 14 -> 15 -> 15 vertices and a length-three tangent ray.
Frozen R5 scientific inputs: GK a01383f825ef9d43b4b754254303298c64041568;
EM 86149263e38c22292c9def1e0f69092efa1be77e.
All matrices and arithmetic are exact SymPy rationals.
"""
from sympy import Matrix, Rational as Q

R = (2, 10, 15, 20, 25, 30, 38)
r = [Q(z, 20) for z in R]
D = [(i,j) for j in (0,1,2,3,5,6) for i in range(7)
     if j not in (0,6) or i == j]
C = Matrix.hstack(*(Matrix([int(i==k) for k in range(7)]
       + [int(j==k) for k in range(7)]
       + [r[i] if j==k else 0 for k in range(7)]) for i,j in D))
M = {
(0,0):'219346331/10192753200',(0,1):'18669495/951323632',
(1,1):'1898238/8493961',(5,1):'3733899/475661816',
(2,2):'196521/2426846',(0,3):'8057361/237830908',
(2,3):'1544855/16987922',(3,3):'377644447/2548188300',
(4,3):'1544855/16987922',(5,3):'26530335/475661816',
(6,3):'196521/67951688',(0,5):'196521/9707384',
(6,5):'1375647/19414768',(6,6):'451274777/3397584400'
}
x = Matrix([Q(M[a]) if a in M else Q(0) for a in D])
assert C.rank()==15

def supp(v):
    return [i for i,z in enumerate(v) if z>0]

def pivot_at(v,insert_arcs,weights):
    p=supp(v)
    z=[i for i,q in enumerate(v) if q==0]
    pi=list(C[:,p].T.rref()[1])
    assert len(pi)==len(p)
    insert=[D.index(e) for e in insert_arcs]
    assert all(i in z for i in insert)
    old=-C[pi,p].inv()*sum((C[pi,idx]*w for idx,w in zip(insert,weights)),
                            Matrix.zeros(len(p),1))
    d=Matrix.zeros(30,1)
    for idx,w in zip(insert,weights):d[idx]=w
    for idx,w in zip(p,old):d[idx]=w
    assert C*d==Matrix.zeros(21,1)
    assert all(d[k]>=0 for k in z)
    t=min(v[k]/(-d[k]) for k in p if d[k]<0)
    out=v+t*d
    assert min(out)>=0 and C*out==C*v
    assert C[:,supp(out)].rank()==len(supp(out))
    return out,d,t

def H(j,k,a,b,c):
    vec=Matrix.zeros(30,1)
    for i,w in ((a,r[b]-r[c]),(b,r[c]-r[a]),(c,r[a]-r[b])):
        vec[D.index((i,j))]=w
        vec[D.index((i,k))]=-w
    assert C*vec==Matrix.zeros(21,1)
    assert sum(1 if w else 0 for w in vec)==6
    return vec

assert C[:,supp(x)].rank()==len(supp(x))==14
V,d1,t1=pivot_at(x,[(1,2),(4,2)],[Q(1,2),Q(1,4)])
assert len(supp(V))==15
W,d,t2=pivot_at(V,[(3,5)],[Q(1)])
assert len(supp(W))==15
assert sum(1 if u else 0 for u in d)==14
cert=-Q(1,2)*H(1,3,0,1,5)-Q(7,5)*H(2,3,1,2,4)-Q(5,9)*H(3,5,0,3,6)
assert d==cert
union=sorted(set(supp(V))|set(supp(W)))
assert len(union)==16 and C[:,union].rank()==15
assert len(union)-C[:,union].rank()==1
# Any sum of two six-support circuits has support <= 12.
assert sum(1 if u else 0 for u in d)>12
print('OBSERVER_RANK',C.rank())
print('START_VERTEX_SUPPORT',len(supp(x)),'START_RANK',C[:,supp(x)].rank())
print('FIRST_INSERTED_ARCS',[(1,2),(4,2)],'WEIGHTS',(Q(1,2),Q(1,4)),'STEP',t1)
print('INTERMEDIATE_VERTEX_SUPPORT',len(supp(V)),'RANK',C[:,supp(V)].rank())
print('SECOND_INSERTED_ARC',(3,5),'STEP',t2)
print('FINAL_VERTEX_SUPPORT',len(supp(W)),'RANK',C[:,supp(W)].rank())
print('ADJACENCY_UNION_SUPPORT',len(union),'UNION_RANK',C[:,union].rank(),
      'FACE_DIM',len(union)-C[:,union].rank())
print('TANGENT_DIRECTION_SUPPORT',sum(1 if u else 0 for u in d))
print('EXACT_THREE_CIRCUIT_IDENTITY',
      '-1/2 H(1,3;0,1,5) -7/5 H(2,3;1,2,4) -5/9 H(3,5;0,3,6)')
print('EXACT_MINIMUM_K23_WORD_LENGTH',3)
print('INTERMEDIATE_POSITIVE_ARCS',[(D[i],str(V[i])) for i in supp(V)])
print('EDGE_DIRECTION_NONZERO',[(D[i],str(d[i])) for i in range(len(D)) if d[i]])
print('PASS_EXACT_R5_ADJACENT_EDGE_RAY_WORD_LENGTH_THREE')


# NEW EXACT FOUR-ATOM EDGE, independently verified at the same frozen fiber.
v_data = {
 (0,0):'219346331/10192753200',
 (0,1):'7271277/135903376',(1,1):'29907399/169879220',
 (5,1):'7271277/339758440',(1,2):'8057361/169879220',
 (2,2):'9236487/679516880',(4,2):'11594739/679516880',
 (6,2):'196521/67951688',(2,3):'107583593/679516880',
 (3,3):'377644447/2548188300',(4,3):'50199461/679516880',
 (5,3):'14346033/339758440',(0,5):'196521/9707384',
 (6,5):'1375647/19414768',(6,6):'451274777/3397584400'
}
direction_data = {
 (0,1):'1/2',(1,1):'-7/10',(5,1):'1/5',
 (1,2):'7/10',(2,2):'-2/5',(4,2):'-4/5',(6,2):'1/2',
 (2,3):'2/5',(3,3):'-1',(4,3):'4/5',(5,3):'-1/5',
 (0,5):'-1/2',(3,5):'1',(6,5):'-1/2'
}
V4=Matrix([Q(v_data.get(a,'0')) for a in D])
d4=Matrix([Q(direction_data.get(a,'0')) for a in D])
assert C*V4==C*x
assert C*d4==Matrix.zeros(21,1)
assert len(supp(V4))==C[:,supp(V4)].rank()==15
assert min(V4)>=0
exact_four = (-Q(1,2)*H(1,2,0,1,5)
 +Q(5,9)*H(5,2,0,3,6)
 +2*H(2,3,2,3,4)
 -Q(2,5)*H(2,3,2,4,5))
assert d4==exact_four
def srcrow(j,z):
 return {i:z[D.index((i,j))] for i in range(7)
         if (i,j) in D and z[D.index((i,j))]!=0}
assert [len(srcrow(j,d4)) for j in (1,2,3,5)]==[3,4,4,3]
assert set(srcrow(1,d4)) != set(srcrow(5,d4))
alternatives=[]
for u,w in ((2,3),(3,2)):
 rem=d4.copy()
 for low,high in ((1,u),(5,w)):
  for i,m in srcrow(low,d4).items():
   rem[D.index((i,low))]-=m
   rem[D.index((i,high))]+=m
 assert srcrow(1,rem)=={} and srcrow(5,rem)=={}
 assert srcrow(2,rem)=={i:-m for i,m in srcrow(3,rem).items()}
 alternatives.append((u,w,len(srcrow(2,rem))))
 assert len(srcrow(2,rem))==5
step4=min(V4[i]/(-d4[i]) for i in range(30) if d4[i]<0 and V4[i]>0)
assert step4==Q(11594739,543613504)
W4=V4+step4*d4
U4=sorted(set(supp(V4))|set(supp(W4)))
assert min(W4)>=0 and C*W4==C*x
assert len(supp(W4))==C[:,supp(W4)].rank()==15
assert len(U4)==16 and C[:,U4].rank()==15

# Verify the original physical parameter witness and 26 capacities, not only its C-fiber.
p4=[Q(q) for q in (
 '1,1016902/1213423,1,2304159/67951688,0,2273985/9707384,0,'
 '1,5573459/8493961,6949106/8493961,0,8483579/33975844,'
 '1701717/8493961,5573459/84939610').split(',')]
e04=Matrix([Q(q) for q in (
 '219346331/10192753200,7664319/135903376,2813871/16987922,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,393042/8493961,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,5251441/33975844,166713611/1274094150,'
 '2500147/33975844,393042/8493961,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,7664319/135903376,451274777/3397584400').split(',')])
def physical_mass(y):
 g,a,b,u,v,w,z=y
 return (Q(509,900)*u+Q(47,180)*z+Q(67,162)*(v-z)+w/100,
   Q(13,40)*a+b/80-u,(g-a)/2,
   1-g+a/10+Q(9,40)*b-v+Q(191,450)*(u+w)+Q(43,90)*z+Q(14,81)*(v-z),
   (g-b)/2,Q(3,40)*a+Q(21,80)*b-w,
   u/100+Q(47,180)*z+Q(67,162)*(v-z)+Q(509,900)*w)
def physical_times(y):
 g,a,b,u,v,w,z=y
 return (1+g+Q(3,8)*a+Q(5,8)*b+u/2+v+Q(3,2)*w,
         1+g+(a+b)/2+u+v+w)
def physical_slacks(y):
 g,a,b,u,v,w,z=y
 return (a,g-a,1-g,b,g-b,u,Q(13,40)*a+b/80-u,
   w,Q(3,40)*a+Q(21,80)*b-w,z,a/10-z,v-z,z+Q(9,40)*b-v)
a,b=p4[:7],p4[7:]
physical_equalities=(a[0]-a[2],b[0]-1,b[6]-b[1]/10,
 *[s-t for s,t in zip(physical_times(a),physical_times(b))])
assert len(physical_equalities)==5 and all(z==0 for z in physical_equalities)
capacity=physical_slacks(a)+physical_slacks(b)
assert len(capacity)==26 and all(z>=0 for z in capacity)
assert all(z>0 for z in e04)
mu,nu=physical_mass(b),physical_mass(a)
bobs=Matrix([*mu,*nu,*[r[j]*nu[j] for j in range(7)])
assert C*e04==bobs==C*V4
print('FOUR_EDGE_PHYSICAL_EQUALITIES',5,'ALL_ZERO')
print('FOUR_EDGE_CAPACITY_SLACKS',26,'ALL_NONNEGATIVE')
print('FOUR_EDGE_FROZEN_OBSERVER_RANK',C.rank())
print('FOUR_EDGE_END_VERTEX_SUPPORTS',len(supp(V4)),len(supp(W4)))
print('FOUR_EDGE_ADJACENCY_UNION_SIZE_RANK',len(U4),C[:,U4].rank())
print('FOUR_EDGE_BOUNDARY_STEP',step4)
print('FOUR_EDGE_DIRECTION_SUPPORT',len([t for t in d4 if t!=0]))
print('FOUR_EDGE_THREE_ATOM_CASES_REMAINDER_SIZE',alternatives)
print('FOUR_EDGE_EXACT_DECOMPOSITION',
      '-1/2 H(1,2;0,1,5) +5/9 H(5,2;0,3,6) +2 H(2,3;2,3,4) -2/5 H(2,3;2,4,5)')
print('FOUR_EDGE_EXACT_MINIMUM_WORD_LENGTH',4)
print('PASS_EXACT_R5_ADJACENT_EDGE_RAY_WORD_LENGTH_FOUR')
