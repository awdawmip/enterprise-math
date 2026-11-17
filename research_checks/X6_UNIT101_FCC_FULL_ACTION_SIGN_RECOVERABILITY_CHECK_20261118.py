from itertools import permutations, product, combinations
from collections import Counter
import json
V='ABCD'
E=tuple(combinations(V,2))
vec=((1,1,0),(1,0,1),(0,1,-1),(0,1,1),(1,0,-1),(1,-1,0))
def det(m):
 return m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
def matvec(m,v):return tuple(sum(m[i][j]*v[j] for j in range(3)) for i in range(3))
def mul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def signed(m):
 out=[]
 for v in vec:
  z=matvec(m,v)
  opts=[(j,s) for j,w in enumerate(vec) for s in (-1,1) if z==tuple(s*q for q in w)]
  if len(opts)!=1:raise AssertionError(('not unique',m,z,opts))
  out.append(opts[0])
 return tuple(out)
def compose(a,b):return tuple((a[j][0],a[j][1]*s) for j,s in b)
def require(x,m):
 if not x:raise AssertionError(m)
rot=[]
for p in permutations(range(3)):
 for s in product((-1,1),repeat=3):
  m=[[0]*3 for _ in range(3)]
  for j,row in enumerate(p):m[row][j]=s[j]
  m=tuple(map(tuple,m))
  if det(m)==1:rot.append(m)
require(len(rot)==24,'rotations')
full={m:signed(m) for m in rot}
unsigned={tuple(t for t,s in image):m for m,image in full.items()}
require(len(unsigned)==24,'faithfulness')
for a in rot:
 for b in rot:
  require(full[mul(a,b)]==compose(full[a],full[b]),'composition')
amb=[]
for src in range(6):
 for tgt in range(6):
  signs=Counter(s for image in full.values() for t,s in [image[src]] if t==tgt)
  require(sum(signs.values())==4,'stabilizer')
  amb.append((src,tgt,signs[-1],signs[1]))
require(len(amb)==36,'pairs')
require(all(a>0 and b>0 for _,_,a,b in amb),'each individual edge ambiguity')
witness=(( -1,0,0),(0,-1,0),(0,0,1))
require(tuple(t for t,s in full[witness]) in unsigned,'witness')
res={'schema':'X6_UNIT101_FCC_SIGNED_CARRIER_RECOVERABILITY_V1',
 'domain':'24 determinant-positive signed 3x3 coordinate permutations; six derived FCC edge carriers',
 'full_unsigned_permutations':len(unsigned),
 'full_signed_actions':len(set(full.values())),
 'lookup_collisions':24-len(unsigned),
 'matrix_pair_compositions_checked':len(rot)**2,
 'signed_basis_equalities_checked':len(rot)**2*6,
 'edge_source_target_pairs':len(amb),
 'counts_per_edge_target':sorted(set((a,b) for _,_,a,b in amb)),
 'single_edge_target_ambiguous_in_all_pairs':all(a>0 and b>0 for _,_,a,b in amb),
 'strongest_inference':'complete unsigned six-edge permutation identifies the unique signed orientation action; individual edge target alone does not',
 'native_p000_six_axis_rotation_claimed':False,'review_status':'UNREVIEWED / NOT_ADMITTED'}
print(json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2))
