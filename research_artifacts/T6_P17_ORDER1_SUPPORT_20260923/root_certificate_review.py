"""Non-author certificate audit; symbolic rational identities, no search rerun.

The determinant is independently expanded by subset minors (no division).
Gram data are checked via G=M D M^T, not the author's Gram-Schmidt routine.
Only divisibility/floor materialization uses the existing BRC facade.
"""
import hashlib
import itertools
import json
import sys
from pathlib import Path

BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE/'dependencies'))
from enterprise_math.exact_arithmetic import division, brc_evaluate_division

trace_count=0
def qr(n,d):
 global trace_count
 t=brc_evaluate_division(division(abs(n),d));trace_count+=1
 q,r=t.quotient,t.remainder
 if n<0:q,r=(-q,0) if r==0 else (-q-1,d-r)
 assert n==q*d+r and 0<=r<d
 return q,r

class Q:
 def __init__(self,n=0,d=1):
  self.n,self.d=int(n),int(d);assert self.d>0
 def __add__(self,b):
  if isinstance(b,int):b=Q(b)
  return Q(self.n*b.d+b.n*self.d,self.d*b.d)
 __radd__=__add__
 def __mul__(self,b):
  if isinstance(b,int):b=Q(b)
  return Q(self.n*b.n,self.d*b.d)
 __rmul__=__mul__
 def eq(self,b):
  if isinstance(b,int):b=Q(b)
  return self.n*b.d==b.n*self.d
 def above(self,b):return self.n>b*self.d

def determinant(rows):
 prev={():1}
 for k in range(1,len(rows)+1):
  nxt={}
  for cols in itertools.combinations(range(len(rows)),k):
   sign=(-1)**(k-1);value=0
   for position,column in enumerate(cols):
    value+=sign*rows[k-1][column]*prev[cols[:position]+cols[position+1:]]
    sign=-sign
   nxt[cols]=value
  prev=nxt
 return prev[tuple(range(len(rows)))]

def product(values):
 out=1
 for value in values:out*=value
 return out

data_bytes=(BASE/'portable_input.json').read_bytes();cert_bytes=(BASE/'certificate.json').read_bytes()
p=json.loads(data_bytes);c=json.loads(cert_bytes)
assert hashlib.sha256(data_bytes).hexdigest()==c['portable_input_sha256']
assert p['prime']=='17' and p['residue']=='1' and p['vertical_order']=='1'
assert p['q0_positive_budget']=='2026' and p['q0_negative_budget']=='2331'
radius=2026**2+2331**2;assert radius==9538237==int(p['radius_squared'])
w=list(map(int,p['weights']));B=[list(map(int,r)) for r in p['weighted_basis']]
U=[list(map(int,r)) for r in p['unweighted_basis']]
x=list(map(int,p['weighted_particular']));u=list(map(int,p['particular_q0']))
assert w==[17*j-1 for j in range(1,17)]
assert len(B)==len(U)==16 and all(len(r)==16 for r in B+U)
assert B==[[a*b for a,b in zip(row,w)] for row in U]
assert x==[a*b for a,b in zip(u,w)]
det=determinant(U);assert abs(det)==17**21
# Clearing unit denominators gives the same congruences. The six-coordinate
# inverse-power minor is a nonzero Vandermonde modulo 17, hence the target
# map onto product_k Z/(17**k) is surjective. Index and determinant coincide.
for k in range(1,7):
 powers=[j**k for j in range(1,17)]
 coefficients=[18**k*product(powers[:j]+powers[j+1:]) for j in range(16)]
 modulus=17**k
 for row in U:assert qr(sum(a*b for a,b in zip(row,coefficients)),modulus)[1]==0
 assert qr(sum(a*b for a,b in zip(u,coefficients))+product(powers),modulus)[1]==0
D=[Q(*a) for a in p['gram_schmidt_squared']]
M=[[Q(*a) for a in row] for row in p['mu']]
centers=[Q(*a) for a in p['centers']]
assert all(d.above(radius) for d in D)
for i in range(16):
 for j in range(16):
  if j>i:assert M[i][j].eq(0)
  if j==i:assert M[i][j].eq(1)
  direct=sum(a*b for a,b in zip(B[i],B[j]))
  assert sum(M[i][k]*D[k]*M[j][k] for k in range(min(i,j)+1)).eq(direct)
 assert sum(M[i][k]*D[k]*centers[k] for k in range(i+1)).eq(sum(a*b for a,b in zip(x,B[i])))
assert sum(D[k]*centers[k]*centers[k] for k in range(16)).eq(sum(a*a for a in x))
nodes={node['id']:node for node in c['nodes']};assert len(nodes)==len(c['nodes'])==8
visited=set();chosen=[0]*16;pruned=0
def audit_node(ident,level,partial):
 global pruned
 assert ident not in visited;visited.add(ident);node=nodes[ident];assert node['level']==level
 center=centers[level]+sum(chosen[j]*M[j][level] for j in range(level+1,16))
 assert center.eq(Q(*node['center'])) and partial.eq(Q(*node['partial_before']))
 f=node['floor_witness'];n,d,q,r=(int(f[k]) for k in ('numerator','denominator','quotient','remainder'))
 assert center.eq(Q(n,d)) and qr(n,d)==(q,r)
 assert [int(a['coefficient']) for a in node['options']]==[-q-1,-q]
 for option in node['options']:
  z=int(option['coefficient']);chosen[level]=z
  error=center+z;term=D[level]*error*error;total=partial+term
  assert term.eq(Q(*option['squared_component'])) and total.eq(Q(*option['partial_after']))
  if total.above(radius):
   assert option['decision']=='PRUNE_EXACT_SQUARED_NORM' and 'child' not in option;pruned+=1
  else:
   assert level>0 and option['decision']=='DESCEND'
   audit_node(option['child'],level-1,total)
audit_node(c['root'],15,Q())
assert visited==set(nodes) and c['full_leaves']==0 and c['kernel'] is None and c['status']=='R1_AFFINE_CLASS_EMPTY'
receipt={'schema':'T6_R1_NONAUTHOR_COMPUTATIONAL_REVIEW_V1','status':'PASS_FINITE_R1_EXCLUSION',
 'reviewer':'root agent; different authoring process; source-exposed, not a formal independent Driver acceptance',
 'portable_input_sha256':hashlib.sha256(data_bytes).hexdigest(),'certificate_sha256':hashlib.sha256(cert_bytes).hexdigest(),
 'review_code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'basis_determinant':str(det),'dimension':16,'degree':6,'radius_squared':str(radius),
 'basis_kernel_index':'17**21; surjectivity follows from unit inverse-power Vandermonde minor',
 'gram_check':'ALL_256_INTEGER_GRAM_IDENTITIES_AND_16_CENTER_IDENTITIES',
 'search_tree':'COMPLETE_CERTIFICATE_CONSUMPTION_WITHOUT_SOLVER_RERUN','nodes':len(visited),'pruned_edges':pruned,
 'brc_materializations':trace_count,'scope':'p=17, order=1, r=1 only; no claim of full T6 completion or acceptance of the older Result',
 'scientific_statement':'No signed integer q0 vector satisfies all six affine congruences and the stated positive/negative mass bounds.'}
(BASE/'ROOT_REVIEW.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(receipt))
