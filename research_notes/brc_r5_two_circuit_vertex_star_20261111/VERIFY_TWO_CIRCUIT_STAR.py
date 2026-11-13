from sympy import Matrix, Rational as Q
from itertools import combinations
from collections import Counter,defaultdict
r=list(map(Q,['1/10','1/2','3/4','1','5/4','3/2','19/10']))
D=[(i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j]
C=Matrix.hstack(*(Matrix([int(i==k) for k in range(7)]+[int(j==k) for k in range(7)]+[r[i] if j==k else 0 for k in range(7)]) for i,j in D))
M={(0,0):'219346331/10192753200',(0,1):'18669495/951323632',(1,1):'1898238/8493961',(5,1):'3733899/475661816',(2,2):'196521/2426846',(0,3):'8057361/237830908',(2,3):'1544855/16987922',(3,3):'377644447/2548188300',(4,3):'1544855/16987922',(5,3):'26530335/475661816',(6,3):'196521/67951688',(0,5):'196521/9707384',(6,5):'1375647/19414768',(6,6):'451274777/3397584400'}
x=Matrix([Q(M[a]) if a in M else 0 for a in D]);
P=[i for i,v in enumerate(x) if v>0]; Z=[i for i,v in enumerate(x) if not v]
assert C.rank()==15 and C[:,P].rank()==14
I=list(C[:,P].T.rref()[1]);Ainv=C[I,P].inv()
coeff={k:Ainv*C[I,k] for k in Z};lam={k:C[16,k]-(C[16,P]*coeff[k])[0] for k in Z}
assert len([k for k in Z if lam[k]==0])==10
rays=[]
def pivot(adds,weights):
 d=Matrix.zeros(30,1)
 for k,w in zip(adds,weights):d[k]=w
 old=-sum((coeff[k]*w for k,w in zip(adds,weights)),Matrix.zeros(14,1))
 for p,v in zip(P,old):d[p]=v
 assert C*d==Matrix.zeros(21,1)
 rays.append((tuple(D[k] for k in adds),tuple(d)))
for k in Z:
 if not lam[k]:pivot((k,),(Q(1),))
for k,l in combinations(Z,2):
 if lam[k]<0<lam[l]:pivot((k,l),(lam[l],-lam[k]))
 if lam[l]<0<lam[k]:pivot((l,k),(lam[k],-lam[l]))
assert len(rays)==18
# 210 normalized 6-edge K23 circuits
circs=[]
for j,k in combinations([1,2,3,5],2):
 for a,b,c in combinations(range(7),3):
  v=[Q(0)]*30
  for i,w in ((a,r[b]-r[c]),(b,r[c]-r[a]),(c,r[a]-r[b])):
   v[D.index((i,j))]=w
   v[D.index((i,k))]=-w
  assert C*Matrix(v)==Matrix.zeros(21,1)
  circs.append(((j,k),(a,b,c),tuple(v)))
assert len(circs)==210
# normalize nonzero vector for scalar-invariant dictionary

def key(z):
 first=next((v for v in z if v),None)
 if first is None:return None
 return tuple(v/first for v in z)
ck={key(v): (j,abc) for j,abc,v in circs}
print('CIRCUITS',len(circs),'RAYS',len(rays))
classes=Counter(); decomposition_counts={}
for arcs,d in rays:
 d=tuple(d); sup=sum(bool(a) for a in d)
 if sup==6:
  assert key(d) in ck
  print('ARC',arcs,'SUPPORT',6,'MIN_CIRCUIT_COUNT',1)
  classes[(6,1)]+=1
  continue
 candidates=[]
 for j,abc,v in circs:
  for z,abc2,w in circs:
   if (j,abc)>=(z,abc2):continue
   # select two independent support rows
   ix=next((i for i in range(30) if v[i] and not w[i]), None)
   if ix is None: continue
   a=d[ix]/v[ix]
   if not a:continue
   iy=next((i for i in range(30) if w[i]),None)
   b=(d[iy]-a*v[iy])/w[iy]
   if not b:continue
   if all(d[i]==a*v[i]+b*w[i] for i in range(30)):
    candidates.append(((j,abc),(z,abc2),a,b))
 assert sup in (9,10) and candidates
 classes[(sup,2)]+=1
 decomposition_counts[arcs]=len(candidates)
 print('ARC',arcs,'SUPPORT',sup,'TWO_CIRCUIT_DECOMPOSITIONS',len(candidates))
 if candidates:
  print('  CERTIFICATE',candidates[0])
  ainfo,binfo,aa,bb=candidates[0]
  u=next(v for j,abc,v in circs if (j,abc)==ainfo)
  v=next(v for j,abc,v in circs if (j,abc)==binfo)
  nneg_u=[D[k] for k in Z if aa*u[k]<0]
  nneg_v=[D[k] for k in Z if bb*v[k]<0]
  print('  SINGLE_COMPONENT_NEGATIVE_ZERO_ARCS',nneg_u,nneg_v)


assert classes == Counter({(6,1):13,(9,2):2,(10,2):3})
assert sorted(decomposition_counts.values())==[1,1,1,3,3]
print('CLASSIFICATION',dict(classes))
print('PASS_EXACT_TWO_CIRCUIT_STAR_18_OF_18')
