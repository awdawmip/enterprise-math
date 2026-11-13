#!/usr/bin/env python3
"""PREFIX583-R2: exact quartic/native X6-BRC axis stabilizers; standard library only."""
from itertools import product
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import json

path=Path(__file__).with_name('PREFIX581_R2_exact_monomial_certificate.json')
obj=json.loads(path.read_text(encoding='utf-8'))
C={tuple(map(int,k.split('/'))):Fraction(v) for k,v in obj['coefficients'].items()}
assert len(C)==126 and all(sum(e)==4 for e in C)
Z=(0,)*6
def mul(A,B):
 out=defaultdict(Fraction)
 for e,x in A.items():
  for f,y in B.items():out[tuple(e[i]+f[i] for i in range(6))]+=x*y
 return {k:v for k,v in out.items() if v}
def transformed(p):
 X=[{tuple(int(i==j) for i in range(6)):Fraction(1)} for j in range(5)]+[{}]
 L=[]
 for j in range(5):
  t=defaultdict(Fraction)
  for e,v in X[p[j]].items():t[e]+=v
  for e,v in X[p[5]].items():t[e]-=v
  L.append({e:v for e,v in t.items() if v})
 L.append({(0,0,0,0,0,1):Fraction(1)})
 out=defaultdict(Fraction)
 for exp,v in C.items():
  term={Z:v}
  for j,power in enumerate(exp):
   for _ in range(power):term=mul(term,L[j])
  for e,x in term.items():out[e]+=x
 return {e:x for e,x in out.items() if x}

def single_axis_gate(i):
 x=[int(j==i) for j in range(5)] if i<5 else [-1]*5
 return sum(v*__import__('math').prod(x[j]**e[j] for j in range(5)) for e,v in C.items() if e[5]==1)
cls=[single_axis_gate(i) for i in range(6)]
assert cls[0]==cls[2] and cls[1]==cls[3] and cls[4]==cls[5] and len(set(cls))==3
perms=[]
for a,b,c in product((0,1),repeat=3):
 p=list(range(6))
 for flag,i,j in ((a,0,2),(b,1,3),(c,4,5)):
  if flag:p[i],p[j]=p[j],p[i]
 perms.append(tuple(p))
quad=[p for p in perms if transformed(p)==C]
assert set(quad)=={(0,1,2,3,4,5),(0,1,2,3,5,4),(2,3,0,1,4,5),(2,3,0,1,5,4)}

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple((-1 if c>0 else 1)*k for k in STARS[a] if k!=abs(c))
PHASE=tuple((a,p,s*k) for a in range(4) for k in STARS[a] for s in(-1,1) for p in near(a,s*k))
IX={t:i for i,t in enumerate(PHASE)}
def nexts(i):
 a,p,c=PHASE[i];b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
 return tuple(IX[t] for t in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
NEXT=[nexts(i) for i in range(48)]; TARGET=IX[(0,1,-3)]
def edge(port,slot,nb):
 phase,bit=divmod(port,2); dest=NEXT[phase][slot]
 return (2*dest+nb,abs(PHASE[phase][2]),int(bit==nb==1 and dest==TARGET))
gates=[(port,slot,nb) for port in range(96) for slot,nb in product(range(3),(0,1)) if edge(port,slot,nb)[2]]
assert len(gates)==3 and {edge(*z)[1] for z in gates}=={1}
# Exact uniform one-step mixed moment and covariance: reduced observer separator.
total=96*6
axis_counts=[sum(1 for v in range(96) for sl,nb in product(range(3),(0,1)) if edge(v,sl,nb)[1]==i) for i in range(1,7)]
assert axis_counts==[96]*6
pK=Fraction(len(gates),total)
cov1=Fraction(3,total)-Fraction(axis_counts[0],total)*pK
cov3=Fraction(0,total)-Fraction(axis_counts[2],total)*pK
assert pK==Fraction(1,192) and cov1==Fraction(5,1152) and cov3==Fraction(-1,1152)
swap=(1,2,3,4,6,5)
def image(x):return (1 if x>0 else -1)*swap[abs(x)-1]
map48=[]
for a,p,c in PHASE:
 u,v=image(p),image(c)
 new=[j for j,star in enumerate(STARS) if {abs(u),abs(v)}<=set(star)]
 assert len(new)==1
 map48.append(IX[(new[0],u,v)])
assert len(set(map48))==48 and map48[TARGET]==TARGET
map96=tuple(2*map48[i//2]+i%2 for i in range(96))
assert len(set(map96))==96
for port in range(96):
 for slot,nb in product(range(3),(0,1)):
  dest,axis,gate=edge(port,slot,nb)
  assert (map96[dest],swap[axis-1],gate) in [edge(map96[port],newslot,nb) for newslot in range(3)]
native=[p for p in quad if p[0]==0]
assert set(native)=={(0,1,2,3,4,5),(0,1,2,3,5,4)}
result={'schema':'PREFIX583_R2_SYMMETRY_V1','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'exact_quartic_monomials':len(C),'single_axis_gate_a3b':[str(x) for x in cls],
 'axis_candidates_by_invariants':len(perms),'quartic_group_order':len(quad),'quartic_permutations':[[i+1 for i in p] for p in quad],
 'native_marked_group_order':len(native),'native_permutations':[[i+1 for i in p] for p in native],
 'gate_edge_count':len(gates),'gate_source_axis':1,'checked_native_lift_edges':96*6,
 'uniform_depth_one_gate_expectation':str(pK),'uniform_depth_one_cov_R1_K':str(cov1),'uniform_depth_one_cov_R3_K':str(cov3),
 'phase_lift_swap_5_6':map48,'status':'ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED'}
Path(__file__).with_name('PREFIX583_R2_symmetry_certificate_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('quartic_group_order','native_marked_group_order','checked_native_lift_edges','status')},indent=2))
