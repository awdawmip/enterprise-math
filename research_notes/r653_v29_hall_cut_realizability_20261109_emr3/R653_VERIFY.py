"""R653 exact Hall conditions for V29 TRANSFER event margins; no BRC numerical propagation."""
from itertools import product
import json

def hall(supply,demand,edges):
 A=len(supply)
 if sum(supply)!=sum(demand):return False
 for mask in range(1<<A):
  subset={i for i in range(A) if mask>>i&1}
  nbr={j for i,j in edges if i in subset}
  if sum(supply[i] for i in subset)>sum(demand[j] for j in nbr):return False
 return True

def reach(supply,demand,edges):
 S=sum(supply)
 if S!=sum(demand):return False
 for vals in product(range(S+1),repeat=len(edges)):
  if sum(vals)!=S:continue
  p=[0]*len(supply);q=[0]*len(demand)
  for (a,b),v in zip(edges,vals):p[a]+=v;q[b]+=v
  if p==list(supply) and q==list(demand):return True
 return False

missing=((0,0),(0,1),(1,0))
full=tuple(product(range(2),repeat=2))
checked=0;feasible=0;infeasible_balanced=0
for edges in (missing,full):
 for margins in product(range(4),repeat=4):
  s=margins[:2];t=margins[2:]
  h=hall(s,t,edges);r=reach(s,t,edges)
  assert h==r,(edges,margins,h,r)
  checked+=1;feasible+=h
  if sum(s)==sum(t) and not h:infeasible_balanced+=1
s=(0,1);t=(0,1)
assert sum(s)==sum(t)==1
assert not hall(s,t,missing) and not reach(s,t,missing)
assert hall(s,t,full) and reach(s,t,full)

# Four consecutive X6 unit-axis relative Cells; link only adjacent cells.
edges4=[(i,j) for i in range(4) for j in range(4) if abs(i-j)==1]
s4=(1,0,0,0);t4=(0,0,0,1)
assert not hall(s4,t4,edges4)
out=[0]*4;inn=[0]*4
for i,j,v in ((0,1,1),(2,1,-1),(2,3,1)):
 out[i]+=v;inn[j]+=v
assert tuple(out)==s4 and tuple(inn)==t4

print(json.dumps({
 'marker':'R653_SPARSE_TRANSFER_HALL_REALIZABILITY_EXACT_PASS',
 'margin_instances_exhaustively_checked':checked,
 'feasible_instances':feasible,
 'balanced_but_not_feasible_instances':infeasible_balanced,
 'two_port_counterexample':{'edges':missing,'out':s,'in':t,'violating_Hall_U':[1],'lhs':1,'rhs':0},
 'x6_unit_step_four_cell_counterexample':{
 'relative_positions':[(i,0,0,0,0,0) for i in range(4)],
 'out_per_cell_port0':s4,'in_per_cell_port0':t4,
 'signed_witness':[(0,1,1),(2,1,-1),(2,3,1)],'nonnegative_realization':False},
 'proof':'integer max flow/min cut with all Hall inequalities',
 'status':'author-side exact mathematics; no native CLAIM'
},ensure_ascii=False,indent=2))
