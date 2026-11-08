#!/usr/bin/env python3
"""PREFIX589 exact dual native X6 BRC carrier certificate; Python standard library."""
import json
from pathlib import Path
from collections import Counter
from fractions import Fraction
STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple(-k if c>0 else k for k in STARS[a] if k!=abs(c))
P=tuple((a,p,t*k) for a in range(4) for k in STARS[a] for t in (-1,1) for p in near(a,t*k))
IX={v:i for i,v in enumerate(P)}
def nxt(i):
 a,p,c=P[i]; b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
 return tuple(IX[t] for t in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
N=tuple(nxt(i) for i in range(48))
S=[[int(j in N[i]) for j in range(48)] for i in range(48)]
REV=[IX[(a,c,p)] for a,p,c in P]
TARGET=IX[(0,1,-3)]
assert len(P)==48 and len({c for _,_,c in P})==12 and all(len(t)==3 for t in N)
assert all(REV[REV[i]]==i for i in range(48))
WP=[[int(i!=k and P[i][2]==P[k][2]) for k in range(48)] for i in range(48)]
assert all(S[i][REV[k]]==WP[i][k] for i in range(48) for k in range(48))
assert all(S[REV[i]][REV[j]]==S[j][i] for i in range(48) for j in range(48))
blocks=[]
for c in sorted({c for a,p,c in P}):
 indices=[i for i,(a,p,q) in enumerate(P) if q==c]
 assert len(indices)==4
 for bit in (0,1):blocks.append(tuple(2*i+bit for i in indices))
assert len(blocks)==24 and len({x for b in blocks for x in b})==96
bid={idx:b for b,group in enumerate(blocks) for idx in group}

def base_coefs(dual):
 """All seven 96x96 coefficient arrays from original / reversed native tagged edges."""
 coeffs=[[[0]*96 for _ in range(96)] for _ in range(7)]
 for i in range(48):
  axis=abs(P[i][2])-1
  succ=(j for j in range(48) if S[j][i]) if dual else N[i]
  marked=(REV[i]==TARGET) if dual else None
  for j in succ:
   for u in (0,1):
    for v in (0,1):
     gate=(marked and u==v==1) if dual else (j==TARGET and u==v==1)
     if gate:assert axis==0
     coeffs[6 if gate else axis][2*i+u][2*j+v]+=1
 return coeffs
A=base_coefs(False);D=base_coefs(True)
assert all(t in (0,1) for C in A+D for row in C for t in row)

def conjugate(C):
 """Compute W^-1 C W entrywise exactly, using only the original 4-port blocks."""
 out=[[Fraction(0)]*96 for _ in range(96)]
 for i in range(96):
  group=blocks[bid[i]]
  for j in range(96):
   dg=blocks[bid[j]]
   a=sum(C[k][l] for k in group for l in dg if l!=j)
   b=sum(C[i][l] for l in dg if l!=j)
   out[i][j]=Fraction(a,3)-b
 return out
for a in range(7):
 V=conjugate(A[a])
 assert all(V[i][j]==D[a][i][j] for i in range(96) for j in range(96)),a

original_gate=[i for i in range(96) for j in range(96) if A[6][i][j]]
dual_gate=[i for i in range(96) for j in range(96) if D[6][i][j]]
assert sorted(Counter(original_gate).values())==[1,1,1]
assert sorted(Counter(dual_gate).values())==[3]
assert len(set(original_gate))==3 and len(set(dual_gate))==1
counts=[sum(map(sum,C)) for C in D]
assert counts==[93,96,96,96,96,96,3] and sum(counts)==576
for port in range(96):
 ax=abs(P[port//2][2])-1
 assert sum(D[k][port][j] for k in range(7) for j in range(96))==6
 assert all(not D[k][port][j] for j in range(96) for k in range(6) if k!=ax)
for C in (A,D):
 E=[[sum(M[i][j] for M in C) for j in range(96)] for i in range(96)]
 assert all(v in (0,1) for row in E for v in row)
 assert all(sum(row)==6 for row in E)
 assert all(sum(E[i][j] for i in range(96))==6 for j in range(96))

for group in blocks:
 for singled in group:
  r={j:int(j==singled) for j in group}
  y=[Fraction(sum(r.values()),3)-r[j] for j in group]
  assert sorted(y)==[Fraction(-2,3)]+[Fraction(1,3)]*3
def minimal_buffer(r):
 assert len(r)==4 and all(v>=0 for v in r)
 return max(0,*(3*v-sum(r) for v in r))
for group in blocks:
 for singled in group:
  r=[int(j==singled) for j in group]
  t=minimal_buffer(r)
  assert t==2
  rr=[v+t for v in r]
  assert all(Fraction(sum(rr),3)-v>=0 for v in rr)
  assert any(Fraction(sum(rr),3)-v==0 for v in rr)
for r in [[0,0,0,0],[4,1,1,2],[1,5,0,7],[3,3,3,3]]:
 t=minimal_buffer(r)
 assert all(3*(v+t)<=sum(r)+4*t for v in r)
 if t>0:assert any(3*(v+t-1)>sum(r)+4*(t-1) for v in r)

def weighted(C,x,z):
 return [[sum(x[a]*C[a][i][j] for a in range(6))+x[0]*z*C[6][i][j]
          for j in range(96)] for i in range(96)]
def multiply(M,v):return [sum(t*w for t,w in zip(row,v)) for row in M]
for x,z in [((1,1,1,1,1,1),0),((1,1,1,1,1,1),1),((2,3,5,7,11,13),17),((0,1,0,0,0,0),7)]:
 a=weighted(A,x,z);d=weighted(D,x,z)
 va=[1]*96;vd=[1]*96
 for depth in range(7):
  assert sum(va)==sum(vd),(x,z,depth)
  va=multiply(a,va);vd=multiply(d,vd)
sequence=[((1,1,1,1,1,1),0),((2,3,5,7,11,13),17),((0,1,0,0,0,0),2),((4,1,7,5,9,2),3)]
va=[1]*96;vd=[1]*96
for x,z in sequence:
 va=multiply(weighted(A,x,z),va);vd=multiply(weighted(D,x,z),vd)
 assert sum(va)==sum(vd)
result={
 'schema':'PREFIX589_R2_DUAL_TYPED_BRC_CARRIER_V1',
 'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'phases':48,'native_ports':96,'labelled_actions':576,
 'phase_identities':'W_phase=SR and RSR=S^T, 2304 exact entries each',
 'dual_identity':'W^-1 A(x,z) W = X (R D(z) R) S^T (two-bit lifted)',
 'all_rational_coefficient_entries_checked':7*96*96,
 'coefficient_nonzero_counts':counts,
 'source_axis_rows':96,
 'original_gate_sources':sorted(Counter(original_gate).items()),
 'dual_gate_sources':sorted(Counter(dual_gate).items()),
 'gate_label_preserving_port_isomorphism':False,
 'original_singleton_dual_values':['-2/3','1/3','1/3','1/3'],
 'minimal_uniform_buffer':'t_g=max(0,max_i(3*r_i-sum_group(r)))',
 'singleton_minimal_buffer':2,
 'uniform_open_path_checks':'all depths 0..6, four weight points, nonstationary 4-step sequence',
 'native_and_dual_direct_sparse_weighted_terms_per_step':576,
 'status':'ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED'
}
Path(__file__).with_name('PREFIX589_R2_dual_carrier_results.json').write_text(
 json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(result['status'], 'original gate',result['original_gate_sources'],
      'dual gate',result['dual_gate_sources'])
