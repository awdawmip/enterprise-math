#!/usr/bin/env python3
"""PREFIX584-R2 exact structural certificate; the all-length proof is the companion paper."""
import json
from pathlib import Path
from itertools import product
STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple((-1 if c>0 else 1)*k for k in STARS[a] if k!=abs(c))
PHASE=tuple((a,p,s*k) for a in range(4) for k in STARS[a] for s in(-1,1) for p in near(a,s*k))
IX={x:i for i,x in enumerate(PHASE)}
def nexts(i):
 a,p,c=PHASE[i];b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
 return tuple(IX[x] for x in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
NEXT=[nexts(i) for i in range(48)]
TARGET=IX[(0,1,-3)]
ALPHA=(3,4,1,2,5,6)
def flip(x):return (-1 if x>0 else 1)*ALPHA[abs(x)-1]
THETA=[]
for a,p,c in PHASE:
 u,v=flip(c),flip(p)
 ns=[j for j,t in enumerate(STARS) if abs(u) in t and abs(v) in t]
 assert len(ns)==1
 THETA.append(IX[(ns[0],u,v)])
assert len(set(THETA))==48 and all(THETA[THETA[i]]==i for i in range(48))
assert THETA[TARGET]==TARGET
edges={(i,j) for i in range(48) for j in NEXT[i]}
assert len(edges)==144
assert all((THETA[j],THETA[i]) in edges for i,j in edges)
assert all(abs(PHASE[THETA[j]][2])==ALPHA[abs(PHASE[i][2])-1] for i,j in edges)
def matmul(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def trace_word(word,z):
 A=((1,0),(0,1))
 for t in word:A=matmul(A,((1,1),(1,z if t else 1)))
 return A[0][0]+A[1][1]
for n in range(1,11):
 for w in product((0,1),repeat=n):
  for z in (0,2,7):
   a=trace_word(w,z)
   assert a==trace_word(tuple(reversed(w)),z)==trace_word(w[1:]+w[:1],z)
out={'schema':'PREFIX584_R2_ALL_LENGTH_CLOSED_TRACE_INVARIANCE_CERTIFICATE_V1',
 'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'phase_count':48,'native_port_count':96,'original_labeled_action_count':576,
 'phase_edges_checked':144,'phase_involution':THETA,'gate_target_phase_index':TARGET,
 'permutation_on_absolute_axes':list(ALPHA),
 'phase_edge_reversal_and_reward_permutation_check':True,
 'finite_bit_transfer_trace_identity_checks':'all binary words lengths 1..10, z in {0,2,7}',
 'general_all_length_proof':'exact phase anti-involution plus formal 2x2 symmetric transfer trace; see companion paper',
 'status':'ALL_ASSERTIONS_PASS_STRUCTURAL_AUTHOR_SIDE_UNREVIEWED'}
Path(__file__).with_name('PREFIX584_R2_all_length_trace_involution_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'phase_edges':144,'phase_count':48,'status':out['status']}))
