#!/usr/bin/env python3
"""Native 96-port X6-BRC: positive WE/EW factor, 49-state exact recurrence."""
from pathlib import Path
import runpy, json
s=runpy.run_path(str(Path(__file__).with_name('PREFIX589_R2_dual_carrier_certificate.py')))
A,T,P,N,REV,g,blocks=(s[z] for z in ('A','D','P','N','REV','TARGET','blocks'))
axis=[abs(p[2])-1 for p in P]
gsrc=REV[g]
bid={j:k for k,b in enumerate(blocks) for j in b}
E=[[[0]*96 for _ in range(96)] for _ in range(7)]
for k in range(7):
 for j in range(96):
  for b in blocks:
   t=[A[k][i][j] for i in b]
   assert all(v in (0,1) for v in t)
   if sum(t):
    assert sorted(t)==[0,1,1,1]
    E[k][b[t.index(0)]][j]=1
for k in range(7):
 for i in range(96):
  for j in range(96):
   assert A[k][i][j]==sum(E[k][t][j] for t in blocks[bid[i]] if t!=i)
   assert T[k][i][j]==sum(E[k][i][t] for t in blocks[bid[j]] if t!=j)
assert [sum(sum(row) for row in E[k]) for k in range(7)]==[31,32,32,32,32,32,1]
assert all(sum(E[k][i][j] for k in range(7) for j in range(96))==2 for i in range(96))
assert all(sum(E[k][i][j] for k in range(7) for i in range(96))==2 for j in range(96))
assert all(g not in N[g] for _ in (0,))
assert sum(g in N[i] for i in range(48))==3
for i in range(48):
 for bit in (0,1):
  got={(j,k) for k in range(7) for j,v in enumerate(E[k][2*i+bit]) if v}
  expected={(2*REV[i],axis[i]),(2*REV[i]+1,axis[i])}
  if i==gsrc and bit==1:
   expected.remove((2*REV[i]+1,0));expected.add((2*REV[i]+1,6))
  assert got==expected
edges=[[(j,k) for k in range(7) for j,v in enumerate(A[k][i]) if v] for i in range(96)]
def native(r,x,z):return [sum((x[0]*z if k==6 else x[k])*r[j] for j,k in row) for row in edges]
def state(r,z):return [r[2*i]+r[2*i+1] for i in range(48)],(z-1)*r[2*g+1]
def q(b,x):return [x[axis[i]]*sum(b[j] for j in N[i]) for i in range(48)]
def output(b,delta,x):
 v=q(b,x)
 return [value for i in range(48) for value in (v[i],v[i]+x[axis[i]]*(g in N[i])*delta)]
def advance(b,delta,x,znext):
 v=q(b,x)
 return [2*v[i]+x[axis[i]]*(g in N[i])*delta for i in range(48)],(znext-1)*v[g]
inputs=[[int(j==i) for j in range(96)] for i in range(96)]
inputs += [[1]*96, [(17*j+13)%7 for j in range(96)], [int(j%11==0) for j in range(96)]]
sequences=[[((1,1,1,1,1,1),1)]*8,
 [((2,3,5,7,11,13),17),((1,1,1,1,1,1),0),((3,1,4,1,5,9),2)]*4,
 [((0,1,0,1,0,1),0),((1,0,1,0,1,0),3),((1,2,0,3,1,0),1)]*4]
checks=0
for inp in inputs:
 for seq in sequences:
  r=inp[:];b,delta=state(inp,seq[0][1])
  for t,(x,z) in enumerate(seq):
   r=native(r,x,z)
   assert output(b,delta,x)==r
   checks+=1
   if t+1<len(seq):b,delta=advance(b,delta,x,seq[t+1][1])
assert checks==3168
result={'schema':'PREFIX593_R2_NATIVE_49STATE_V1','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'full_native_ports':96,'labelled_actions':576,'E_ones_by_generator':[31,32,32,32,32,32,1],
 'native_factor':'A_k = W E_k; T_k = E_k W; E(x,z) = X R D(z)',
 'typed_coefficient_checks':7*96*96,'exact_port_vector_checks':checks,
 'all_raw_96_ports_recovered_after_each_step':True,
 'optimal_linear_future_state_dim_for_generic_axis_and_gate':49,
 'status':'ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED'}
Path(__file__).with_name('PREFIX593_R2_native_49state_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(result['status'],checks)
