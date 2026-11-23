#!/usr/bin/env python3
"""R749SPT: exact regular unimodular triangulation for R749SPR's signed-Walsh minimax-center polytope.
Only Python standard library. The fixed lift is a discovery-independent executable certificate.
All determinants, supporting tests and counting use integers; no float/scipy in validation.
"""
from itertools import combinations, product
from collections import Counter, defaultdict
import hashlib, json

FACETS=(
 ((-1,-1,-1),-2),((-1,-1,1),-2),((-1,1,-1),-2),((-1,1,1),-2),
 ((1,-1,-1),-2),((1,-1,1),-4),((1,1,-1),-4),((1,1,1),-2))
JITTER=(16,13,25,9,30,11,9,5,24,22,22,17,21,8,3,29,0,7,12,26,23,13,8,27,16,25,10,20,27,21,30,23,12)

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def det3(a,b,c):
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def inside(p,n=1): return all(dot(m,p)>=n*b for m,b in FACETS)
P=tuple(x for x in product(range(-4,5),repeat=3) if inside(x))
assert len(P)==33 and len(JITTER)==33
Z=tuple(1000*dot(x,x)+j for x,j in zip(P,JITTER))

# Every exact supporting lower 4-vertex facet of the lifted 33-point polytope.
# For each nondegenerate candidate, Cramer's rule reconstructs its affine height.
lower=[]
nondegenerate=0
coplanar_lower=0
for ids in combinations(range(len(P)),4):
 p0,p1,p2,p3=(P[i] for i in ids)
 a,b,c=sub(p1,p0),sub(p2,p0),sub(p3,p0)
 D=det3(a,b,c)
 if D==0: continue
 nondegenerate+=1
 z0=Z[ids[0]]
 dz=(Z[ids[1]]-z0,Z[ids[2]]-z0,Z[ids[3]]-z0)
 N=(det3((dz[0],a[1],a[2]),(dz[1],b[1],b[2]),(dz[2],c[1],c[2])),
    det3((a[0],dz[0],a[2]),(b[0],dz[1],b[2]),(c[0],dz[2],c[2])),
    det3((a[0],a[1],dz[0]),(b[0],b[1],dz[1]),(c[0],c[1],dz[2])))
 sg=1 if D>0 else -1
 count_tight=0
 valid=True
 for q,z in zip(P,Z):
  gap=sg*(D*(z-z0)-dot(N,sub(q,p0)))
  if gap<0:
   valid=False
   break
  if gap==0: count_tight+=1
 if valid:
  if count_tight>4: coplanar_lower+=1
  assert count_tight==4, ('non-simplicial lower face', ids, count_tight)
  assert abs(D)==1, ('non-unimodular lower simplex', ids, D)
  lower.append(ids)

assert len(lower)==92, len(lower)
assert coplanar_lower==0
# At any generic lower lifting, the supporting simplices are precisely the regular
# subdivision cells. Their determinant sum equals normalized volume 92 of K
# (independently established by R749SPS), hence they fill K.
assert sum(abs(det3(sub(P[i1],P[i0]),sub(P[i2],P[i0]),sub(P[i3],P[i0]))) for i0,i1,i2,i3 in lower)==92

# Exact face incidence independently audits boundary/topological closure.
faces=Counter(tuple(sorted(f)) for ids in lower for f in combinations(ids,3))
assert set(faces.values())=={1,2}
boundary=[face for face,mul in faces.items() if mul==1]
assert all(any(all(dot(m,P[i])==rhs for i in face) for m,rhs in FACETS) for face in boundary)
# Cone the boundary triangular mesh to the strict interior origin: exact independent volume check.
boundary_cone_volume = sum(abs(det3(*(P[i] for i in face))) for face in boundary)
assert boundary_cone_volume==92

# Every n-grid optimal center is a mean of n from this fixed set of 33
# first-grid centers: a lattice point in a unimodular simplex has integer barycentric
# coordinates after dilation. Check finite collision/provenance witness at n=2.
sums=defaultdict(list)
for i,j in combinations(range(len(P)),2):
 s=tuple(P[i][k]+P[j][k] for k in range(3))
 sums[s].append((i,j))
for i in range(len(P)):
 s=tuple(2*P[i][k] for k in range(3))
 sums[s].append((i,i))
assert len(sums)==179   # Ehrhart L_K(2)
assert sum(map(len,sums.values()))==561  # unordered 2-multisets of 33 types
assert all(inside(s,2) for s in sums)
max_mult=max(map(len,sums.values()))
first_collision=min((s,pairs) for s,pairs in sums.items() if len(pairs)>=2)
witness_sum, witness_pairs=first_collision
witness=[(P[i],P[j]) for i,j in witness_pairs[:2]]

result={
 'status':'PASS','unit':'R749SPT',
 'model':'frozen auxiliary 16-atom signed-Walsh probability source fiber',
 'frozen_science':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'predecessor':'R749SPR eight-facet complete minimax-center K; R749SPS exact Ehrhart counts',
 'precise_claim':'K has a certified regular unimodular triangulation; K has the integer decomposition property at every positive integer n',
 'grid1_lattice_points':len(P),
 'supporting_lower_tetrahedra':len(lower),
 'sum_absolute_lattice_determinants':92,
 'nonsingular_four_point_candidates':nondegenerate,
 'non_simplicial_lower_faces':coplanar_lower,
 'boundary_triangles':len(boundary),
 'boundary_cone_normalized_volume':boundary_cone_volume,
 'interior_triangles':sum(m==2 for m in faces.values()),
 'scale2_unordered_source_multisets':561,
 'scale2_distinct_lattice_centers':179,
 'scale2_max_source_multiset_multiplicity':max_mult,
 'scale2_collision_sum':list(witness_sum),
 'scale2_collision_witness':[[list(x) for x in pair] for pair in witness],
 'lifting':'z_i=1000*(H_i^2+U_i^2+V_i^2)+JITTER[i] on lexicographic 33 first-grid points',
 'jitter':list(JITTER),
 'tetrahedra_sha256':hashlib.sha256(json.dumps(lower,separators=(',',':')).encode()).hexdigest(),
 'independent_review':'NOT_REVIEWED',
 'origin_precision':'all integer exact; no floating-point comparisons',
 'native_X6_transfer':'NOT_ESTABLISHED'}
print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
